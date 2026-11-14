---
title: "regulator_disable_deferred(9)"
name: "regulator_disable_deferred"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_disable_deferred/"
description: "regulator_disable_deferred – disable regulator output with delay"
---

<p>regulator_disable_deferred &#8211; disable regulator output with delay</p>
<h2>Synopsis</h2>
<pre><code>int regulator_disable_deferred(struct regulator *regulator, int ms);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>ms</i></p>
<dl>
<dd>miliseconds until the regulator is disabled</dl>
<h2>Description</h2>
<p>Execute <code>regulator_disable</code> on the regulator after a delay. This is intended for use with devices that require some time to quiesce.</p>
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
