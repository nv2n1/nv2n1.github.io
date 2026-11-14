---
title: "rpc_count_iostats(9)"
name: "rpc_count_iostats"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_count_iostats/"
---

rpc_count_iostats - tally up per-task stats

<h2>Synopsis</h2>

<pre><code>void rpc_count_iostats(const struct rpc_task *task, struct rpc_iostats *stats);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>completed rpc_task</dl>
 

 <i>stats</i>
<dl><dd>array of stat structures</dl>

<h2>Description</h2>

Uses the statidx from <i>task</i>

<h2>Copyright</h2>


