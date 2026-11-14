---
title: "gnet_stats_copy_rate_est(9)"
name: "gnet_stats_copy_rate_est"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_copy_rate_est/"
description: "gnet_stats_copy_rate_est – copy rate estimator statistics into statistics TLV"
---

<p>gnet_stats_copy_rate_est &#8211; copy rate estimator statistics into statistics TLV</p>
<h2>Synopsis</h2>
<pre><code>int gnet_stats_copy_rate_est(struct gnet_dump *d, const struct gnet_stats_basic_packed *b, struct gnet_stats_rate_est64 *r);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>dumping handle</dl>
<p> <i>b</i></p>
<dl>
<dd>basic statistics</dl>
<p> <i>r</i></p>
<dl>
<dd>rate estimator statistics</dl>
<h2>Description</h2>
<p>Appends the rate estimator statistics to the top level TLV created by <code>gnet_stats_start_copy</code>. </p>
<p> Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.</p>
<h2>Copyright</h2>
