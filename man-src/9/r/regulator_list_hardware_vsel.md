---
title: "regulator_list_hardware_vsel(9)"
name: "regulator_list_hardware_vsel"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_list_hardware_vsel/"
description: "regulator_list_hardware_vsel – get the HW-specific register value for a selector"
---

<p>regulator_list_hardware_vsel &#8211; get the HW-specific register value for a selector</p>
<h2>Synopsis</h2>
<pre><code>int regulator_list_hardware_vsel(struct regulator *regulator, unsigned selector);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>selector</i></p>
<dl>
<dd>identify voltage to list</dl>
<h2>Description</h2>
<p>Converts the selector to a hardware-specific voltage selector that can be directly written to the regulator registers. The address of the voltage register can be determined by calling <i>regulator_get_hardware_vsel_register</i>. </p>
<p> On error a negative errno is returned.</p>
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
