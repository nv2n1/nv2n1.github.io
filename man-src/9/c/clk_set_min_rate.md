---
title: "clk_set_min_rate(9)"
name: "clk_set_min_rate"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_set_min_rate/"
---

clk_set_min_rate - set a minimum clock rate for a clock source

<h2>Synopsis</h2>

<pre><code>int clk_set_min_rate(struct clk *clk, unsigned long rate);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>
 

 <i>rate</i>
<dl><dd>desired minimum clock rate in Hz, inclusive</dl>

<h2>Description</h2>

Returns success (0) or negative errno.

<h2>Copyright</h2>


