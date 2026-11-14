---
title: "regulator_register(9)"
name: "regulator_register"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_register/"
description: "regulator_register – register regulator"
---

<p>regulator_register &#8211; register regulator</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_dev *regulator_register(const struct regulator_desc *regulator_desc, const struct regulator_config *cfg);</code></pre>
<h2>Arguments</h2>
<p><i>regulator_desc</i></p>
<dl>
<dd>
<dd>regulator to register</dl>
<p> <i>cfg</i></p>
<dl>
<dd>runtime configuration for regulator</dl>
<h2>Description</h2>
<p>Called by regulator drivers to register a regulator. Returns a valid pointer to struct regulator_dev on success or an <code>ERR_PTR</code> on error.</p>
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
