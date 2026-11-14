---
title: "rpc_call_async(9)"
name: "rpc_call_async"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_call_async/"
---

rpc_call_async - Perform an asynchronous RPC call

<h2>Synopsis</h2>

<pre><code>int rpc_call_async(struct rpc_clnt *clnt, const struct rpc_message *msg, int flags, const struct rpc_call_ops *tk_ops, void *data);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>pointer to RPC client</dl>
 

 <i>msg</i>
<dl><dd>RPC call parameters</dl>
 

 <i>flags</i>
<dl><dd>RPC call flags</dl>
 

 <i>tk_ops</i>
<dl><dd>RPC call ops</dl>
 

 <i>data</i>
<dl><dd>user call data</dl>

<h2>Copyright</h2>


