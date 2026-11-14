---
title: "xprt_complete_rqst(9)"
name: "xprt_complete_rqst"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_complete_rqst/"
---

xprt_complete_rqst - called when reply processing is complete

<h2>Synopsis</h2>

<pre><code>void xprt_complete_rqst(struct rpc_task *task, int copied);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>RPC request that recently completed</dl>
 

 <i>copied</i>
<dl><dd>actual number of bytes received from the transport</dl>

<h2>Description</h2>

Caller holds transport lock.

<h2>Copyright</h2>


