---
title: "rpc_create(9)"
name: "rpc_create"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_create/"
---

rpc_create - create an RPC client and transport with one call

<h2>Synopsis</h2>

<pre><code>struct rpc_clnt *rpc_create(struct rpc_create_args *args);</code></pre>

<h2>Arguments</h2>

<i>args</i>
<dl><dd><dd>rpc_clnt create argument structure</dl>

<h2>Description</h2>

Creates and initializes an RPC transport and an RPC client. 

 It can ping the server in order to determine if it is up, and to see if it supports this program and version. RPC_CLNT_CREATE_NOPING disables this behavior so asynchronous tasks can also use rpc_create.

<h2>Copyright</h2>


