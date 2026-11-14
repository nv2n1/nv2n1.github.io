---
title: "regulator_get_voltage(9)"
name: "regulator_get_voltage"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_get_voltage/"
description: "regulator_get_voltage – get regulator output voltage"
---

<p>regulator_get_voltage &#8211; get regulator output voltage</p>
<h2>Synopsis</h2>
<pre><code>int regulator_get_voltage(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>This returns the current regulator voltage in uV.</p>
<h2>Note</h2>
<p>If the regulator is disabled it will return the voltage value. This function should not be used to determine regulator state.</p>
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
