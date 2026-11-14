---
title: "clk_put(9)"
name: "clk_put"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_put/"
---

clk_put - &quot;free&quot; the clock source

<h2>Synopsis</h2>

<pre><code>void clk_put(struct clk *clk);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>

<h2>Note</h2>

drivers must ensure that all clk_enable calls made on this clock source are balanced by clk_disable calls prior to calling this function. 

 clk_put should not be called from within interrupt context.

<h2>Copyright</h2>


