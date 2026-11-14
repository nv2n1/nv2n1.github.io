---
title: "wsgen-java-1(1)"
name: "wsgen-java-1"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsgen-java-1/"
description: "wsgen – Java(TM) API for XML Web Services (JAX-WS) 2.0"
---

<h2>Name</h2>
<p> wsgen &#8211; Java(TM) API for XML Web Services (JAX-WS) 2.0 </p>
<p> <code>Specification Version:</code> 2.1<br />
 <code>Implementation Version:</code> 2.1.1 </p>
<p> The <i>wsgen</i> tool generates JAX-WS portable artifacts used in JAX-WS web services. The tool reads a web service endpoint implementation class (SEI) and generates all the required artifacts for web service deployment, and invocation</p>
<h2>Overview</h2>
<p> The <i>wsgen</i> tool generates JAX-WS portable artifacts used in JAX-WS web services. The tool reads a web service endpoint class and generates all the required artifacts for web service deployment, and invocation. JAXWS 2.1.1 RI also provides a wsgen ant task, see <i>Wsgen ant task</i> @ <a rel="nofollow" href="https://jax-ws.dev.java.net/nonav/2.1.1/docs/wsgenant.html">https://jax-ws.dev.java.net/nonav/2.1.1/docs/wsgenant.html</a> for details. </p>
<h2>Launching wsgen</h2>
<dl>
<dt>
<dd>
<dl>
<dt>o</p>
<dd> <code>Solaris/Linux</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <i>export JAXWS_HOME=/pathto/jaxws-ri</i></p>
<dt>*</p>
<dd> <i>$JAXWS_HOME/bin/wsgen.sh -help</i></dl>
</dl>
<dt>o</p>
<dd> <code>Windows</code></p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <i>set JAXWS_HOME=c:\pathto\jaxws-ri</i></p>
<dt>*</p>
<dd> <i>%JAXWS_HOME%in\wsgen.bat -help</i></dl>
</dl>
</dl>
</dl>
<h2>Syntax</h2>
<pre>
<code>wsgen [options] &lt;SEI&gt;</code>
<br>
</pre>
<p> The following table lists the <i>wsgen</i> options. </p>
<pre>
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
<tt>-classpath &lt;path&gt;</tt>
<tt>-cp &lt;path&gt;</tt>
<tt>-d &lt;directory&gt;</tt>
<tt>-extension</tt>
<tt>-help</tt>Display help
<tt>-keep</tt>Keep generated files
<tt>-r &lt;directory&gt;</tt>
<tt>-s &lt;directory&gt;</tt>
<tt>-verbose</tt>
<tt>-version</tt>
<tt>-wsdl[:protocol]</tt>
<tt>-servicename &lt;name&gt;</tt>
<tt>-portname &lt;name&gt;</tt>
</pre>
<h2>Example</h2>
<pre>
<code>wsgen -d stock -cp myclasspath stock.StockService</code> 
</pre>
<p> This will generate the wrapper classes needed for StockService annotated with @WebService annotation inside <code>stock</code>directory. </p>
<pre>
<code>wsgen -wsdl -d stock -cp myclasspath stock.StockService</code> 
</pre>
<p> This will generate a SOAP 1.1 WSDL and schema for your Java class stock.StockService annotated with @WebService annotation. </p>
<pre>
<code>wsgen -wsdl:Xsoap1.2 -d stock -cp myclasspath stock.StockService</code> 
</pre>
<p> Will generate a SOAP 1.2 WSDL. </p>
<p> Note that you do not have to generate WSDL at the development time as JAXWS runtime will automatically generate a WSDL for you when you deploy your service. </p>
<h2>Index</h2>
