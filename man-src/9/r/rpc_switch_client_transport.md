---
title: "rpc_switch_client_transport(9)"
name: "rpc_switch_client_transport"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_switch_client_transport/"
---

rpc_switch_client_transport -

<h2>Synopsis</h2>

<pre><code>int rpc_switch_client_transport(struct rpc_clnt *clnt, struct xprt_create *args, const struct rpc_timeout *timeout);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>pointer to a struct rpc_clnt</dl>
 

 <i>args</i>
<dl><dd>pointer to the new transport arguments</dl>
 

 <i>timeout</i>
<dl><dd>pointer to the new timeout parameters</dl>

<h2>Description</h2>

This function allows the caller to switch the RPC transport for the rpc_clnt structure 'clnt' to allow it to connect to a mirrored NFS server, for instance. It assumes that the caller has ensured that there are no active RPC tasks by using some form of locking. 

 Returns zero if "clnt" is now using the new xprt. Otherwise a negative errno is returned, and "clnt" continues to use the old xprt.

<h2>Copyright</h2>


