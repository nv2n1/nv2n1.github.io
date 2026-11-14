---
title: "regulator_suspend_prepare(9)"
name: "regulator_suspend_prepare"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_suspend_prepare/"
description: "regulator_suspend_prepare – prepare regulators for system wide suspend"
---

<p>regulator_suspend_prepare &#8211; prepare regulators for system wide suspend</p>
<h2>Synopsis</h2>
<pre><code>int regulator_suspend_prepare(suspend_state_t state);</code></pre>
<h2>Arguments</h2>
<p><i>state</i></p>
<dl>
<dd>
<dd>system suspend state</dl>
<h2>Description</h2>
<p>Configure each regulator with it&#8217;s suspend operating parameters for state. This will usually be called by machine suspend code prior to supending.</p>
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
