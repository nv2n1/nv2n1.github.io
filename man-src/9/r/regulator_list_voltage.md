---
title: "regulator_list_voltage(9)"
name: "regulator_list_voltage"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_list_voltage/"
description: "regulator_list_voltage – enumerate supported voltages"
---

<p>regulator_list_voltage &#8211; enumerate supported voltages</p>
<h2>Synopsis</h2>
<pre><code>int regulator_list_voltage(struct regulator *regulator, unsigned selector);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>selector</i></p>
<dl>
<dd>identify voltage to list</dl>
<h2>Context</h2>
<p>can sleep</p>
<h2>Description</h2>
<p>Returns a voltage that can be passed to <i>regulator_set_voltage</i>(), zero if this selector code can&#8217;t be used on this system, or a negative errno.</p>
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
