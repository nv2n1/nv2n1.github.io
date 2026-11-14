---
title: "log4cpppropertyconfigurator(3)"
name: "log4cpppropertyconfigurator"
section: "3"
letter: "l"
url: "/docs/linux/man/3-log4cpppropertyconfigurator/"
description: "log4cpp::PropertyConfigurator –"
---

<p>log4cpp::PropertyConfigurator &#8211; </p>
<p> Property configurator will read a config file using the same (or similar) format to the config file used by log4j.</p>
<h2>Synopsis</h2>
<p>#include &lt;PropertyConfigurator.hh&gt;</p>
<h3>Static Public Member Functions</h3>
<p>static void <code>configure</code> (const std::string &amp;initFileName) throw (ConfigureFailure) </p>
<h2>Detailed Description</h2>
<p>Property configurator will read a config file using the same (or similar) format to the config file used by log4j. </p>
<p> This file is in a standard Java &#8216;properties&#8217; file format. </p>
<p> Example: </p>
<p>&nbsp;<wbr> </p>
<pre># a simple test config</pre>
<pre>log4j.rootCategory=DEBUG, rootAppender
log4j.category.sub1=A1
log4j.category.sub2=INFO
log4j.category.sub1.sub2=ERROR, A2</pre>
<pre>log4j.appender.rootAppender=org.apache.log4j.ConsoleAppender
log4j.appender.rootAppender.layout=org.apache.log4j.BasicLayout</pre>
<pre>log4j.appender.A1=org.apache.log4j.FileAppender
log4j.appender.A1.fileName=A1.log
log4j.appender.A1.layout=org.apache.log4j.BasicLayout</pre>
<pre>log4j.appender.A2=org.apache.log4j.ConsoleAppender
log4j.appender.A2.layout=org.apache.log4j.PatternLayout
log4j.appender.A2.layout.ConversionPattern=The message %m at time %d%n</pre>
<p><code>Since:</code></p>
<dl COMPACT>
<dd>0.3.2</dl>
<h2>Member Function Documentation</h2>
<h3>void log4cpp::PropertyConfigurator::configure (const std::string &amp;initFileName)<code>ConfigureFailure</code> [static]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for log4cpp from the source code.</p>
