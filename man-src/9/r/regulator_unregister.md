---
title: "regulator_unregister(9)"
name: "regulator_unregister"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_unregister/"
description: "regulator_unregister – unregister regulator"
---

<p>regulator_unregister &#8211; unregister regulator</p>
<h2>Synopsis</h2>
<pre><code>void regulator_unregister(struct regulator_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>regulator to unregister</dl>
<h2>Description</h2>
<p>Called by regulator drivers to unregister a regulator.</p>
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
