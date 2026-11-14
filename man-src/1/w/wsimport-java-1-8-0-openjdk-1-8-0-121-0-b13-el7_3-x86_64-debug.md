---
title: "wsimport-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug(1)"
name: "wsimport-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsimport-java-1-8-0-openjdk-1-8-0-121-0-b13-el7_3-x86_64-debug/"
description: "wsimport – Generates JAX-WS portable artifacts that can be packaged in a web application archive (WAR) file and provides an Ant task."
---

<p>wsimport &#8211; Generates JAX-WS portable artifacts that can be packaged in a web application archive (WAR) file and provides an Ant task.</p>
<h2>Synopsis</h2>
<pre><code>wsimport</code> [ <i>options</i> ] <i>wsdl</i></pre>
<dl COMPACT>
<dt><i>options</i></p>
<dd>The command-line options. See Options.</p>
<dt><i>wsdl</i></p>
<dd>The file that contains the machine-readable description of how the web service can be called, what parameters it expects, and what data structures it returns.</dl>
<h2>Description</h2>
<p>The <code>wsimport</code> command generates the following JAX-WS portable artifacts. These artifacts can be packaged in a WAR file with the WSDL and schema documents and the endpoint implementation to be deployed. The <code>wsimport</code> command also provides a <code>wsimport</code> Ant task, see the Tools tab of the Wsimport Ant Task page at <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html">http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html</a></p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Service Endpoint Interface (SEI)</p>
<dt>&bull;</p>
<dd>Service</p>
<dt>&bull;</p>
<dd>Exception class is mapped from <code>wsdl:fault</code> (if any)</p>
<dt>&bull;</p>
<dd>Async Response Bean is derived from response <code>wsdl:message</code> (if any)</p>
<dt>&bull;</p>
<dd>JAXB generated value types (mapped java classes from schema types)</dl>
<p> To start the <code>wsgen</code> command, do the following: </p>
<p> <i>Oracle Solaris/Linux</i>: </p>
<pre><code>/bin/wsimport.sh -help</code></pre>
<p><i>Windows</i>: </p>
<pre><code>in\wsimport.bat -help</code></pre>
<h2>Options</h2>
<dl COMPACT>
<dt>-d <i>directory</i></p>
<dd>Specifies where to place generated output files.</p>
<dt>-b <i>path</i></p>
<dd>Specifies external JAX-WS or JAXB binding files. Multiple JAX-WS and JAXB binding files can be specified with the <code>-b</code> option. You can use these files to customize package names, bean names, and so on. For more information about JAX-WS and JAXB binding files, see the <i>Users Guide</i> tab of WSDL Customization at <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html">http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html</a></p>
<dt>-B <i>jaxbOption</i></p>
<dd>Passes the <code>jaxbOption</code> option to the JAXB schema compiler.</p>
<dt>-catalog</p>
<dd>Specifies a catalog file to resolve external entity references. The <code>-catalog</code> option supports the TR9401, XCatalog, and OASIS XML Catalog formats. See the <i>Users Guide</i> tab of the Catalog Support page at <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/catalog-support.html">http://jax-ws.java.net/nonav/2.1.1/docs/catalog-support.html</a></p>
<dt>-extension</p>
<dd>Allows vendor extensions. Use of extensions can result in applications that are not portable or that do not work with other implementations.</p>
<dt>-help</p>
<dd>Displays a help message for the <code>wsimport</code> command.</p>
<dt>-httpproxy: <i>host</i>:<i>port</i></p>
<dd>Specifies an HTTP proxy server. The default is 8080.</p>
<dt>-keep</p>
<dd>Keeps generated files.</p>
<dt>-p <i>name</i></p>
<dd>Specifies a target package <i>name</i> to override the WSDL and schema binding customizations, and the default algorithm defined in the specification.</p>
<dt>-s <i>directory</i></p>
<dd>Specifies where to place generated source files.</p>
<dt>-verbose</p>
<dd>Displays compiler messages.</p>
<dt>-version</p>
<dd>Prints release information.</p>
<dt>-wsdllocation <i>location</i></p>
<dd>Specifies the <code>@WebServiceClient.wsdlLocation</code> value.</p>
<dt>-target</p>
<dd>Generates code according to the specified JAX-WS specification version. Version 2.0 generates compliant code for the JAX-WS 2.0 specification.</p>
<dt>-quiet</p>
<dd>Suppresses the <code>wsimport</code> command output.</dl>
<p> Multiple <code>JAX-WS</code> and <code>JAXB</code> binding files can be specified using the <code>-b</code> option, and they can be used to customize various things such as package names and bean names. More information about <code>JAX-WS</code> and <code>JAXB</code> binding files can be found in the customization documentation at <a rel="nofollow" href="https://jax-ws.dev.java.net/nonav/2.1.1/docs/customizations.html">https://jax-ws.dev.java.net/nonav/2.1.1/docs/customizations.html</a></p>
<h2>Nonstandard Options</h2>
<dl COMPACT>
<dt>-XadditionalHeaders</p>
<dd>Maps headers not bound to a request or response message to Java method parameters.</p>
<dt>-Xauthfile <i>file</i></p>
<dd>The WSDL URI that specifies the file that contains authorization information. This URI is in the following format: </p>
<p> http://<i>user-name</i>:<code>password</code>@<i>host-name</i>/<i>web-service-name</i>&gt;?wsdl.</p>
<dt>-Xdebug</p>
<dd>Prints debugging information.</p>
<dt>-Xno-addressing-databinding</p>
<dd>Enables binding of W3C EndpointReferenceType to Java.</p>
<dt>-Xnocompile</p>
<dd>Does not compile the generated Java files.</dl>
<h2>Example</h2>
<p>The following example generates the Java artifacts and compiles the artifacts by importing <code><a rel="nofollow" href="http://stockquote.example.com/quote?wsdl">http://stockquote.example.com/quote?wsdl</a></code> </p>
<pre><code>wsimport -p stockquote <a rel="nofollow" href="http://stockquote.example.com/quote?wsdl">http://stockquote.example.com/quote?wsdl</a></code></pre>
<h2>See Also</h2>
<dl COMPACT>
<dt>&bull;</p>
<dd><a href="/docs/linux/man/1-wsgen/">wsgen</a>(1)</p>
<dt>&bull;</p>
<dd>The Tools tab of Wsimport Ant Task page <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html">http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html</a></p>
<dt>&bull;</p>
<dd>The <i>Users Guide</i> tab of Catalog Support page <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/catalog-support.html">http://jax-ws.java.net/nonav/2.1.1/docs/catalog-support.html</a></p>
<dt>&bull;</p>
<dd>The <i>Users Guide</i> tab of WSDL Customization page <a rel="nofollow" href="http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html">http://jax-ws.java.net/nonav/2.1.1/docs/wsimportant.html</a> </p>
</dl>
