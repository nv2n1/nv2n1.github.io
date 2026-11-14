---
title: "schemagen-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64(1)"
name: "schemagen-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64"
section: "1"
letter: "s"
url: "/docs/linux/man/1-schemagen-java-1-8-0-openjdk-1-8-0-65-3-b17-fc22-x86_64/"
description: "schemagen – Generates a schema for every name space that is referenced in your Java classes."
---

<p>schemagen &#8211; Generates a schema for every name space that is referenced in your Java classes.</p>
<h2>Synopsis</h2>
<pre><code>schemagen</code> [ <i>options</i> ] <i>java-files</i></pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>java-files</i></p>
<dd>The Java class files to be processed.</dl>
<h2>Description</h2>
<p>The schema generator creates a schema file for each name space referenced in your Java classes. Currently, you cannot control the name of the generated schema files. To control the schema file names, see Using SchemaGen with Ant at <a rel="nofollow" href="http://jaxb.java.net/nonav/2.2.3u1/docs/schemagenTask.html">http://jaxb.java.net/nonav/2.2.3u1/docs/schemagenTask.html</a> </p>
<p> Start the schema generator with the appropriate <code>schemagen</code> shell script in the bin directory for your platform. The current schema generator can process either Java source files or class files. </p>
<pre><code>schemagen.sh Foo.java Bar.java ...</code></pre>
<pre><code>Note: Writing schema1.xsd</code></pre>
<p>If your java files reference other classes, then those classes must be accessible on your system <code>CLASSPATH</code> environment variable, or they need to be specified in the <code>schemagen</code> command line with the class path options. See Options. If the referenced files are not accessible or specified, then you get errors when you generate the schema.</p>
<h2>Options</h2>
<dl COMPACT>
<dt>-d <i>path</i></p>
<dd>The location where the <code>schemagen</code> command places processor-generated and <code>javac</code>-generated class files.</p>
<dt>-cp <i>path</i></p>
<dd>The location where the <code>schemagen</code> command places user-specified files.</p>
<dt>-classpath <i>path</i></p>
<dd>The location where the <code>schemagen</code> command places user-specified files.</p>
<dt>-encoding <i>encoding</i></p>
<dd>Specifies the encoding to use for <code>apt</code> or <code>javac</code> command invocations.</p>
<dt>-episode <i>file</i></p>
<dd>Generates an episode file for separate compilation.</p>
<dt>-version</p>
<dd>Displays release information.</p>
<dt>-help</p>
<dd>Displays a help message.</dl>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd>Using SchemaGen with Ant at <a rel="nofollow" href="http://jaxb.java.net/nonav/2.2.3u1/docs/schemagenTask.html">http://jaxb.java.net/nonav/2.2.3u1/docs/schemagenTask.html</a></p>
<dt>&bull;</p>
<dd>Java Architecture for XML Binding (JAXB) at <a rel="nofollow" href="http://docs.oracle.com/javase/8/docs/technotes/guides/xml/jaxb/index.html">http://docs.oracle.com/javase/8/docs/technotes/guides/xml/jaxb/index.html</a> </p>
</dl>
