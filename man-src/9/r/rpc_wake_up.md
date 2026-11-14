---
title: "rpc_wake_up(9)"
name: "rpc_wake_up"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_wake_up/"
---

rpc_wake_up - wake up all rpc_tasks

<h2>Synopsis</h2>

<pre><code>void rpc_wake_up(struct rpc_wait_queue *queue);</code></pre>

<h2>Arguments</h2>

<i>queue</i>
<dl><dd><dd>rpc_wait_queue on which the tasks are sleeping</dl>

<h2>Description</h2>

Grabs queue-&gt;lock

<h2>Copyright</h2>


