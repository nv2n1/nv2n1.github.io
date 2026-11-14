---
title: "rpcb_getport_async(9)"
name: "rpcb_getport_async"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpcb_getport_async/"
---

rpcb_getport_async - obtain the port for a given RPC service on a given host

<h2>Synopsis</h2>

<pre><code>void rpcb_getport_async(struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>task that is waiting for portmapper request</dl>

<h2>Description</h2>

This one can be called for an ongoing RPC request, and can be used in an async (rpciod) context.

<h2>Copyright</h2>


