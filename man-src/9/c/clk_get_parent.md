---
title: "clk_get_parent(9)"
name: "clk_get_parent"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_get_parent/"
description: "clk_get_parent – get the parent clock source for this clock"
---

<p>clk_get_parent &#8211; get the parent clock source for this clock</p>
<h2>Synopsis</h2>
<pre><code>struct clk *clk_get_parent(struct clk *clk);</code></pre>
<h2>Arguments</h2>
<p><i>clk</i></p>
<dl>
<dd>
<dd>clock source</dl>
<h2>Description</h2>
<p>Returns struct clk corresponding to parent clock source, or valid <code>IS_ERR</code> condition containing errno.</p>
<h2>Copyright</h2>
