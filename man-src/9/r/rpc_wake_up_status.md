---
title: "rpc_wake_up_status(9)"
name: "rpc_wake_up_status"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_wake_up_status/"
---

rpc_wake_up_status - wake up all rpc_tasks and set their status value.

<h2>Synopsis</h2>

<pre><code>void rpc_wake_up_status(struct rpc_wait_queue *queue, int status);</code></pre>

<h2>Arguments</h2>

<i>queue</i>
<dl><dd><dd>rpc_wait_queue on which the tasks are sleeping</dl>
 

 <i>status</i>
<dl><dd>status value to set</dl>

<h2>Description</h2>

Grabs queue-&gt;lock

<h2>Copyright</h2>


