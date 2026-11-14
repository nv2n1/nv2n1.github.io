---
title: "clk_set_parent(9)"
name: "clk_set_parent"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_set_parent/"
---

clk_set_parent - set the parent clock source for this clock

<h2>Synopsis</h2>

<pre><code>int clk_set_parent(struct clk *clk, struct clk *parent);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>
 

 <i>parent</i>
<dl><dd>parent clock source</dl>

<h2>Description</h2>

Returns success (0) or negative errno.

<h2>Copyright</h2>


