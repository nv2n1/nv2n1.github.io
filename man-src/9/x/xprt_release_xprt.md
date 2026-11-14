---
title: "xprt_release_xprt(9)"
name: "xprt_release_xprt"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_release_xprt/"
---

xprt_release_xprt - allow other requests to use a transport

<h2>Synopsis</h2>

<pre><code>void xprt_release_xprt(struct rpc_xprt *xprt, struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>xprt</i>
<dl><dd><dd>transport with other tasks potentially waiting</dl>
 

 <i>task</i>
<dl><dd>task that is releasing access to the transport</dl>

<h2>Description</h2>

Note that "task" can be NULL. No congestion control is provided.

<h2>Copyright</h2>


