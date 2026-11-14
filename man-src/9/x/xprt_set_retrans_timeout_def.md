---
title: "xprt_set_retrans_timeout_def(9)"
name: "xprt_set_retrans_timeout_def"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_set_retrans_timeout_def/"
---

xprt_set_retrans_timeout_def - set a request's retransmit timeout

<h2>Synopsis</h2>

<pre><code>void xprt_set_retrans_timeout_def(struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>task whose timeout is to be set</dl>

<h2>Description</h2>

Set a request's retransmit timeout based on the transport's default timeout parameters. Used by transports that don't adjust the retransmit timeout based on round-trip time estimation.

<h2>Copyright</h2>


