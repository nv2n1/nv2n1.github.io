---
title: "regulator_register_notifier(9)"
name: "regulator_register_notifier"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_register_notifier/"
description: "regulator_register_notifier – register regulator event notifier"
---

<p>regulator_register_notifier &#8211; register regulator event notifier</p>
<h2>Synopsis</h2>
<pre><code>int regulator_register_notifier(struct regulator *regulator, struct notifier_block *nb);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>nb</i></p>
<dl>
<dd>notifier block</dl>
<h2>Description</h2>
<p>Register notifier block to receive regulator events.</p>
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
