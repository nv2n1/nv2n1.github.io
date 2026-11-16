---
title: "rpc_clnt_test_and_add_xprt(9)"
name: "rpc_clnt_test_and_add_xprt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_clnt_test_and_add_xprt/"
---

rpc_clnt_test_and_add_xprt - Test and add a new transport to a rpc_clnt

<h2>Synopsis</h2>

<pre><code>int rpc_clnt_test_and_add_xprt(struct rpc_clnt *clnt, struct rpc_xprt_switch *xps, struct rpc_xprt *xprt, void *dummy);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd></dd><dd>pointer to struct rpc_clnt</dd></dl>
 

 <i>xps</i>
<dl><dd>pointer to struct rpc_xprt_switch,</dd></dl>
 

 <i>xprt</i>
<dl><dd>pointer struct rpc_xprt</dd></dl>
 

 <i>dummy</i>
<dl><dd>unused</dd></dl>

<h2>Copyright</h2>


