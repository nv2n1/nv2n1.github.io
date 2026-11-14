---
title: "rpc_call_sync(9)"
name: "rpc_call_sync"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_call_sync/"
---

rpc_call_sync - Perform a synchronous RPC call

<h2>Synopsis</h2>

<pre><code>int rpc_call_sync(struct rpc_clnt *clnt, const struct rpc_message *msg, int flags);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>pointer to RPC client</dl>
 

 <i>msg</i>
<dl><dd>RPC call parameters</dl>
 

 <i>flags</i>
<dl><dd>RPC call flags</dl>

<h2>Copyright</h2>


