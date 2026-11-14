---
title: "regulator_set_voltage_time(9)"
name: "regulator_set_voltage_time"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_set_voltage_time/"
description: "regulator_set_voltage_time – get raise/fall time"
---

<p>regulator_set_voltage_time &#8211; get raise/fall time</p>
<h2>Synopsis</h2>
<pre><code>int regulator_set_voltage_time(struct regulator *regulator, int old_uV, int new_uV);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>old_uV</i></p>
<dl>
<dd>starting voltage in microvolts</dl>
<p> <i>new_uV</i></p>
<dl>
<dd>target voltage in microvolts</dl>
<h2>Description</h2>
<p>Provided with the starting and ending voltage, this function attempts to calculate the time in microseconds required to rise or fall to this new voltage.</p>
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
