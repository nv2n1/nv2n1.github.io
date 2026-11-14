---
title: "rpc_clone_client(9)"
name: "rpc_clone_client"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_clone_client/"
---

rpc_clone_client - Clone an RPC client structure

<h2>Synopsis</h2>

<pre><code>struct rpc_clnt *rpc_clone_client(struct rpc_clnt *clnt);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>RPC client whose parameters are copied</dl>

<h2>Description</h2>

Returns a fresh RPC client or an ERR_PTR.

<h2>Copyright</h2>


