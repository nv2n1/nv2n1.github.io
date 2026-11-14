---
title: "clk_unprepare(9)"
name: "clk_unprepare"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_unprepare/"
---

clk_unprepare - undo preparation of a clock source

<h2>Synopsis</h2>

<pre><code>void clk_unprepare(struct clk *clk);</code></pre>

<h2>Arguments</h2>

<i>clk</i>
<dl><dd><dd>clock source</dl>

<h2>Description</h2>

This undoes a previously prepared clock. The caller must balance the number of prepare and unprepare calls. 

 Must not be called from within atomic context.

<h2>Copyright</h2>


