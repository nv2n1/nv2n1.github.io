---
title: "regulator_set_current_limit(9)"
name: "regulator_set_current_limit"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_set_current_limit/"
description: "regulator_set_current_limit – set regulator output current limit"
---

<p>regulator_set_current_limit &#8211; set regulator output current limit</p>
<h2>Synopsis</h2>
<pre><code>int regulator_set_current_limit(struct regulator *regulator, int min_uA, int max_uA);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>min_uA</i></p>
<dl>
<dd>Minimum supported current in uA</dl>
<p> <i>max_uA</i></p>
<dl>
<dd>Maximum supported current in uA</dl>
<h2>Description</h2>
<p>Sets current sink to the desired output current. This can be set during any regulator state. IOW, regulator can be disabled or enabled. </p>
<p> If the regulator is enabled then the current will change to the new value immediately otherwise if the regulator is disabled the regulator will output at the new current when enabled.</p>
<h2>Note</h2>
<p>Regulator system constraints must be set for this regulator before calling this function otherwise this call will fail.</p>
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
