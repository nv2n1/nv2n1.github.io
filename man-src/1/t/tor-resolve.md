---
title: "tor-resolve(1)"
name: "tor-resolve"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tor-resolve/"
description: "tor-resolve – resolve a hostname to an IP address via tor"
---

<h2 class="name">NAME</h2>
<p> tor-resolve &#8211; resolve a hostname to an IP address via tor </p>
<h2>SYNOPSIS</h2>
<p> <code>tor-resolve</code> [-4|-5] [-v] [-x] [-p <i>socksport</i>] <i>hostname</i> [<i>sockshost</i>[:<i>socksport</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>tor-resolve</code> is a simple script to connect to a SOCKS proxy that knows about the SOCKS RESOLVE command, hand it a hostname, and return an IP address. </p>
<p> By default, <code>tor-resolve</code> uses the Tor server running on 127.0.0.1 on SOCKS port 9050. If this isn&#8217;t what you want, you should specify an explicit <i>sockshost</i> and/or <i>socksport</i> on the command line.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code></p>
<dl>
<dt>
</dt><dd> Display verbose output.</dd></dl>
<p> <code>-x</code></p>
<dl>
<dt>
</dt><dd> Perform a reverse lookup: get the PTR record for an IPv4 address.</dd></dl>
<p> <code>-5</code></p>
<dl>
<dt>
</dt><dd> Use the SOCKS5 protocol. (Default)</dd></dl>
<p> <code>-4</code></p>
<dl>
<dt>
</dt><dd> Use the SOCKS4a protocol rather than the default SOCKS5 protocol. Doesn&#8217;t support reverse DNS.</dd></dl>
<p> <code>-p</code> <i>socksport</i></p>
<dl>
<dt>
</dt><dd> Override the default SOCKS port without setting the hostname.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tor/">tor</a></code>(1), <code><a href="/docs/linux/man/1-torify/">torify</a></code>(1). </p>
<p> See doc/socks-extensions.txt in the Tor package for protocol details.</p>
<h2>AUTHORS</h2>
<p> Roger Dingledine &lt;arma [at] mit.edu&gt;, Nick Mathewson &lt;nickm [at] alum.mit.edu&gt;.</p>
<h2>AUTHOR</h2>
<p> <code>Peter Palfrader</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
