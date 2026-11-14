---
title: "rpc_clone_client_set_auth(9)"
name: "rpc_clone_client_set_auth"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_clone_client_set_auth/"
---

rpc_clone_client_set_auth - Clone an RPC client structure and set its auth

<h2>Synopsis</h2>

<pre><code>struct rpc_clnt *rpc_clone_client_set_auth(struct rpc_clnt *clnt, rpc_authflavor_t flavor);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>RPC client whose parameters are copied</dl>
 

 <i>flavor</i>
<dl><dd>security flavor for new client</dl>

<h2>Description</h2>

Returns a fresh RPC client or an ERR_PTR.

<h2>Copyright</h2>


