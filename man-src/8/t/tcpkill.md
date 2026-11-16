---
title: "tcpkill(8)"
name: "tcpkill"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tcpkill/"
description: "tcpkill – kill TCP connections on a LAN"
---

<p>tcpkill &#8211; kill TCP connections on a LAN</p>
<h2>Synopsis</h2>
<p><code>tcpkill</code> [<code>-i </code><i>interface</i>] [<code>-1</code>&#8230;<code>9</code>] <i>expression</i></p>
<h2>Description</h2>
<p><code>tcpkill</code> kills specified in-progress TCP connections (useful for libnids-based applications which require a full TCP 3-whs for TCB creation).</p>
<h2>Options</h2>
<dl>
<dt><code>-i </code><i>interface</i></dt>
<dd>Specify the interface to listen on.</dd>
<dt><code>-1</code>&#8230;<code>9</code></dt>
<dd>Specify the degree of brute force to use in killing a connection. Fast connections may require a higher number in order to land a RST in the moving receive window. Default is 3.</dd>
<dt><i>expression</i></dt>
<dd>Specify a <a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8) filter expression to select the connections to kill.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dsniff/">dsniff</a>(8), <a href="/docs/linux/man/8-tcpnice/">tcpnice</a>(8)</p>
<h2>Author</h2>
<pre>Dug Song &lt;dugsong [at] monkey.org&gt;</pre>
