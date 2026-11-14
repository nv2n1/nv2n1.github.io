---
title: "regulator_enable(9)"
name: "regulator_enable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_enable/"
description: "regulator_enable – enable regulator output"
---

<p>regulator_enable &#8211; enable regulator output</p>
<h2>Synopsis</h2>
<pre><code>int regulator_enable(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Request that the regulator be enabled with the regulator output at the predefined voltage or current value. Calls to <code>regulator_enable</code> must be balanced with calls to <code>regulator_disable</code>.</p>
<h2>Note</h2>
<p>the output value can be set by other drivers, boot loader or may be hardwired in the regulator.</p>
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
