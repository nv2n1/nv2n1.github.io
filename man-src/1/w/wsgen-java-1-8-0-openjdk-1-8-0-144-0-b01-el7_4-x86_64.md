---
title: "wsgen-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64(1)"
name: "wsgen-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsgen-java-1-8-0-openjdk-1-8-0-144-0-b01-el7_4-x86_64/"
description: "wsgen – Reads a web service endpoint implementation (SEI) class and generates all of the required artifacts for web service deployment, and invocation."
---

<p>wsgen &#8211; Reads a web service endpoint implementation (SEI) class and generates all of the required artifacts for web service deployment, and invocation.</p>
<h2>Synopsis</h2>
<pre><code>wsgen</code> [ <i>options</i> ] <i>SEI</i></pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>SEI</i></p>
<dd>The web service endpoint implementation class (SEI) to be read.</dl>
<h2>Description</h2>
<p>The <code>wsgen</code> command generates JAX-WS portable artifacts used in JAX-WS web services. The tool reads a web service endpoint class and generates all the required artifacts for web service deployment and invocation. JAXWS 2.1.1 RI also provides a <code>wsgen</code> Ant task, see the <i>Tools</i> tab of the JAX-WS (wsgen) page at <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/wsgenant.html">http://jax-ws.java.net/nonav/2.1.1/docs/wsgenant.html</a> </p>
<p> To start the <code>wsgen</code> command, do the following: </p>
<pre><code>export JAXWS_HOME=/pathto/jaxws-ri</code></pre>
<pre><code>$JAXWS_HOME/bin/wsgen.sh -help</code></pre>
<h2>Options</h2>
<dl COMPACT>
<dt>-classpath <i>path</i></p>
<dd>The location of the input class files.</p>
<dt>-cp <i>path</i></p>
<dd>The location of the input class files.</p>
<dt>-d <i>directory</i></p>
<dd>The location for where to place generated output files.</p>
<dt>-extension</p>
<dd>Allow vendor extensions. Use of extensions can result in applications that are not portable or that do not work with other implementations.</p>
<dt>-help</p>
<dd>Displays a help message about the <code>wsgen</code> command.</p>
<dt>-keep</p>
<dd>Keeps the generated files.</p>
<dt>-r <i>directory</i></p>
<dd>Uses this option with the <code>-wsdl</code> option to specify where to place generated resource files such as WSDLs.</p>
<dt>-s <i>directory</i></p>
<dd>The location for where to place generated source files.</p>
<dt>-verbose</p>
<dd>Displays compiler messages.</p>
<dt>-version</p>
<dd>Prints release information.</p>
<dt>-wsdl [ :protocol ] <i></i></p>
<dd>An optional command that generates a WSDL file to review before endpoint deployment. The WSDL files contains a machine-readable description of how the service can be called, what parameters it expects, and what data structures it returns. </p>
<p> By default the <code>wsgen</code> command does not generate a WSDL file. The <code>protocol</code> value is optional and is used to specify what protocol should be used for the WSDL binding (<code>wsdl:binding</code>). Valid protocols are <code>soap1.1</code> and <code>Xsoap1.2</code>. The default is <code>soap1.1</code>. The <code>Xsoap1.2</code> protocol is not standard and can only be used with the <code>-extension</code> option.</p>
<dt>-servicename <i>name</i></p>
<dd>Used only with the <code>-wsdl</code> option to specify a particular WSDL service (<code>wsdl:service</code>) name to be generated in the WSDL, for example: <code>-servicename &quot;{<a rel="nofollow" href="http://mynamespace/}MyService">http://mynamespace/}MyService</a>&quot;</code>.</p>
<dt>-portname <i>name</i></p>
<dd>Used only with the <code>-wsdl</code> option to specify a particular WSDL port (<code>wsdl:port</code>) name to be generated in the WSDL, for example: <code>-portname &quot;{<a rel="nofollow" href="http://mynamespace/}MyPort">http://mynamespace/}MyPort</a>&quot;</code>.</dl>
<h2>Examples</h2>
<p>The following example generates the wrapper classes for <code>StockService</code> with <code>@WebService</code> annotations inside stock directory. </p>
<pre><code>wsgen -d stock -cp myclasspath stock.StockService</code></pre>
<p>The following example generates a SOAP 1.1 WSDL and schema for the <code>stock.StockService</code> class with <code>@WebService</code> annotations. </p>
<pre><code>wsgen -wsdl -d stock -cp myclasspath stock.StockService</code></pre>
<p>The following example generates a SOAP 1.2 WSDL. </p>
<pre><code>wsgen -wsdl:Xsoap1.2 -d stock -cp myclasspath stock.StockService </code></pre>
<p><i>Note:</i> You do not have to generate WSDL at development time because the JAXWS run time environment generates a WSDL for you when you deploy your service.</p>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-wsimport/">wsimport</a>(1)</p>
<dt>&bull;</p>
<dd><i>The Tools</i> tab of the JAX-WS (wsgen) page <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/wsgenant.html">http://jax-ws.java.net/nonav/2.1.1/docs/wsgenant.html</a> </p>
</dl>
