---
title: "client(5)"
name: "client"
section: "5"
letter: "c"
url: "/docs/linux/man/5-client/"
description: "client.conf – client configuration file for cups"
---

<p>client.conf &#8211; client configuration file for cups</p>
<h2>Description</h2>
<p>The <i>client.conf</i> file configures the CUPS client and is normally located in the <i>/etc/cups</i> or <i>~/.cups</i> directory. Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character.</p>
<h2>Directives</h2>
<p>The following directives are understood by the client. Consult the on-line help for detailed descriptions:</p>
<dl>
<dt>Encryption IfRequested</p>
<dd>
<dt>Encryption Never</p>
<dd>
<dt>Encryption Required</p>
<dd>Specifies the level of encryption that is required for a particular location.</p>
<dt>GSSServiceName name</p>
<dd>Specifies the Kerberos service name that is used for authentication, typically &quot;host&quot;, &quot;http&quot;, or &quot;ipp&quot;. CUPS adds the remote hostname (&quot;name [at] server.example.com&quot;) for you. The default name is &quot;http&quot;.</p>
<dt>ServerName hostname-or-ip-address[:port]</p>
<dd>
<dt>ServerName /domain/socket</p>
<dd>Specifies the address and optionally the port to use when connecting to the server. <code>Note: Not supported on OS X 10.7 or later.</code></p>
<dt>ServerName hostname-or-ip-address[:port]/version=1.1</p>
<dd>Specifies the address and optionally the port to use when connecting to a server running CUPS 1.3.12 and earlier. <code>Note: Not supported on OS X 10.7 or later.</code></p>
<dt>User name</p>
<dd>Specifies the default user name to use for requests.</dl>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>Copyright</h2>
<p>Copyright 2007-2013 by Apple Inc.</p>
