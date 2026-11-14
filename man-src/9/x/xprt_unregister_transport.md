---
title: "xprt_unregister_transport(9)"
name: "xprt_unregister_transport"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_unregister_transport/"
---

xprt_unregister_transport - unregister a transport implementation

<h2>Synopsis</h2>

<pre><code>int xprt_unregister_transport(struct xprt_class *transport);</code></pre>

<h2>Arguments</h2>

<i>transport</i>
<dl><dd><dd>transport to unregister</dl>

<h2>Return</h2>

0: transport successfully unregistered -ENOENT: transport never registered

<h2>Copyright</h2>


