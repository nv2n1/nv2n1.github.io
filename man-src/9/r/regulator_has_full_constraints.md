---
title: "regulator_has_full_constraints(9)"
name: "regulator_has_full_constraints"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_has_full_constraints/"
description: "regulator_has_full_constraints – the system has fully specified constraints"
---

<p>regulator_has_full_constraints &#8211; the system has fully specified constraints</p>
<h2>Synopsis</h2>
<pre><code>void regulator_has_full_constraints(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>Calling this function will cause the regulator API to disable all regulators which have a zero use count and don&#8217;t have an always_on constraint in a late_initcall. </p>
<p> The intention is that this will become the default behaviour in a future kernel release so users are encouraged to use this facility now.</p>
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
