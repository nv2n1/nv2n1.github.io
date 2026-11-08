---
title: "Building Executable JARs in Scala with sbt"
date: 2018-03-24 11:41:00 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-package-a-scala-project-to-a-jar-with-sbt/
---

The simplest approach creates a JAR with just your project’s compiled classes:

``` bash
sbt package
```

This outputs to `target/scala-2.x.y/projectname_2.x.y-zz.jar`. The naming convention includes the Scala version to prevent classpath conflicts when multiple Scala versions coexist.

For iterative development, use watch mode:

``` bash
sbt ~package
```

This rebuilds the JAR after every source change. However, this JAR only contains your project’s code—not its dependencies. Use it for publishing to repositories where dependency management is handled separately.

## Standalone JAR with Dependencies

For a self-contained executable JAR that includes all dependencies, use the sbt-assembly plugin. This is the standard approach for distributable applications.

Add it to `project/plugins.sbt`:

``` scala
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.2.0")
```

Then build the assembly:

``` bash
sbt assembly
```

This produces `target/scala-2.x.y/projectname-assembly-x.y.jar`—a single JAR with everything bundled.

Run it with:

``` bash
java -jar projectname-assembly-x.y.jar [arguments]
```

### Setting a Main Class

If your project has a main class, configure it in `build.sbt`:

``` scala
assembly / mainClass := Some("com.example.Main")
```

Then the JAR runs without specifying the class name:

``` bash
java -jar projectname-assembly-x.y.jar
```

If you don’t set a main class and want to run a specific one, use:

``` bash
java -cp projectname-assembly-x.y.jar com.example.Main [arguments]
```

## Handling Merge Conflicts

When combining dependencies, you may encounter conflicting files (META-INF resources, logging configs, or duplicate files). Configure merge strategies in `build.sbt`:

``` scala
assembly / assemblyMergeStrategy := {
  case PathList("META-INF", xs @ _*) =>
    xs match {
      case "services" :: xs => MergeStrategy.filterDistinctLines
      case "MANIFEST.MF" :: Nil => MergeStrategy.discard
      case _ => MergeStrategy.first
    }
  case "application.conf" => MergeStrategy.concat
  case "reference.conf" => MergeStrategy.concat
  case x => MergeStrategy.first
}
```

Common strategies:

- `MergeStrategy.discard` — ignore the file
- `MergeStrategy.first` — keep the first occurrence
- `MergeStrategy.concat` — merge text files (useful for configs)
- `MergeStrategy.filterDistinctLines` — combine and deduplicate lines

If a particular dependency causes conflicts, you can also exclude it entirely:

``` scala
assembly / assemblyExcludedJars := {
  val cp = (assembly / fullClasspath).value
  cp.filter(_.data.getName == "some-dependency.jar")
}
```

## Excluding the Scala Runtime

If your deployment environment already provides Scala (Spark clusters, for example), exclude it to reduce JAR size:

``` scala
assembly / assemblyOption := (assembly / assemblyOption).value
  .copy(includeScala = false)
```

This can reduce JAR size from 30+ MB to a few MB depending on your dependencies.

## Skipping Tests

Speed up packaging by skipping test compilation:

``` bash
sbt 'set test in assembly := {}' assembly
```

Or configure it permanently in `build.sbt`:

``` scala
assembly / test := {}
```

## Verifying the JAR

List contents to confirm everything is included:

``` bash
jar tf projectname-assembly-x.y.jar | head -20
```

Check the manifest to verify the main class:

``` bash
jar xf projectname-assembly-x.y.jar META-INF/MANIFEST.MF
cat META-INF/MANIFEST.MF
```

Look for the `Main-Class` entry. Count total class files:

``` bash
jar tf projectname-assembly-x.y.jar | grep '\.class$' | wc -l
```

Check JAR size:

``` bash
du -h projectname-assembly-x.y.jar
```

## Publishing vs Distribution

Use plain `sbt package` when publishing to Maven Central or a private repository—the dependency manager will resolve transitive dependencies at install time.

Use `sbt assembly` when building a final application for distribution, especially if the end user doesn’t manage Scala dependencies themselves or when you need a standalone executable.

For reproducible builds, pin the sbt-assembly version in `project/plugins.sbt` and consider using `assembly / assemblyJarName` to control output naming:

``` scala
assembly / assemblyJarName := s"${name.value}-${version.value}.jar"
```
