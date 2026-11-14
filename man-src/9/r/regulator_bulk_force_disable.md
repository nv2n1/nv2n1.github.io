---
title: "regulator_bulk_force_disable(9)"
name: "regulator_bulk_force_disable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_bulk_force_disable/"
description: "regulator_bulk_force_disable – force disable multiple regulator consumers"
---

<p>regulator_bulk_force_disable &#8211; force disable multiple regulator consumers</p>
<h2>Synopsis</h2>
<pre><code>int regulator_bulk_force_disable(int num_consumers, struct regulator_bulk_data *consumers);</code></pre>
<h2>Arguments</h2>
<p><i>num_consumers</i></p>
<dl>
<dd>
<dd>Number of consumers</dl>
<p> <i>consumers</i></p>
<dl>
<dd>Consumer data; clients are stored here. <i>return</i> 0 on success, an errno on failure</dl>
<h2>Description</h2>
<p>This convenience API allows consumers to forcibly disable multiple regulator clients in a single API call.</p>
<h2>Note</h2>
<p>This should be used for situations when device damage will likely occur if the regulators are not disabled (e.g. over temp). Although regulator_force_disable function call for some consumers can return error numbers, the function is called for all consumers.</p>
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
