---
title: "gen_new_estimator(9)"
name: "gen_new_estimator"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gen_new_estimator/"
---

gen_new_estimator - create a new rate estimator

<h2>Synopsis</h2>

<pre><code>int gen_new_estimator(struct gnet_stats_basic_packed *bstats, struct gnet_stats_basic_cpu __percpu *cpu_bstats, struct gnet_stats_rate_est64 *rate_est, spinlock_t *stats_lock, seqcount_t *running, struct nlattr *opt);</code></pre>

<h2>Arguments</h2>

<i>bstats</i>
<dl><dd><dd>basic statistics</dl>
 

 <i>cpu_bstats</i>
<dl><dd>bstats per cpu</dl>
 

 <i>rate_est</i>
<dl><dd>rate estimator statistics</dl>
 

 <i>stats_lock</i>
<dl><dd>statistics lock</dl>
 

 <i>running</i>
<dl><dd>qdisc running seqcount</dl>
 

 <i>opt</i>
<dl><dd>rate estimator configuration TLV</dl>

<h2>Description</h2>

Creates a new rate estimator with bstats as source and rate_est as destination. A new timer with the interval specified in the configuration TLV is created. Upon each interval, the latest statistics will be read from bstats and the estimated rate will be stored in rate_est with the statistics lock grabbed during this period. 

 Returns 0 on success or a negative error code.

<h2>Copyright</h2>


