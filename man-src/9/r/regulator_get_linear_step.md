---
title: "regulator_get_linear_step(9)"
name: "regulator_get_linear_step"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_get_linear_step/"
description: "regulator_get_linear_step – return the voltage step size between VSEL values"
---

<p>regulator_get_linear_step &#8211; return the voltage step size between VSEL values</p>
<h2>Synopsis</h2>
<pre><code>unsigned int regulator_get_linear_step(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Returns the voltage step size between VSEL values for linear regulators, or return 0 if the regulator isn&#8217;t a linear regulator.</p>
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
