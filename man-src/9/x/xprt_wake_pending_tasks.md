---
title: "xprt_wake_pending_tasks(9)"
name: "xprt_wake_pending_tasks"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xprt_wake_pending_tasks/"
---

xprt_wake_pending_tasks - wake all tasks on a transport's pending queue

<h2>Synopsis</h2>

<pre><code>void xprt_wake_pending_tasks(struct rpc_xprt *xprt, int status);</code></pre>

<h2>Arguments</h2>

<i>xprt</i>
<dl><dd><dd>transport with waiting tasks</dl>
 

 <i>status</i>
<dl><dd>result code to plant in each task before waking it</dl>

<h2>Copyright</h2>


