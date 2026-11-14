---
title: "rpc_peeraddr(9)"
name: "rpc_peeraddr"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_peeraddr/"
---

rpc_peeraddr - extract remote peer address from clnt's xprt

<h2>Synopsis</h2>

<pre><code>size_t rpc_peeraddr(struct rpc_clnt *clnt, struct sockaddr *buf, size_t bufsize);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>RPC client structure</dl>
 

 <i>buf</i>
<dl><dd>target buffer</dl>
 

 <i>bufsize</i>
<dl><dd>length of target buffer</dl>

<h2>Description</h2>

Returns the number of bytes that are actually in the stored address.

<h2>Copyright</h2>


