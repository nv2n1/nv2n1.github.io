---
title: "clk_get_accuracy(9)"
name: "clk_get_accuracy"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_get_accuracy/"
---

clk_get_accuracy - obtain the clock accuracy in ppb (parts per billion) for a clock source.

<h2>Synopsis</h2>

<pre><code>long clk_get_accuracy(struct clk *clk);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>

<h2>Description</h2>

This gets the clock source accuracy expressed in ppb. A perfect clock returns 0.

<h2>Copyright</h2>


