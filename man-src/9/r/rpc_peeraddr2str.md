---
title: "rpc_peeraddr2str(9)"
name: "rpc_peeraddr2str"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_peeraddr2str/"
---

rpc_peeraddr2str - return remote peer address in printable format

<h2>Synopsis</h2>

<pre><code>const char *rpc_peeraddr2str(struct rpc_clnt *clnt, enum rpc_display_format_t format);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>RPC client structure</dl>
 

 <i>format</i>
<dl><dd>address format</dl>

<h2>Description</h2>

NB: the lifetime of the memory referenced by the returned pointer is the same as the rpc_xprt itself. As long as the caller uses this pointer, it must hold the RCU read lock.

<h2>Copyright</h2>


