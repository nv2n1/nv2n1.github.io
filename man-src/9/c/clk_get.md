---
title: "clk_get(9)"
name: "clk_get"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clk_get/"
description: "clk_get – lookup and obtain a reference to a clock producer."
---

<p>clk_get &#8211; lookup and obtain a reference to a clock producer.</p>
<h2>Synopsis</h2>
<pre><code>struct clk *clk_get(struct device *dev, const char *id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device for clock &#8220;consumer&#8221;</dl>
<p> <i>id</i></p>
<dl>
<dd>clock consumer ID</dl>
<h2>Description</h2>
<p>Returns a struct clk corresponding to the clock producer, or valid <code>IS_ERR</code> condition containing errno. The implementation uses <i>dev</i> and <i>id</i> to determine the clock consumer, and thereby the clock producer. (IOW, <i>id</i> may be identical strings, but clk_get may return different clock producers depending on <i>dev</i>.) </p>
<p> Drivers must assume that the clock source is not enabled. </p>
<p> clk_get should not be called from within interrupt context.</p>
<h2>Copyright</h2>
