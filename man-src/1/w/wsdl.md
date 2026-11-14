---
title: "wsdl(1)"
name: "wsdl"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wsdl/"
description: "wsdl – Mono’s Web Service Proxy Generator"
---

<h2>NAME</h2>
<p> wsdl &#8211; Mono&#8217;s Web Service Proxy Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>wsdl</code> [options] [path | url]</p>
<h2>DESCRIPTION</h2>
<p> <i>wsdl</i> is a tool for generating proxy classes that can be used to access to web services. The tool reads a WSDL document from the provided path or url, and downloads referenced schemas or other WSDL documents if needed. </p>
<p> This tool is used to target the 1.x API, for targetting the 2.x API, please use the wsdl2 tool. </p>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><i>-appsettingurlkey:key -urlkey:key</i></p>
<dd> Specifies that the url for the services should be read from the &lt;appsettings&gt; section of the configuration file, using the provided key.</p>
<dt><i>-appsettingbaseurl:url, -baseurl:url</i></p>
<dd> Specifies a base URL for the service. The final URL will be constructed by combining this value with the URL read from the <i>-appsettingurlkey</i> option, and the <i>-type:typename, assembly</i> Generate a proxy for a compiled web service class. The URL parameter can be used to providethe location of the service. <i>location</i> attribute specified in the WSDL document.</p>
<dt><i>-language:language, -l</i></p>
<dd> Language of the code to generate. It can be CS for C# (default), Boo for Boo and VB for Visual.Basic.</p>
<dt>Alternatively you can specify a full type name for a CodeProvider, for</p>
<dd> example, you could use this to generate code for the imaginary &quot;MyLan&quot; language which has the following full type: </p>
<pre>
        wsdl myservice.wsdl -language:MyLan.MyLanCodeProvider, MyLan.CodeDom, Version=1.0.0.0, Culture=neutral, PublicKeyToken=xxyy'
</pre>
<dt><i>-namespace:name, -n:name</i></p>
<dd> The namespace of the generated classes. If none is specified, the default namespace is used.</p>
<dt><i>-out:filename, -o:filename</i></p>
<dd> The target file for generated code.</p>
<dt><i>-protocol:protocol, -p:protocol</i></p>
<dd> The protocol for which to generate code. It can be Soap (default), HttpGet or HttpPost.</p>
<dt><i>-sample:METHOD</i></p>
<dd> This will display XML request and reply of the sample invocations to that SOAP message. You can use the -protocol: option to render the message in different forms.</p>
<dt><i>-server</i></p>
<dd> Generate a server skeleton instead of a client proxy.</p>
<dt><i>-nologo</i></p>
<dd> Supress the startup logo.</p>
<dt><i>-u:username, -user:username</i></p>
<dd> The user name to use when connecting to the server.</p>
<dt><i>-p:password, -password:password</i></p>
<dd> The password to use when connecting to the server.</p>
<dt><i>-d:domain, -domain:domain</i></p>
<dd> The domain to use when connecting to the server.</dl>
<h2>AUTHORS</h2>
<p> Lluis Sanchez Gual (lluis [at] ximian.com) </p>
<h2>LICENSE</h2>
<p> wsdl is released under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-disco/">disco</a>(1), <a href="/docs/linux/man/1-soapsuds/">soapsuds</a>(1), <a href="/docs/linux/man/1-mono/">mono</a>(1), <a href="/docs/linux/man/1-mcs/">mcs</a>(1), <a href="/docs/linux/man/1-wsdl2/">wsdl2</a>(1) </p>
<h2>Index</h2>
