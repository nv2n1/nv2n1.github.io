---
title: "synchronize_net(9)"
name: "synchronize_net"
section: "9"
letter: "s"
url: "/docs/linux/man/9-synchronize_net/"
---

synchronize_net - Synchronize with packet receive processing

<h2>Synopsis</h2>

<pre><code>void synchronize_net(void);</code></pre>

<h2>Arguments</h2>

<i>void</i>
<dl><dd><dd>no arguments</dl>

<h2>Description</h2>

Wait for packets currently being received to be done. Does not block later packets from starting.

<h2>Copyright</h2>


