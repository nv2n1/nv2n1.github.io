---
title: "xprt_reserve_xprt(9)"
name: "xprt_reserve_xprt"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_reserve_xprt/"
---

xprt_reserve_xprt - serialize write access to transports

<h2>Synopsis</h2>

<pre><code>int xprt_reserve_xprt(struct rpc_xprt *xprt, struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>xprt</i>
<dl><dd><dd>pointer to the target transport</dl>
 

 <i>task</i>
<dl><dd>task that is requesting access to the transport</dl>

<h2>Description</h2>

This prevents mixing the payload of separate requests, and prevents transport connects from colliding with writes. No congestion control is provided.

<h2>Copyright</h2>


