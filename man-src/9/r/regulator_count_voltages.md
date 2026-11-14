---
title: "regulator_count_voltages(9)"
name: "regulator_count_voltages"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_count_voltages/"
description: "regulator_count_voltages – count regulator_list_voltage selectors"
---

<p>regulator_count_voltages &#8211; count <code>regulator_list_voltage</code> selectors</p>
<h2>Synopsis</h2>
<pre><code>int regulator_count_voltages(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Returns number of selectors, or negative errno. Selectors are numbered starting at zero, and typically correspond to bitfields in hardware registers.</p>
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
