---
title: "devm_clk_put(9)"
name: "devm_clk_put"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_clk_put/"
description: "devm_clk_put – \"free\" a managed clock source"
---

<p>devm_clk_put &#8211; &quot;free&quot; a managed clock source</p>
<h2>Synopsis</h2>
<pre><code>void devm_clk_put(struct device *dev, struct clk *clk);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device used to acquire the clock</dl>
<p> <i>clk</i></p>
<dl>
<dd>clock source acquired with <code>devm_clk_get</code></dl>
<h2>Note</h2>
<p>drivers must ensure that all clk_enable calls made on this clock source are balanced by clk_disable calls prior to calling this function. </p>
<p> clk_put should not be called from within interrupt context.</p>
<h2>Copyright</h2>
