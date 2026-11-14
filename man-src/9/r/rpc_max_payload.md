---
title: "rpc_max_payload(9)"
name: "rpc_max_payload"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_max_payload/"
---

rpc_max_payload - Get maximum payload size for a transport, in bytes

<h2>Synopsis</h2>

<pre><code>size_t rpc_max_payload(struct rpc_clnt *clnt);</code></pre>

<h2>Arguments</h2>

<i>clnt</i>
<dl><dd><dd>RPC client to query</dl>

<h2>Description</h2>

For stream transports, this is one RPC record fragment (see RFC 1831), as we don't support multi-record requests yet. For datagram transports, this is the size of an IP packet minus the IP, UDP, and RPC header sizes.

<h2>Copyright</h2>


