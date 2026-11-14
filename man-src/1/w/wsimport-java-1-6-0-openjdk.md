---
title: "wsimport-java-1-6-0-openjdk(1)"
name: "wsimport-java-1-6-0-openjdk"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsimport-java-1-6-0-openjdk/"
description: "wsimport – JAX-WS 2.0 Beta"
---

<p>wsimport &#8211; JAX-WS 2.0 Beta</p>
<h2>Synopsis</h2>
<pre><code>wsimport [options] &lt;wsdl&gt;</code></pre>
<h2>Description</h2>
<p>The <i>wsimport</i> tool generates JAX-WS portable artifacts, such as: </p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>o</p>
<dd>Service Endpoint Interface (SEI)</p>
<dt>o</p>
<dd>Service</p>
<dt>o</p>
<dd>Exception class mapped from wsdl:fault (if any)</p>
<dt>o</p>
<dd>Async Reponse Bean derived from response wsdl:message (if any)</p>
<dt>o</p>
<dd>JAXB generated value types (mapped java classes from schema types)</dl>
</dl>
<p> These artifacts can be packaged in a WAR file with the WSDL and schema documents along with the endpoint implementation to be deployed. </p>
<p> wsimport tool can be launched using the command line script wsimport.sh (Unix) or wsimport.bat(windows). There is also and ant task to import and compile the wsdl, see the details below. </p>
<h2>Options</h2>
<p>The following table lists the <i>wsimport</i> options. </p>
<p> Table 1-1 wsimport Options </p>
<pre><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<code>Option</code><code>Description</code>
<i>-d &lt;directory&gt;</i>
<i>-b &lt;path&gt;</i>
-catalog
<i>-extension</i>
<i>-help</i>Display help
<i>-keep</i>Keep generated files
<i>-p</i>
<i>-s &lt;directory&gt;</i>
<i>-verbose</i>
<i>-version</i>
Multiple JAX-WS and JAXB binding files can be specified using <i>-b</i> option and they can be used to customize various things like package names, bean names, etc. More information on JAX-WS and JAXB binding files can be found in the customization documentation.
<br></pre>
<h3>Ant task</h3>
<p>An Ant task for the <i>wsimport</i> tool is provided along with the tool. The attributes and elements supported by the Ant task are listed below: </p>
<pre><code> &lt;wsimport </code>
<br>
<code>
 wsdl=&quot;...&quot; </code>
<br>
<code>
 destdir=&quot;directory for generated class files&quot;</code>
<br>
<code>
 sourcedestdir=&quot;directory for generated source files&quot;</code>
<br>
<code>
 keep=&quot;true|false&quot;</code>
<br>
<code>
 extension=&quot;true|false&quot;</code>
<br>
<code>
 verbose=&quot;true|false&quot;</code>
<br>
<code>
 version=&quot;true|false&quot;</code>
<br>
<code>
 wsdlLocation=&quot;...&quot;</code>
<br>
<code>
 catalog=&quot;catalog file&quot;</code>
<br>
<code>
 package=&quot;package name&quot;</code>
<br>
<code>
 &lt;binding dir=&quot;...&quot; includes=&quot;...&quot; /&gt;</code>
<br>
<code>
 &lt;/wsimport&gt;</code></pre>
<pre><br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<code>Attribute</code><code>Description</code><code>Command line</code>
<i>wsdl</i>WSDL fileWSDL
<i>destdir</i><i>-d</i>
sourcedestdir<i>-s</i>
<i>keep</i><i>-keep</i>
<i>verbose</i><i>-verbose</i>
<i>binding</i><i>-b</i>
<i>extension</i>
<br>
<i>-extension</i>
The <i>binding</i> attributes is like a 
<i>path-like structure</i> @</pre>
<p><a rel="nofollow" href="http://ant.apache.org/manual/using.html#path">http://ant.apache.org/manual/using.html#path</a> and can also be set via nested <i>&lt;binding&gt;</i> elements, respectively. Before this task can be used, a <i>&lt;taskdef&gt;</i> element needs to be added to the project as given below: </p>
<pre><code> &lt;taskdef name=&quot;wsimport&quot; classname=&quot;com.sun.tools.ws.ant.WsImport&quot;&gt;</code>
<br>
<code>
 &lt;classpath path=&quot;jaxws.classpath&quot;/&gt;</code>
<br>
<code>
 &lt;/taskdef&gt;</code></pre>
<p>where <i>jaxws.classpath</i> is a reference to a <i>path-like structure</i> @ <a rel="nofollow" href="http://ant.apache.org/manual/using.html#path,">http://ant.apache.org/manual/using.html#path,</a> defined elsewhere in the build environment, and contains the list of classes required by the JAX-WS tools. </p>
<h2>Examples</h2>
<pre><code> &lt;wsimport</code>
<br>
<tt>destdir</tt><code>=&quot;${build.classes.home}&quot;</code>
<br>
<code>
 debug=&quot;true&quot;</code>
<br>
<code>
 wsdl=&quot;AddNumbers.wsdl&quot;</code>
<br>
<code>
 binding=&quot;custom.xml&quot;/&gt;</code></pre>
<p>The above example generates client-side artifacts for <i>AddNumbers.wsdl</i>, stores <i>.class</i> files in the <i>${build.classes.home}</i> directory using the <i>custom.xml</i> customization file. The classpath used is <i>xyz.jar</i> and compiles with debug information on. </p>
<pre><code> &lt;wsimport</code>
<br>
<code>
 keep=&quot;true&quot;</code>
<br>
<code>
 sourcedestdir=&quot;${source.dir}&quot;</code>
<br>
<tt>destdir</tt><code>=&quot;${build.classes.home}&quot;</code>
<br>
<code>
 wsdl=&quot;AddNumbers.wsdl&quot;&gt;</code>
<br>
<code>
 &lt;binding dir=&quot;${basedir}/etc&quot; includes=&quot;custom.xml&quot;/&gt;</code>
<br>
<code>
 &lt;/wsimport&gt;</code></pre>
<p>The above example generates portable artifacts for <i>AddNumbers.wsdl</i>, stores <i>.java</i> files in the <i>${source.dir}</i> directory, stores <i>.class</i> files in the <i>${build.classes.home}</i> directory. </p>
<h2>Notes</h2>
<p>Summary of Changed and Removed wsimport ant attributes: </p>
<p> <code>base</code> replaced by <code>destdir</code> </p>
<p> <code>sourceBase</code> is replaced by <code>sourcedestdir</code> </p>
<p> <code>wsdlFile</code> is replaced by <code>wsdl</code> </p>
<p> <code>httpProxy</code> is removed. Use ant&#8217;s setproxy task instead for proxy configuration. </p>
<p> <code>version</code> is removed </p>
<p>&nbsp;<wbr></p>
