---
title: "regulator_set_mode(9)"
name: "regulator_set_mode"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_set_mode/"
description: "regulator_set_mode – set regulator operating mode"
---

<p>regulator_set_mode &#8211; set regulator operating mode</p>
<h2>Synopsis</h2>
<pre><code>int regulator_set_mode(struct regulator *regulator, unsigned int mode);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<p> <i>mode</i></p>
<dl>
<dd>operating mode &#8211; one of the REGULATOR_MODE constants</dl>
<h2>Description</h2>
<p>Set regulator operating mode to increase regulator efficiency or improve regulation performance.</p>
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
