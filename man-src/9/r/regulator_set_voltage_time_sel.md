---
title: "regulator_set_voltage_time_sel(9)"
name: "regulator_set_voltage_time_sel"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_set_voltage_time_sel/"
description: "regulator_set_voltage_time_sel – get raise/fall time"
---

<p>regulator_set_voltage_time_sel &#8211; get raise/fall time</p>
<h2>Synopsis</h2>
<pre><code>int regulator_set_voltage_time_sel(struct regulator_dev *rdev, unsigned int old_selector, unsigned int new_selector);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>regulator source device</dl>
<p> <i>old_selector</i></p>
<dl>
<dd>selector for starting voltage</dl>
<p> <i>new_selector</i></p>
<dl>
<dd>selector for target voltage</dl>
<h2>Description</h2>
<p>Provided with the starting and target voltage selectors, this function returns time in microseconds required to rise or fall to this new voltage </p>
<p> Drivers providing ramp_delay in regulation_constraints can use this as their <code>set_voltage_time_sel</code> operation.</p>
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
