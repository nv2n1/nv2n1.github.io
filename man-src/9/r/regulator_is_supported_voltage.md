---
title: "regulator_is_supported_voltage(9)"
name: "regulator_is_supported_voltage"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_is_supported_voltage/"
description: "regulator_is_supported_voltage – check if a voltage range can be supported"
---

<p>regulator_is_supported_voltage &#8211; check if a voltage range can be supported</p>
<h2>Synopsis</h2>
<pre><code>int regulator_is_supported_voltage(struct regulator *regulator, int min_uV, int max_uV);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>Regulator to check.</dl>
<p> <i>min_uV</i></p>
<dl>
<dd>Minimum required voltage in uV.</dl>
<p> <i>max_uV</i></p>
<dl>
<dd>Maximum required voltage in uV.</dl>
<h2>Description</h2>
<p>Returns a boolean or a negative error code.</p>
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
