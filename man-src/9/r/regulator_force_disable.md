---
title: "regulator_force_disable(9)"
name: "regulator_force_disable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_force_disable/"
description: "regulator_force_disable – force disable regulator output"
---

<p>regulator_force_disable &#8211; force disable regulator output</p>
<h2>Synopsis</h2>
<pre><code>int regulator_force_disable(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Forcibly disable the regulator output voltage or current.</p>
<h2>Note</h2>
<p>this *will* disable the regulator output even if other consumer devices have it enabled. This should be used for situations when device damage will likely occur if the regulator is not disabled (e.g. over temp).</p>
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
