---
title: "teredo-mire(1)"
name: "teredo-mire"
section: "1"
letter: "t"
url: "/docs/linux/man/1-teredo-mire/"
description: "teredo-mire – Stateless Teredo IPv6 responder"
---

<h2>NAME</h2>
<p> teredo-mire &#8211; Stateless Teredo IPv6 responder</p>
<h2>SYNOPSIS</h2>
<p> <code>teredo-mire</code> </p>
<h2>DESCRIPTON</h2>
<p> <code>Teredo-Mire</code> is a test back-end for the Teredo IPv6 tunneling protocol. It listens for requests from other Teredo clients or IPv6 nodes (through Teredo relays) and answers to them statelessly. Currently only ICMPv6 Echo Requests (&quot;pings&quot;) are handled. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Display some help and exit. </p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd> Display program version and exit. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> To contact a teredo-mire responder, a valid Teredo IPv6 address must be determined for it. The server IPv4 address and mapped client IPv4 address parts should both represent the IPv4 address of the host running teredo-mire. The mapped UDP port number must be 3545. The Teredo prefix and Teredo flags are ignored. </p>
<h2>BUGS</h2>
<p> <i>teredo-mire</i> uses UDP ports 3544 and 3545, and assumes it has a public IPv4 address. </p>
<p> Neither RFC 2460 nor RFC 4380 are properly implemented. </p>
<h2>SECURITY</h2>
<p> <i>teredo-mire</i> does not require any priviledge to run. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-ping6/">ping6</a>(8), <a href="/docs/linux/man/8-miredo/">miredo</a>(8), <a href="/docs/linux/man/7-ipv6/">ipv6</a>(7) </p>
<h2>AUTHOR</h2>
<p> R33mi Denis-Courmont &lt;remi at remlab dot net&gt; </p>
<p> <a rel="nofollow" href="http://www.remlab.net/miredo/">http://www.remlab.net/miredo/</a> </p>
<h2>Index</h2>
