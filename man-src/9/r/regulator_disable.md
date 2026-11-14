---
title: "regulator_disable(9)"
name: "regulator_disable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_disable/"
description: "regulator_disable – disable regulator output"
---

<p>regulator_disable &#8211; disable regulator output</p>
<h2>Synopsis</h2>
<pre><code>int regulator_disable(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Disable the regulator output voltage or current. Calls to <code>regulator_enable</code> must be balanced with calls to <code>regulator_disable</code>.</p>
<h2>Note</h2>
<p>this will only disable the regulator output if no other consumer devices have it enabled, the regulator device supports disabling and machine constraints permit this operation.</p>
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
