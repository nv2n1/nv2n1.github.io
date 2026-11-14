---
title: "rpc_count_iostats_metrics(9)"
name: "rpc_count_iostats_metrics"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_count_iostats_metrics/"
---

rpc_count_iostats_metrics - tally up per-task stats

<h2>Synopsis</h2>

<pre><code>void rpc_count_iostats_metrics(const struct rpc_task *task, struct rpc_iostats *op_metrics);</code></pre>

<h2>Arguments</h2>

<i>task</i>
<dl><dd><dd>completed rpc_task</dl>
 

 <i>op_metrics</i>
<dl><dd>stat structure for OP that will accumulate stats from <i>task</i></dl>

<h2>Copyright</h2>


