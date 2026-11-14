---
title: "hostip(8)"
name: "hostip"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hostip/"
description: "hostip – Resolve a host name to an IP address"
---

<p><code>hostip</code> &#8211; Resolve a host name to an IP address</p>
<h2>Synopsis</h2>
<p><code>hostip</code> [<i>options</i>] host_name</p>
<h2>Description</h2>
<p><code>hostip</code> sends a DNS query to a resolver, and prints the IP addresses for the given host name. </p>
<p> It can be useful in order to retrieve IP addresses before <a href="/docs/linux/man/8-dnscrypt-proxy/">dnscrypt-proxy</a>(8) is started.</p>
<h2>Options</h2>
<dl>
<dt>&bull;</p>
<dd><code>-6</code>, <code>&#8211;ipv6</code>: ask for AAAA records.</p>
<dt>&bull;</p>
<dd><code>-h</code>, <code>&#8211;help</code>: show usage.</p>
<dt>&bull;</p>
<dd><code>-r</code>, <code>&#8211;resolver-address=&lt;ip&gt;[:port]</code>: the resolver IP address (default: 8.8.8.8, Google DNS).</p>
<dt>&bull;</p>
<dd><code>-V</code>, <code>&#8211;version</code>: show version number.</p>
<dd></dl>
<h2>Simple Usage Example</h2>
<pre>$ hostip <a rel="nofollow" href="http://www.example.com">www.example.com</a></pre>
<h2>Advanced Usage Example</h2>
<pre>$ hostip -6 -r 4.2.2.2 <a rel="nofollow" href="http://www.google.com">www.google.com</a></pre>
<h2>Exit Status</h2>
<p>The <code>hostip</code> utility exits 0 on success, and &gt; 0 if an error occurs.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dnscrypt-proxy/">dnscrypt-proxy</a>(8) </p>
