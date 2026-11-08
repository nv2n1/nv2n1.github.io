---
title: "Installing Scala on Fedora Linux"
date: 2018-03-24 08:16:53 +0000
layout: post
canonical: https://www.systutorials.com/how-to-install-scala-on-fedora-linux-2/
---

Scala runs on the JVM and combines object-oriented and functional programming. Here’s how to install Scala on Fedora Linux using several methods.

## Method 1: Install via Coursier (Recommended)

Coursier is the official Scala installer and handles JDK dependencies automatically:

```wp-block-code
# Install Coursier
curl -fL https://github.com/coursier/coursier/releases/latest/download/cs-x86_64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup

# This installs:
# - Scala compiler (scalac)
# - Scala REPL (scala)
# - sbt build tool
# - ammonite (enhanced REPL)
# - scalafmt (code formatter)
```

After installation, restart your shell or run `source ~/.bashrc`.

## Method 2: Install via SDKMAN

SDKMAN manages multiple versions of JVM-based tools:

```wp-block-code
# Install SDKMAN
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Install latest Scala
sdk install scala

# Install specific version
sdk install scala 3.4.2

# Install sbt (Scala Build Tool)
sdk install sbt

# List available versions
sdk list scala
```

## Method 3: DNF Package Manager

Fedora includes Scala in its repositories (may not be the latest version):

```wp-block-code
sudo dnf install scala
```

## Verify Installation

```wp-block-code
scala -version
scalac -version
```

## Scala REPL Quick Start

Launch the REPL to experiment with Scala:

```wp-block-code
$ scala
Welcome to Scala 3.4.2
Type in expressions for evaluation.

scala> val message = "Hello, Scala!"
val message: String = Hello, Scala!

scala> def add(a: Int, b: Int): Int = a + b
def add(a: Int, b: Int): Int

scala> add(3, 4)
val res0: Int = 7

scala> :quit
```

## Create a Simple Project with sbt

```wp-block-code
# Create project directory
mkdir myproject && cd myproject

# Create build file
echo 'name := "MyProject"
version := "0.1"
scalaVersion := "3.4.2"' > build.sbt

# Create source file
mkdir -p src/main/scala
cat > src/main/scala/Main.scala << 'EOF'
@main def hello(): Unit =
  println("Hello, Scala 3!")
EOF

# Run
sbt run
```

## Scala 2 vs Scala 3

Scala 3 (released 2021) introduces significant language changes:

- New indentation-based syntax (optional)
- `given/using` replaces `implicit` for context parameters
- Extension methods replace implicit classes
- Union and intersection types
- Omit parentheses for no-arg methods

Most libraries support both Scala 2.13 and Scala 3. For new projects, use Scala 3 unless you have a specific dependency that requires 2.13.

## IDE Support

**Metals** is the recommended Scala language server, works with VS Code and other editors:

```wp-block-code
# Install Metals for VS Code
# Install the "Scala (Metals)" extension from the marketplace

# For Vim/Neovim with CoC or nvim-lsp
# Metals is auto-configured by most Scala plugins
```

**IntelliJ IDEA** with the Scala plugin provides the most full-featured Scala development environment with debugger integration, refactoring, and sbt support.

## Quick Reference

- `Coursier setup` — Install Scala and tools (recommended)
- `sdk install scala` — SDKMAN method
- `sudo dnf install scala` — System package
- `sbt new scala/scala3.g8` — Create new project from template
- `sbt run` — Build and run
- `sbt console` — REPL with project dependencies

## Building and Running Scala Projects

Common sbt commands for daily development:

```wp-block-code
sbt compile          # Compile the project
sbt test             # Run all tests
sbt "testOnly *.MySpec"  # Run specific test
sbt assembly         # Build a fat JAR
sbt run              # Run the main class
sbt console          # REPL with project classpath
sbt reload           # Reload build.sbt changes
sbt clean            # Clean build artifacts
```

## Scala Resources

Official documentation and learning resources:

- **Scala Documentation:** https://docs.scala-lang.org
- **Scala Exercises:** https://www.scala-exercises.org
- **Scastie:** https://scastie.scala-lang.org (online playground)
- **Rock the JVM:** Popular Scala tutorial series

Scala is well-suited for data engineering (Apache Spark), backend services (Akka/Pekka), and functional programming. The strong type system catches errors at compile time that would be runtime errors in dynamically typed languages.
