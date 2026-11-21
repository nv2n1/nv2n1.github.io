---

title: "disco(1)"
name: "disco"
section: "1"
letter: "d"
url: "/docs/linux/man/1-disco/"
description: "disco – Mono’s Web Service Discovery Tool"
---

<h2>NAME</h2>
<p> disco &#8211; Mono&#8217;s Web Service Discovery Tool</p>
<p> <code>disco</code> [options] url</p>
<p> <i>disco</i> is a tool for discovering web services and for retireving the documents that describe those services. </p>
<p> <i>url</i> is the location of a DISCO document, which includes a list of WSDL documents, XML schemas and references to other DISCO documents. </p>
<p> <i>disco</i> downloads the DISCO document and all referenced documents (unless the <i>-nosave</i> option is specified), and saves them to disk.</p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><i>-nologo</i></dt>
<dd> Supress the startup logo.</dd>
<dt><i>-nosave</i></dt>
<dd> Do not save the discovered documents to disk. The default is to save the documents.</dd>
<dt><i>-o:directory, -out:directory</i></dt>
<dd> The directory where to save the discovered documents. By default, documents are saved in the current directory.</dd>
<dt><i>-u:username, -user:username</i></dt>
<dd> The user name to use when connecting to the server.</dd>
<dt><i>-p:password, -password:password</i></dt>
<dd> The password to use when connecting to the server.</dd>
<dt><i>-d:domain, -domain:domain</i></dt>
<dd> The domain to use when connecting to the server.</dd>
<dt><i>-proxy:url</i></dt>
<dd> The url of the proxy server to use for http requests.</dd>
<dt><i>-proxyusername:username</i></dt>
<dd> The user name to use when connecting to the proxy.</dd>
<dt><i>-proxypassword:password</i></dt>
<dd> The password to use when connecting to the proxy.</dd>
<dt><i>-proxydomain:domain</i></dt>
<dd> The domain to use when connecting to the proxy.</dd></dl>
<h2>AUTHORS</h2>
<p> Lluis Sanchez Gual (lluis [at] ximian.com) </p>
<h2>LICENSE</h2>
<p> disco is released under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-wsdl/">wsdl</a>(1), <a href="/docs/linux/man/1-soapsuds/">soapsuds</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1) </p>
