---
title: "wsgen-java-1-6-0-openjdk(1)"
name: "wsgen-java-1-6-0-openjdk"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsgen-java-1-6-0-openjdk/"
description: "wsgen – JAX-WS 2.0 Beta"
---

<p>wsgen &#8211; JAX-WS 2.0 Beta </p>
<dl COMPACT>
<dd>The <i>wsgen</i> tool generates JAX-WS portable artifacts used in JAX-WS web services. The tool reads a web service endpoint implementation class (SEI) and generates all the required artifacts for web service deployment, and invocation. </p>
</dl>
<h2>Synopsis</h2>
<pre><code>wsgen [options] &lt;SEI&gt;</code></pre>
<h2>Options</h2>
<p>The following table lists the <i>wsgen</i> options. </p>
<p> Table 1-1 wsgen Options </p>
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
<i>-classpath &lt;path&gt;</i>
<i>-cp &lt;path&gt;</i>
<i>-d &lt;directory&gt;</i>
<i>-extension</i>
<i>-help</i>Display help
<i>-keep</i>Keep generated files
<i>-r &lt;directory&gt;</i>
<i>-s &lt;directory&gt;</i>
<i>-verbose</i>
<i>-version</i>
<i>-servicename &lt;name&gt;</i>
<i>-portname &lt;name&gt;</i></pre>
<h3>Ant task</h3>
<p>An Ant task for the <i>wsgen</i> tool is provided along with the tool. The attributes and elements supported by the Ant task are listed below: </p>
<pre><code> 
 &lt;wsgen 
 sei=&quot;...&quot;
 destdir=&quot;directory for generated class files&quot; 
 classpath=&quot;classpath&quot; | cp=&quot;classpath&quot;
 resourcedestdir=&quot;directory for generated resource files such as WSDLs&quot;
 sourcedestdir=&quot;directory for generated source files&quot; 
 keep=&quot;true|false&quot;
 verbose=&quot;true|false&quot;
 genwsdl=&quot;true|false&quot; 
 protocol=&quot;soap1.1|Xsoap1.2&quot;
 servicename=&quot;...&quot;
 portname=&quot;...&quot;&gt;
 extension=&quot;true|false&quot;
 &lt;classpath refid=&quot;...&quot;/&gt;
 &lt;/wsgen&gt;</code></pre>
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
<code>Attribute</code><code>Description</code><code>Command line</code>
<i>sei</i>SEI
<i>destdir</i><i>-d</i>
<i>classpath</i><i>-classpath</i>
<i>cp</i>Same as <i>-classpath</i><i>-cp</i>
<i>resourcedestdir</i><i>-r</i>
<i>sourcedestdir</i><i>-s</i>
<i>keep</i>Keep generated files<i>-keep</i>
<i>verbose</i><i>-verbose</i>
<i>genwsdl</i>
<br>
<i>-wsdl</i>
<i>protocol</i>
<br>
<i>servicename</i>
<br>
<i>-servicename</i>
<i>portname</i>
<br>
<i>-servicename</i>
<i>extension</i>
<br>
<i>-extension</i>
The <i>classpath</i> attribute is a 
<i>path-like structure</i> @</pre>
<p><a rel="nofollow" href="http://ant.apache.org/manual/using.html#path">http://ant.apache.org/manual/using.html#path</a> and can also be set via nested <i>&lt;classpath&gt;</i> elements. Before this task can be used, a <i>&lt;taskdef&gt;</i> element needs to be added to the project as given below: </p>
<pre><code> &lt;taskdef name=&quot;wsgen&quot; classname=&quot;com.sun.tools.ws.ant.WsGen&quot;&gt;</code>
<br>
<code>
 &lt;classpath path=&quot;jaxws.classpath&quot;/&gt;</code>
<br>
<code>
 &lt;/taskdef&gt;</code></pre>
<p>where <i>jaxws.classpath</i> is a reference to a <i>path-like structure</i> @ <a rel="nofollow" href="http://ant.apache.org/manual/using.html#path,">http://ant.apache.org/manual/using.html#path,</a> defined elsewhere in the build environment, and contains the list of classes required by the JAX-WS tools. </p>
<h2>Example</h2>
<pre><code>&lt;wsgen 
 resourcedestdir=&quot;${wsdl.dir}&quot;
 sei=&quot;fromjava.server.AddNumbersImpl&quot;&gt;
 &lt;classpath refid=&quot;compile.classpath&quot;/&gt;
&lt;/wsgen&gt;</code></pre>
<p>&nbsp;<wbr></p>
