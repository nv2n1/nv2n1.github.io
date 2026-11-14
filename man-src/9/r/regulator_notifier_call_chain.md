---
title: "regulator_notifier_call_chain(9)"
name: "regulator_notifier_call_chain"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_notifier_call_chain/"
description: "regulator_notifier_call_chain – call regulator event notifier"
---

<p>regulator_notifier_call_chain &#8211; call regulator event notifier</p>
<h2>Synopsis</h2>
<pre><code>int regulator_notifier_call_chain(struct regulator_dev *rdev, unsigned long event, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>event</i></p>
<dl>
<dd>notifier block</dl>
<p> <i>data</i></p>
<dl>
<dd>callback-specific data.</dl>
<h2>Description</h2>
<p>Called by regulator drivers to notify clients a regulator event has occurred. We also notify regulator clients downstream. Note lock must be held by caller.</p>
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
