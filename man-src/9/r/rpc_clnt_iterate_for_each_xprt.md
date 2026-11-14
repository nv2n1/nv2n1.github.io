---
title: "rpc_clnt_iterate_for_each_xprt(9)"
name: "rpc_clnt_iterate_for_each_xprt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_clnt_iterate_for_each_xprt/"
---

rpc_clnt_iterate_for_each_xprt - Apply a function to all transports

<h2>Synopsis</h2>

<pre><code>int rpc_clnt_iterate_for_each_xprt(struct rpc_clnt *clnt, int (*fn)(struct rpc_clnt *, struct rpc_xprt *, void *), void *data);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>pointer to client</dl>
 

 <i>fn</i>
<dl><dd>function to apply</dl>
 

 <i>data</i>
<dl><dd>void pointer to function data</dl>

<h2>Description</h2>

Iterates through the list of RPC transports currently attached to the client and applies the function fn(clnt, xprt, data). 

 On error, the iteration stops, and the function returns the error value.

<h2>Copyright</h2>


