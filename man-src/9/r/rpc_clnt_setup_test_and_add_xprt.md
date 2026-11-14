---
title: "rpc_clnt_setup_test_and_add_xprt(9)"
name: "rpc_clnt_setup_test_and_add_xprt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_clnt_setup_test_and_add_xprt/"
description: "rpc_clnt_setup_test_and_add_xprt –"
---

<p>rpc_clnt_setup_test_and_add_xprt &#8211;</p>
<h2>Synopsis</h2>
<pre><code>int rpc_clnt_setup_test_and_add_xprt(struct rpc_clnt *clnt, struct rpc_xprt_switch *xps, struct rpc_xprt *xprt, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>clnt</i></p>
<dl>
<dd>
<dd>struct rpc_clnt to get the new transport</dl>
<p> <i>xps</i></p>
<dl>
<dd>the rpc_xprt_switch to hold the new transport</dl>
<p> <i>xprt</i></p>
<dl>
<dd>the rpc_xprt to test</dl>
<p> <i>data</i></p>
<dl>
<dd>a struct rpc_add_xprt_test pointer that holds the test function and test function call data</dl>
<h2>Description</h2>
<p>This is an rpc_clnt_add_xprt <code>setup</code> function which returns 1 so: 1) caller of the test function must dereference the rpc_xprt_switch and the rpc_xprt. 2) test function must call rpc_xprt_switch_add_xprt, usually in the rpc_call_done routine. </p>
<p> Upon success (return of 1), the test function adds the new transport to the rpc_clnt xprt switch</p>
<h2>Copyright</h2>
