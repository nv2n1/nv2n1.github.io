---
title: "regulator_bulk_get(9)"
name: "regulator_bulk_get"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_bulk_get/"
description: "regulator_bulk_get – get multiple regulator consumers"
---

<p>regulator_bulk_get &#8211; get multiple regulator consumers</p>
<h2>Synopsis</h2>
<pre><code>int regulator_bulk_get(struct device *dev, int num_consumers, struct regulator_bulk_data *consumers);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>Device to supply</dl>
<p> <i>num_consumers</i></p>
<dl>
<dd>Number of consumers to register</dl>
<p> <i>consumers</i></p>
<dl>
<dd>Configuration of consumers; clients are stored here.</dl>
<h2>Description</h2>
<p><i>return</i> 0 on success, an errno on failure. </p>
<p> This helper function allows drivers to get several regulator consumers in one operation. If any of the regulators cannot be acquired then any regulators that were allocated will be freed before returning to the caller.</p>
<h2>Authors</h2>
<p><code>Liam Girdwood</code> &lt;lrg [at] slimlogic.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Mark Brown</code> &lt;broonie [at] opensource.wolfsonmicro.com&gt;<br />
 Wolfson Microelectronics, </p>
<p>&nbsp;<wbr>&nbsp;<wbr></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
