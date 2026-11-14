---
title: "schemagen-java-1-6-0-openjdk(1)"
name: "schemagen-java-1-6-0-openjdk"
section: "1"
letter: "s"
url: "/docs/linux/man/1-schemagen-java-1-6-0-openjdk/"
description: "schemagen – Java(TM) Architecture for XML Binding Schema Generator Specification Version: 2.0 Reference Implementation (RI) Version: 2.0 ea3"
---

<p>schemagen &#8211; Java(TM) Architecture for XML Binding Schema Generator <code>Specification Version:</code> 2.0<br />
 <code>Reference Implementation (RI) Version:</code> 2.0 ea3 </p>
<h3>Launching schemagen</h3>
<p>The schema generator can be launched using the appropriate <i>schemagen</i> shell script in the <i>bin</i> directory for your platform. </p>
<p> The current schema generator can process either Java source files or class files. </p>
<p> We also provide an Ant task to run the schema generator &#8211; see the instructions for using schemagen with Ant. </p>
<dl COMPACT>
<dd><code>For Solaris/Linux</code> </p>
<pre><code> % path/to/jaxb/bin/schemagen.sh Foo.java Bar.java ...
 Note: Writing schema1.xsd
 </code></pre>
<p><code>For WindowsNT/2000/XP</code> </p>
<pre><code> &gt; path	o\jaxbin\schemagen.bat Foo.java Bar.java ...
 Note: Writing schema1.xsd
 </code></pre>
</dl>
<p> If your java sources/classes reference other classes, they must be accessable on your system CLASSPATH environment variable, or they need to be given to the tool by using the <i>-classpath</i>/<i>-cp</i> options. Otherwise you will see errors when generating your schema. </p>
<dl COMPACT>
<dd><code>Command Line Options</code> </p>
<dl COMPACT>
<dd>
<pre><code>Usage: schemagen [-options ...] &lt;java files&gt; 
Options: 
 -d &lt;path&gt; : Specify where to place processor and javac generated class files 
 -cp &lt;path&gt; : Specify where to find user specified files 
 -classpath &lt;path&gt; : Specify where to find user specified files 
 -help : Display this usage message
 </code></pre>
</dl>
</dl>
<h3>Generated Resource Files</h3>
<p>The current schema generator simply creates a schema file for each namespace referenced in your Java classes. There is no way to control the name of the generated schema files at this time. For that purpose, use the schema generator ant task. </p>
<h2>See Also</h2>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>o</p>
<dd>JAXB 2.0:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>Release Notes</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/ReleaseNotes.html">http://java.sun.com/webservices/docs/2.0/jaxb/ReleaseNotes.html</a></p>
<dt>*</p>
<dd><i>XJC</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/xjc.html">http://java.sun.com/webservices/docs/2.0/jaxb/xjc.html</a></p>
<dt>*</p>
<dd><i>XJCTask</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/xjcTask.html">http://java.sun.com/webservices/docs/2.0/jaxb/xjcTask.html</a></p>
<dt>*</p>
<dd><i>SchemaGen</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/schemagen.html">http://java.sun.com/webservices/docs/2.0/jaxb/schemagen.html</a></p>
<dt>*</p>
<dd><i>schemagenTask</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/schemagenTask.html">http://java.sun.com/webservices/docs/2.0/jaxb/schemagenTask.html</a></p>
<dt>*</p>
<dd><i>Sample Apps</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/samples.html">http://java.sun.com/webservices/docs/2.0/jaxb/samples.html</a></p>
<dt>*</p>
<dd><i>Changelog</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/changelog2.html">http://java.sun.com/webservices/docs/2.0/jaxb/changelog2.html</a></dl>
</dl>
<dt>o</p>
<dd>JAXB 1.0.x:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>Release Notes</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/jaxb-1_0.html">http://java.sun.com/webservices/docs/2.0/jaxb/jaxb-1_0.html</a></p>
<dt>*</p>
<dd><i>Changelog</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/changelog.html">http://java.sun.com/webservices/docs/2.0/jaxb/changelog.html</a></dl>
</dl>
<dt>o</p>
<dd>JAXB RI Extensions:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>Runtime Properties</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/vendorProperties.html">http://java.sun.com/webservices/docs/2.0/jaxb/vendorProperties.html</a></p>
<dt>*</p>
<dd><i>XJC Customizations</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/vendorCustomizations.html">http://java.sun.com/webservices/docs/2.0/jaxb/vendorCustomizations.html</a></p>
<dt>*</p>
<dd><i>Develop Plugins</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/developPlugins.html">http://java.sun.com/webservices/docs/2.0/jaxb/developPlugins.html</a></dl>
</dl>
<dt>o</p>
<dd>JAXB RI Schema Languages:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>W3C XML Schema</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/vendorSchemaLangs.html#xschema">http://java.sun.com/webservices/docs/2.0/jaxb/vendorSchemaLangs.html#xschema</a></p>
<dt>*</p>
<dd><i>RELAX NG</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/vendorSchemaLangs.html#relaxng">http://java.sun.com/webservices/docs/2.0/jaxb/vendorSchemaLangs.html#relaxng</a></p>
<dt>*</p>
<dd><i>DTD</i> @ <a rel="nofollow" href="http://java.sun.com/webservices/docs/2.0/jaxb/vendorSchemaLangs.html#dtd">http://java.sun.com/webservices/docs/2.0/jaxb/vendorSchemaLangs.html#dtd</a></dl>
</dl>
<dt>o</p>
<dd>JAXB Community:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>Java.net Homepage</i> @ <a rel="nofollow" href="http://jaxb.dev.java.net">http://jaxb.dev.java.net</a></p>
<dt>*</p>
<dd><i>Developer interest list</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/servlets/ProjectMailingListList">https://jaxb.dev.java.net/servlets/ProjectMailingListList</a></p>
<dt>*</p>
<dd><i>FAQ</i> @ <a rel="nofollow" href="https://jaxb.dev.java.net/faq/index.html">https://jaxb.dev.java.net/faq/index.html</a></dl>
</dl>
</dl>
</dl>
<p>&nbsp;<wbr></p>
