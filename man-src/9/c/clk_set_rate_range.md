---
title: "clk_set_rate_range(9)"
name: "clk_set_rate_range"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_set_rate_range/"
---

clk_set_rate_range - set a rate range for a clock source

<h2>Synopsis</h2>

<pre><code>int clk_set_rate_range(struct clk *clk, unsigned long min, unsigned long max);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>
 

 <i>min</i>
<dl><dd>desired minimum clock rate in Hz, inclusive</dl>
 

 <i>max</i>
<dl><dd>desired maximum clock rate in Hz, inclusive</dl>

<h2>Description</h2>

Returns success (0) or negative errno.

<h2>Copyright</h2>


