---
title: "xprt_adjust_cwnd(9)"
name: "xprt_adjust_cwnd"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_adjust_cwnd/"
---

xprt_adjust_cwnd - adjust transport congestion window

<h2>Synopsis</h2>

<pre><code>void xprt_adjust_cwnd(struct rpc_xprt *xprt, struct rpc_task *task, int result);</code></pre>

<h2>Arguments</h2>

<i>xprt</i>
<dl><dd><dd>pointer to xprt</dl>
 

 <i>task</i>
<dl><dd>recently completed RPC request used to adjust window</dl>
 

 <i>result</i>
<dl><dd>result code of completed RPC request</dl>

<h2>Description</h2>

The transport code maintains an estimate on the maximum number of out- standing RPC requests, using a smoothed version of the congestion avoidance implemented in 44BSD. This is basically the Van Jacobson congestion algorithm: If a retransmit occurs, the congestion window is halved; otherwise, it is incremented by 1/cwnd when 

 - a reply is received and - a full number of requests are outstanding and - the congestion window hasn't been updated recently.

<h2>Copyright</h2>


