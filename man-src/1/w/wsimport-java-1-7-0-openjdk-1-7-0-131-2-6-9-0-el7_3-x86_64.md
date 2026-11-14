---
title: "wsimport-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64(1)"
name: "wsimport-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsimport-java-1-7-0-openjdk-1-7-0-131-2-6-9-0-el7_3-x86_64/"
description: "wsimport – Java(TM) API for XML Web Services (JAX-WS) 2.0"
---

<p>wsimport &#8211; Java(TM) API for XML Web Services (JAX-WS) 2.0 </p>
<p> <code>Specification Version:</code> 2.1<br />
 <code>Implementation Version:</code> 2.1.1 </p>
<h2>Overview</h2>
<p>The <i>wsimport</i> tool generates JAX-WS portable artifacts, such as:</p>
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
<p> These artifacts can be packaged in a WAR file with the WSDL and schema documents along with the endpoint implementation to be deployed. also provides wsimport ant task, see <i>Wsimport ant task</i> @ <a rel="nofollow" href="https://jax-ws.dev.java.net/nonav/2.1.1/docs/wsimportant.html.">https://jax-ws.dev.java.net/nonav/2.1.1/docs/wsimportant.html.</a> </p>
<h2>Launching wsimport</h2>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>o</p>
<dd><code>Solaris/Linux</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>/bin/wsimport.sh -help</i></dl>
</dl>
<dt>o</p>
<dd><code>Windows</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd><i>in\wsimport.bat -help</i></dl>
</dl>
</dl>
</dl>
<h2>Syntax</h2>
<pre><code>wsimport [options] &lt;wsdl&gt;</code></pre>
<p>The following table lists the <i>wsimport</i> options. </p>
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
<pre><code>Option</code><code>Description</code>
<code>-d &lt;directory&gt; </code>
<code>-b &lt;path&gt; </code>
<code>-B &lt;jaxbOption&gt;</code>
<code>-catalog</code>
<code>-extension </code>
<code>-help </code>Display help
<code>-keep </code>Keep generated files
<code>-p </code>
<code>-s &lt;directory&gt; </code>
<code>-verbose </code>
<code>-version </code>
<code>-target </code>
<code>-quiet </code>Suppress wsimport output
Multiple JAX-WS and JAXB binding files can be specified using <i>-b</i> option and they can be used to customize various things like package names, bean names, etc. More information on JAX-WS and JAXB binding files can be found in the 
<i>customization documentation</i> @</pre>
<p><a rel="nofollow" href="https://jax-ws.dev.java.net/nonav/2.1.1/docs/customizations.html.">https://jax-ws.dev.java.net/nonav/2.1.1/docs/customizations.html.</a> </p>
<p> The following table lists <i>wsimport</i> non-standard options: </p>
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
<pre><code>Option</code><code>Description</code>
<code>-XadditionalHeaders</code>
<code>-Xauthfile &lt;file&gt;</code>
<code>-Xdebug</code>
<code>-Xnocompile</code></pre>
<h2>Example</h2>
<pre><code>wsimport -p stockquote <a rel="nofollow" href="http://stockquote.example.com/quote?wsdl">http://stockquote.example.com/quote?wsdl</a></code></pre>
<p>This will generate the Java artifacts and compile them by importing the <i><a rel="nofollow" href="http://stockquote.example.com/quote?wsdl">http://stockquote.example.com/quote?wsdl</a></i>. </p>
<p>&nbsp;<wbr></p>
