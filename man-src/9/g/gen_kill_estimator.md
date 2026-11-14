---
title: "gen_kill_estimator(9)"
name: "gen_kill_estimator"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gen_kill_estimator/"
---

gen_kill_estimator - remove a rate estimator

<h2>Synopsis</h2>

<pre><code>void gen_kill_estimator(struct gnet_stats_basic_packed *bstats, struct gnet_stats_rate_est64 *rate_est);</code></pre>

<h2>Arguments</h2>

<i>bstats</i>
<dl><dd><dd>basic statistics</dl>
 

 <i>rate_est</i>
<dl><dd>rate estimator statistics</dl>

<h2>Description</h2>

Removes the rate estimator specified by bstats and rate_est.

<h2>Note</h2>

Caller should respect an RCU grace period before freeing stats_lock

<h2>Copyright</h2>


