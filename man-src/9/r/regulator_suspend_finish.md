---
title: "regulator_suspend_finish(9)"
name: "regulator_suspend_finish"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_suspend_finish/"
description: "regulator_suspend_finish – resume regulators from system wide suspend"
---

<p>regulator_suspend_finish &#8211; resume regulators from system wide suspend</p>
<h2>Synopsis</h2>
<pre><code>int regulator_suspend_finish(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>Turn on regulators that might be turned off by regulator_suspend_prepare and that should be turned on according to the regulators properties.</p>
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
