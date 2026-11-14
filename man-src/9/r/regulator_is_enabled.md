---
title: "regulator_is_enabled(9)"
name: "regulator_is_enabled"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_is_enabled/"
description: "regulator_is_enabled – is the regulator output enabled"
---

<p>regulator_is_enabled &#8211; is the regulator output enabled</p>
<h2>Synopsis</h2>
<pre><code>int regulator_is_enabled(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>Returns positive if the regulator driver backing the source/client has requested that the device be enabled, zero if it hasn&#8217;t, else a negative errno code. </p>
<p> Note that the device backing this regulator handle can have multiple users, so it might be enabled even if <code>regulator_enable</code> was never called for this particular source.</p>
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
