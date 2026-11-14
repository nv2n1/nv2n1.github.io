---
title: "clk_enable(9)"
name: "clk_enable"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_enable/"
---

clk_enable - inform the system when the clock source should be running.

<h2>Synopsis</h2>

<pre><code>int clk_enable(struct clk *clk);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>

<h2>Description</h2>

If the clock can not be enabled/disabled, this should return success. 

 May be called from atomic contexts. 

 Returns success (0) or negative errno.

<h2>Copyright</h2>


