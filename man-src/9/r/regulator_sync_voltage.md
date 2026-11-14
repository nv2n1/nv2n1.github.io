---
title: "regulator_sync_voltage(9)"
name: "regulator_sync_voltage"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_sync_voltage/"
description: "regulator_sync_voltage – re-apply last regulator output voltage"
---

<p>regulator_sync_voltage &#8211; re-apply last regulator output voltage</p>
<h2>Synopsis</h2>
<pre><code>int regulator_sync_voltage(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Re-apply the last configured voltage. This is intended to be used where some external control source the consumer is cooperating with has caused the configured voltage to change.</p>
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
