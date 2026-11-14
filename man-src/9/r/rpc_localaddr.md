---
title: "rpc_localaddr(9)"
name: "rpc_localaddr"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_localaddr/"
---

rpc_localaddr - discover local endpoint address for an RPC client

<h2>Synopsis</h2>

<pre><code>int rpc_localaddr(struct rpc_clnt *clnt, struct sockaddr *buf, size_t buflen);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>RPC client structure</dl>
 

 <i>buf</i>
<dl><dd>target buffer</dl>
 

 <i>buflen</i>
<dl><dd>size of target buffer, in bytes</dl>

<h2>Description</h2>

Returns zero and fills in "buf" and "buflen" if successful; otherwise, a negative errno is returned. 

 This works even if the underlying transport is not currently connected, or if the upper layer never previously provided a source address. 

 The result of this function call is transient: multiple calls in succession may give different results, depending on how local networking configuration changes over time.

<h2>Copyright</h2>


