---
title: "clk_prepare(9)"
name: "clk_prepare"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_prepare/"
---

clk_prepare - prepare a clock source

<h2>Synopsis</h2>

<pre><code>int clk_prepare(struct clk *clk);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>

<h2>Description</h2>

This prepares the clock source for use. 

 Must not be called from within atomic context.

<h2>Copyright</h2>


