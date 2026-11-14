---
title: "regulator_put(9)"
name: "regulator_put"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_put/"
description: "regulator_put – \"free\" the regulator source"
---

<p>regulator_put &#8211; &quot;free&quot; the regulator source</p>
<h2>Synopsis</h2>
<pre><code>void regulator_put(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Note</h2>
<p>drivers must ensure that all regulator_enable calls made on this regulator source are balanced by regulator_disable calls prior to calling this function.</p>
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
