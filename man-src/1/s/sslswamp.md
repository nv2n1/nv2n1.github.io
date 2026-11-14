---
title: "sslswamp(1)"
name: "sslswamp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sslswamp/"
description: "swamp – SSL/TLS load-tester based on OpenSSL"
---

<h2>NAME</h2>
<p> swamp &#8211; SSL/TLS load-tester based on OpenSSL</p>
<h2>SYNOPSIS</h2>
<p> <code>swamp</code> -connect &lt;address&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>swamp</code> is a utility that can be used to test and/or benchmark <font SIZE="-1">SSL/TLS</font> servers. It is quite configurable and allows for various different characteristics of the server&#8217;s behaviour to be tested.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-connect</code> address</p>
<dd> Configures the address to which <code>swamp</code> should connect for outgoing connections, using the syntax defined by the <i>libnal</i> <font SIZE="-1">API</font>. For connecting to <font SIZE="-1">TCP/IP</font> addresses, the syntax is illustrated below (you may use an explicit <font SIZE="-1">IP</font> address or a host name); </p>
<pre>
    # swamp -connect IP:192.168.0.1:443
    # swamp -connect IP:<a rel="nofollow" href="http://www.localnet">www.localnet</a>:443
</pre>
<p> To connect to an <font SIZE="-1">SSL/TLS</font> server on a unix domain socket, the syntax is; </p>
<pre>
    # swamp -connect UNIX:/path/to/some/socket
</pre>
<dt><code>-h</code>, <code>-help</code>, <code>-?</code></p>
<dd> Any of these flags will cause <code>swamp</code> to display a brief usage summary to the console and exit cleanly. Any other flags are ignored.</dl>
<h2>BUGS</h2>
<p> This man page is utterly incomplete.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a href="/docs/linux/man/2-nal_address_new/">NAL_ADDRESS_new</a></i>(2)</p>
<dd> Information on the <i>libnal</i> network abstraction library used by swamp. This provides some information about the syntax used for <code>-connect</code>.</p>
<dt><i><a href="/docs/linux/man/8-distcache/">distcache</a></i>(8)</p>
<dd> Overview of the distcache architecture, of which swamp is a component.</p>
<dt><i><a rel="nofollow" href="http://www.distcache.org/">http://www.distcache.org/</a></i></p>
<dd> Distcache home page.</dl>
<h2>AUTHOR</h2>
<p> Swamp was designed and implemented by Geoff Thorpe. Steve Robb has contributed numerous tweaks and fixes along the way too. To consolidate resources and provide an improved framework for ongoing development, the swamp utility was made a component of the distcache project in 2003 (swamp happens to be the ideal tool for testing distcache&#8217;s most common usage &#8211; secure web servers). </p>
<p> Home Page: <i><a rel="nofollow" href="http://www.distcache.org">http://www.distcache.org</a></i> </p>
<h2>Index</h2>
