---
title: "regulator_allow_bypass(9)"
name: "regulator_allow_bypass"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_allow_bypass/"
description: "regulator_allow_bypass – allow the regulator to go into bypass mode"
---

<p>regulator_allow_bypass &#8211; allow the regulator to go into bypass mode</p>
<h2>Synopsis</h2>
<pre><code>int regulator_allow_bypass(struct regulator *regulator, bool enable);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>Regulator to configure</dl>
<p> <i>enable</i></p>
<dl>
<dd>enable or disable bypass mode</dl>
<h2>Description</h2>
<p>Allow the regulator to go into bypass mode if all other consumers for the regulator also enable bypass mode and the machine constraints allow this. Bypass mode means that the regulator is simply passing the input directly to the output with no regulation.</p>
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
