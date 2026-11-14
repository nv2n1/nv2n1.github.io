---
title: "regulator_set_voltage(9)"
name: "regulator_set_voltage"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_set_voltage/"
description: "regulator_set_voltage – set regulator output voltage"
---

<p>regulator_set_voltage &#8211; set regulator output voltage</p>
<h2>Synopsis</h2>
<pre><code>int regulator_set_voltage(struct regulator *regulator, int min_uV, int max_uV);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>min_uV</i></p>
<dl>
<dd>Minimum required voltage in uV</dl>
<p> <i>max_uV</i></p>
<dl>
<dd>Maximum acceptable voltage in uV</dl>
<h2>Description</h2>
<p>Sets a voltage regulator to the desired output voltage. This can be set during any regulator state. IOW, regulator can be disabled or enabled. </p>
<p> If the regulator is enabled then the voltage will change to the new value immediately otherwise if the regulator is disabled the regulator will output at the new voltage when enabled.</p>
<h2>Note</h2>
<p>If the regulator is shared between several devices then the lowest request voltage that meets the system constraints will be used. Regulator system constraints must be set for this regulator before calling this function otherwise this call will fail.</p>
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
