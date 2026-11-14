---
title: "xprt_load_transport(9)"
name: "xprt_load_transport"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_load_transport/"
---

xprt_load_transport - load a transport implementation

<h2>Synopsis</h2>

<pre><code>int xprt_load_transport(const char *transport_name);</code></pre>

<h2>Arguments</h2>

<i>transport_name</i>
<dl><dd><dd>transport to load</dl>

<h2>Return</h2>

0: transport successfully loaded -ENOENT: transport module not available

<h2>Copyright</h2>


