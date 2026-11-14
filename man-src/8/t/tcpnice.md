---
title: "tcpnice(8)"
name: "tcpnice"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpnice/"
description: "tcpnice – slow down TCP connections on a LAN"
---

<p>tcpnice &#8211; slow down TCP connections on a LAN</p>
<h2>Synopsis</h2>
<p><code>tcpnice</code> [<code>-A</code>] [<code>-I</code>] [<code>-M</code>] [<code>-i </code><i>interface</i>] <i>expression</i></p>
<h2>Description</h2>
<p><code>tcpnice</code> slows down specified TCP connections on a LAN via &quot;active&quot; traffic shaping.</p>
<h2>Options</h2>
<dl>
<dt><code>-A</code></p>
<dd>Inject TCP tiny window advertisements.</p>
<dt><code>-I</code></p>
<dd>Inject ICMP source quench replies.</p>
<dt><code>-M</code></p>
<dd>Inject ICMP fragmentation-needed replies with tiny next-hop MTUs.</p>
<dt><code>-i </code><i>interface</i></p>
<dd>Specify the interface to listen on.</p>
<dt><i>expression</i></p>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select the connections to slow down.</dl>
<p> If no attack type is given, all attacks will be enabled.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-tcpkill/">tcpkill</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
