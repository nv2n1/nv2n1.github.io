---
title: "schemagen-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64(1)"
name: "schemagen-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64"
section: "1"
letter: "s"
url: "/docs/linux/man/1-schemagen-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64/"
description: "See Also"
---

<p>schemagen &#8211; Java(TM) Architecture for XML Binding Schema Generator </p>
<p> <code>Specification Version:</code> 2.1<br />
 <code>Implementation Version:</code> 2.1.3 </p>
<h2>Launching schemagen</h2>
<p>The schema generator can be launched using the appropriate <i>schemagen</i> shell script in the <i>bin</i> directory for your platform. </p>
<p> The current schema generator can process either Java source files or class files. </p>
<p> We also provide an Ant task to run the schema generator &#8211; see the instructions for <i>using schemagen with Ant</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagenTask.html.">https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagenTask.html.</a> </p>
<pre><code>% schemagen.sh Foo.java Bar.java ...
Note: Writing schema1.xsd</code></pre>
<p>If your java sources/classes reference other classes, they must be accessable on your system CLASSPATH environment variable, or they need to be given to the tool by using the <i>-classpath</i>/<i>-cp</i> options. Otherwise you will see errors when generating your schema. </p>
<h3>Command Line Options</h3>
<pre><code>Usage: schemagen [-options ...] &lt;java files&gt; 
Options:
 -d &lt;path&gt; : specify where to place processor and javac generated class files
 -cp &lt;path&gt; : specify where to find user specified files
 -classpath &lt;path&gt; : specify where to find user specified files
 -encoding &lt;encoding&gt; : specify encoding to be used for apt/javac invocation
 -episode &lt;file&gt; : generate episode file for separate compilation
 -version : display version information
 -help : display this usage message</code></pre>
<h2>Generated Resource Files</h2>
<p>The current schema generator simply creates a schema file for each namespace referenced in your Java classes. There is no way to control the name of the generated schema files at this time. For that purpose, use <i>the schema generator ant task</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagenTask.html.">https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagenTask.html.</a> </p>
<h2>Name</h2>
<p>See Also </p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>o</p>
<dd>Running the schema generator (schemagen): [ <i>command-line instructions</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagen.html,">https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagen.html,</a> <i>using the SchemaGen Ant task</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagenTask.html]">https://jaxb.dev.java.net/nonav/2.1.3/docs/schemagenTask.html]</a></p>
<dt>o</p>
<dd><i>Java Architecture for XML Binding (JAXB)</i> @ <a rel="nofollow" href="http://docs.oracle.com/javase/7/docs/technotes/guides/xml/jaxb/index.html">http://docs.oracle.com/javase/7/docs/technotes/guides/xml/jaxb/index.html</a></dl>
</dl>
<p>&nbsp;<wbr></p>
