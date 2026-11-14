---
title: "xprt_lookup_rqst(9)"
name: "xprt_lookup_rqst"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_lookup_rqst/"
---

xprt_lookup_rqst - find an RPC request corresponding to an XID

<h2>Synopsis</h2>

<pre><code>struct rpc_rqst *xprt_lookup_rqst(struct rpc_xprt *xprt, __be32 xid);</code></pre>

<h2>Arguments</h2>

<i>xprt</i>
<dl><dd><dd>transport on which the original request was transmitted</dl>
 

 <i>xid</i>
<dl><dd>RPC XID of incoming reply</dl>

<h2>Copyright</h2>


