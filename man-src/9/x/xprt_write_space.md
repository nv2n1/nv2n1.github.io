---
title: "xprt_write_space(9)"
name: "xprt_write_space"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_write_space/"
---

xprt_write_space - wake the task waiting for transport output buffer space

<h2>Synopsis</h2>

<pre><code>void xprt_write_space(struct rpc_xprt *xprt);</code></pre>

<h2>Arguments</h2>

<i>xprt</i>
<dl><dd><dd>transport with waiting tasks</dl>

<h2>Description</h2>

Can be called in a soft IRQ context, so xprt_write_space never sleeps.

<h2>Copyright</h2>


