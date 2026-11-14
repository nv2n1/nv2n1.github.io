---
title: "regulator_get_hardware_vsel_register(9)"
name: "regulator_get_hardware_vsel_register"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_get_hardware_vsel_register/"
description: "regulator_get_hardware_vsel_register – get the HW voltage selector register"
---

<p>regulator_get_hardware_vsel_register &#8211; get the HW voltage selector register</p>
<h2>Synopsis</h2>
<pre><code>int regulator_get_hardware_vsel_register(struct regulator *regulator, unsigned *vsel_reg, unsigned *vsel_mask);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>vsel_reg</i></p>
<dl>
<dd>voltage selector register, output parameter</dl>
<p> <i>vsel_mask</i></p>
<dl>
<dd>mask for voltage selector bitfield, output parameter</dl>
<h2>Description</h2>
<p>Returns the hardware register offset and bitmask used for setting the regulator voltage. This might be useful when configuring voltage-scaling hardware or firmware that can make I2C requests behind the kernel&#8217;s back, for example. </p>
<p> On success, the output parameters <i>vsel_reg</i> and <i>vsel_mask</i> are filled in and 0 is returned, otherwise a negative errno is returned.</p>
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
