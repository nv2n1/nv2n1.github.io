---
title: "rpc_clnt_add_xprt(9)"
name: "rpc_clnt_add_xprt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_clnt_add_xprt/"
---

rpc_clnt_add_xprt - Add a new transport to a rpc_clnt

<h2>Synopsis</h2>

<pre><code>int rpc_clnt_add_xprt(struct rpc_clnt *clnt, struct xprt_create *xprtargs, int (*setup)(struct rpc_clnt *, struct rpc_xprt_switch *, struct rpc_xprt *, void *), void *data);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>pointer to struct rpc_clnt</dl>
 

 <i>xprtargs</i>
<dl><dd>pointer to struct xprt_create</dl>
 

 <i>setup</i>
<dl><dd>callback to test and/or set up the connection</dl>
 

 <i>data</i>
<dl><dd>pointer to setup function data</dl>

<h2>Description</h2>

Creates a new transport using the parameters set in args and adds it to clnt. If ping is set, then test that connectivity succeeds before adding the new transport.

<h2>Copyright</h2>


