---
title: "rpc_bind_new_program(9)"
name: "rpc_bind_new_program"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_bind_new_program/"
---

rpc_bind_new_program - bind a new RPC program to an existing client

<h2>Synopsis</h2>

<pre><code>struct rpc_clnt *rpc_bind_new_program(struct rpc_clnt *old, const struct rpc_program *program, u32 vers);</code></pre>

<h2>Arguments</h2>

<i>old</i>
<dl><dd><dd>old rpc_client</dl>
 

 <i>program</i>
<dl><dd>rpc program to set</dl>
 

 <i>vers</i>
<dl><dd>rpc program version</dl>

<h2>Description</h2>

Clones the rpc client and sets up a new RPC program. This is mainly of use for enabling different RPC programs to share the same transport. The Sun NFSv2/v3 ACL protocol can do this.

<h2>Copyright</h2>


