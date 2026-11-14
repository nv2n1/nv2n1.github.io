---
title: "httpcfg(1)"
name: "httpcfg"
section: "1"
letter: "h"
url: "/docs/linux/man/1-httpcfg/"
description: "httpcfg – Mono Certificate Management for HttpListener"
---

<h2>NAME</h2>
<p> httpcfg &#8211; Mono Certificate Management for HttpListener</p>
<h2>SYNOPSIS</h2>
<p> <code>httpcfg [options] certificate</code></p>
<h2>DESCRIPTION</h2>
<p> This tool is used to manage the certificates used by the HttpListener embeddable server class when the HttpListener is configured as an HTTPS server instead of an HTTP server. </p>
<p> You must select one of the possible actions: add, delete or list. </p>
<p> When adding a certificate (-add), you must provide the following information: a certificate (with the -cert flag) a Private Key file (with the -pvk argument, the filename is typically &quot;key&quot;) and a port number (with the -port flag). </p>
<p> When deleting a certificate (-del or -delete) you need to provide the port number.</p>
<h2>PARAMETERS</h2>
<dl>
<dt><i>-add</i></p>
<dd> Adds a new certificate/private key combination for being used at a given port by the HttpListener API.</p>
<dt><i>-del, -delete</i></p>
<dd> Deletes the certificates associated for the port specified (must be specified separatedly).</p>
<dt><i>-list</i></p>
<dd> List all known certificates.</p>
<dt><i>-port PORT</i></p>
<dd> Specifies the port to add certificates to, or remove certificates from.</p>
<dt><i>-pvk FILE</i></p>
<dd> Specifies the Private Key file.</p>
<dt><i>-cert CERT</i></p>
<dd> Specifies the certificate file to use.</dl>
<h2>EXAMPLES</h2>
<pre>
httpcfg -add -port 8081 -pvk myfile.pvk -cert MyCert
</pre>
<p> For more details on creating the certificate file and the private key, see the following web page: </p>
<p> <a rel="nofollow" href="http://www.mono-project.com/docs/web/using-clientcertificates-with-xsp/">http://www.mono-project.com/docs/web/using-clientcertificates-with-xsp/</a></p>
<h2>FILES</h2>
<p> The certificates are stored in the ~/.mono/httplistener directory</p>
<h2>AUTHOR</h2>
<p> <code>httpcfg</code> was written by Gonzalo Paniagua.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006 Novell.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-makecert/">makecert</a>(1), <a href="/docs/linux/man/1-signcode/">signcode</a>(1), <a href="/docs/linux/man/1-cert2spc/">cert2spc</a>(1)</code> </p>
<p> The private key format: </p>
<pre>
<a rel="nofollow" href="http://www.drh-consultancy.demon.co.uk/pvk.html">http://www.drh-consultancy.demon.co.uk/pvk.html</a>
</pre>
<h2>Index</h2>
