---
title: "xprt_set_retrans_timeout_rtt(9)"
name: "xprt_set_retrans_timeout_rtt"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_set_retrans_timeout_rtt/"
---

xprt_set_retrans_timeout_rtt - set a request's retransmit timeout

<h2>Synopsis</h2>

<pre><code>void xprt_set_retrans_timeout_rtt(struct rpc_task *task);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>task whose timeout is to be set</dl>

<h2>Description</h2>

Set a request's retransmit timeout using the RTT estimator.

<h2>Copyright</h2>


