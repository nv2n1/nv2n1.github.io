---
title: "wbemexec(1)"
name: "wbemexec"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wbemexec/"
description: "wbemexec – submit a CIM operation request to a CIM Server"
---

<h2>NAME</h2>
<p> wbemexec &#8211; submit a CIM operation request to a CIM Server</p>
<h2>SYNOPSIS</h2>
<p> <code>wbemexec</code> [ <code>-h</code> hostname ] [ <code>-p</code> portnumber ] [ <code>-v</code> httpversion ]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-m</code>&nbsp;<wbr>httpmethod&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-t</code>&nbsp;<wbr>timeout&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-u</code>&nbsp;<wbr>username&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-w</code>&nbsp;<wbr>password&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>-s</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;help</code>&nbsp;<wbr>]&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;version</code>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr>inputfilepath&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>wbemexec </code> command provides a command line interface to a CIM Server. The input to the command consists of a CIM request encoded in XML. The request is submitted to the CIM Server for execution. If the HTTP response from the CIM Server contains a status code of 200 (OK), the result returned to stdout is the CIM response encoded in XML. Otherwise, the result returned to stdout is the HTTP response. Some types of invalid XML requests (e.g. missing PROTOCOLVERSION attribute or missing NAME attribute) are detected by <code>wbemexec,</code> and result in an error message from <code>wbemexec.</code> Other invalid XML requests (e.g. invalid CIMVERSION attribute value or missing XML version), are detected by the CIM Server, and result in an HTTP response, containing a non-Success status code, such as 501 (Not Implemented) or 400 (Bad Request). </p>
<p> By default, the request is sent as an HTTP/1.1 request, using the HTTP M-POST method, and <code>wbemexec </code> waits 20000 milliseconds (20 seconds), then times out if a response hasn&#8217;t been received. Input is read from stdin, if no input file is specified. </p>
<p> By default, the operation is executed on the local host. <code>wbemexec</code> first attempts to connect to the CIM Server on the default port for the wbem-http service, and if that fails, another attempt is made on the default port for the wbem-https service.</p>
<h3>Options</h3>
<p> <code>wbemexec</code> recognizes the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-h</code> hostname</p>
<dd> Connect to the CIM Server on the specified host. If this option is not specified, <code>wbemexec </code> connects to the local host.</p>
<dt><code>&#8211;help</code></p>
<dd> Display command usage information.</p>
<dt><code>-m</code> httpmethod</p>
<dd> Use the specified HTTP method for the request. The method must be &quot;POST&quot; or &quot;M-POST&quot;.</p>
<dt><code>-p</code> portnumber</p>
<dd> Connect to the CIM Server on the specified port number. If this option is not specified, <code>wbemexec</code> connects to the default port for the wbem-http service, or if the <code>-s</code> option is specified, to the default port for the wbem-https service.</p>
<dt><code>-s</code></p>
<dd> Enable the use of the SSL protocol between and the CIM server. The <code>-s</code> option should be specified if the CIM Server on the specified hostname/portnumber expects clients to connect using HTTPS.</p>
<dt><code>-t</code> timeout</p>
<dd> Wait the specified number of milliseconds on sending a request, before timing out if no response has been received. The <i>timeout </i> value must be an integer value greater than 0.</p>
<dt><code>-u</code> username</p>
<dd> Connect as the specified <i>R username . </i> If <i>username </i> is not specified, the current logged in user is used for authentication. This option is ignored if neither <i>hostname </i> nor <i>portnumber </i> is specified.</p>
<dt><code>-v</code> httpversion</p>
<dd> Use the specified HTTP version for the request. The version must be &quot;1.0&quot; or &quot;1.1&quot;. The 1.0 version may not be specified if the M-POST method is specified.</p>
<dt><code>&#8211;version</code></p>
<dd> Display CIM Server version.</p>
<dt><code>-w</code> password</p>
<dd> Authenticate the connection using the specified <i>password .</i> This option is ignored if neither <i>hostname </i> nor <i>portnumber </i> is specified. WARNING: A password should not be specified on the command line on a multi-user system, since command-line options are typically world-readable for a short window of time. If the remote host requests authentication and this option is not specified, <code>wbemexec</code> will prompt for the password. (See <code>cimconfig (1)</code> for information on configuring the CIM Server.)</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> When an error occurs, an explanatory error message is written to stderr and an appropriate value is returned. The following exit values are returned:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> Success</p>
<dt><code>1</code></p>
<dd> Error</dl>
</dl>
<h2>USAGE NOTE</h2>
<p> The <code>wbemexec </code> command requires that the CIM Server is running.</p>
<h2>EXAMPLES</h2>
<p> Submit an XML request contained in the file cimrequest.xml to the CIM Server running on the local host on the default port:</p>
<dl>
<dt>
<dd> <code>wbemexec cimrequest.xml</code></dl>
<p> Submit an XML request contained in the file cimrequest.xml to the CIM Server running on the host hpserver on port 49152, using the <i>username </i> guest and <i>password </i> guest for authentication:</p>
<dl>
<dt>
<dd> <code>wbemexec -h hpserver -p 49152 -u guest -w guest cimrequest.xml</code></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cimserver/">cimserver</a>(1), <a href="/docs/linux/man/1-cimconfig/">cimconfig</a>(1).</p>
<h2>STANDARDS CONFORMANCE</h2>
<p> <code>wbemexec</code>: CIM Operations over HTTP 1.0, Representation of CIM in XML 2.0 </p>
<h2>Index</h2>
