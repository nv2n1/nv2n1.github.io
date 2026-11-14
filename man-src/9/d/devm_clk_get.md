---
title: "devm_clk_get(9)"
name: "devm_clk_get"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_clk_get/"
description: "devm_clk_get – lookup and obtain a managed reference to a clock producer."
---

<p>devm_clk_get &#8211; lookup and obtain a managed reference to a clock producer.</p>
<h2>Synopsis</h2>
<pre><code>struct clk *devm_clk_get(struct device *dev, const char *id);</code></pre>
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
<p> devm_clk_get should not be called from within interrupt context. </p>
<p> The clock will automatically be freed when the device is unbound from the bus.</p>
<h2>Copyright</h2>
