---
title: "gen_replace_estimator(9)"
name: "gen_replace_estimator"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gen_replace_estimator/"
description: "gen_replace_estimator – replace rate estimator configuration"
---

<p>gen_replace_estimator &#8211; replace rate estimator configuration</p>
<h2>Synopsis</h2>
<pre><code>int gen_replace_estimator(struct gnet_stats_basic_packed *bstats, struct gnet_stats_basic_cpu __percpu *cpu_bstats, struct gnet_stats_rate_est64 *rate_est, spinlock_t *stats_lock, seqcount_t *running, struct nlattr *opt);</code></pre>
<h2>Arguments</h2>
<p><i>bstats</i></p>
<dl>
<dd>
<dd>basic statistics</dl>
<p> <i>cpu_bstats</i></p>
<dl>
<dd>bstats per cpu</dl>
<p> <i>rate_est</i></p>
<dl>
<dd>rate estimator statistics</dl>
<p> <i>stats_lock</i></p>
<dl>
<dd>statistics lock</dl>
<p> <i>running</i></p>
<dl>
<dd>qdisc running seqcount (might be NULL)</dl>
<p> <i>opt</i></p>
<dl>
<dd>rate estimator configuration TLV</dl>
<h2>Description</h2>
<p>Replaces the configuration of a rate estimator by calling <code>gen_kill_estimator</code> and <code>gen_new_estimator</code>. </p>
<p> Returns 0 on success or a negative error code.</p>
<h2>Copyright</h2>
