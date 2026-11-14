---
title: "xprt_release_rqst_cong(9)"
name: "xprt_release_rqst_cong"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_release_rqst_cong/"
---

xprt_release_rqst_cong - housekeeping when request is complete

<h2>Synopsis</h2>

<pre><code>void xprt_release_rqst_cong(struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>RPC request that recently completed</dl>

<h2>Description</h2>

Useful for transports that require congestion control.

<h2>Copyright</h2>


