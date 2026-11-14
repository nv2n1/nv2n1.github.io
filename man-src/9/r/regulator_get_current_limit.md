---
title: "regulator_get_current_limit(9)"
name: "regulator_get_current_limit"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_get_current_limit/"
description: "regulator_get_current_limit – get regulator output current"
---

<p>regulator_get_current_limit &#8211; get regulator output current</p>
<h2>Synopsis</h2>
<pre><code>int regulator_get_current_limit(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator source</dl>
<h2>Description</h2>
<p>This returns the current supplied by the specified current sink in uA.</p>
<h2>Note</h2>
<p>If the regulator is disabled it will return the current value. This function should not be used to determine regulator state.</p>
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
