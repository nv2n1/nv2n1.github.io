---
title: "regulator_bulk_enable(9)"
name: "regulator_bulk_enable"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_bulk_enable/"
description: "regulator_bulk_enable – enable multiple regulator consumers"
---

<p>regulator_bulk_enable &#8211; enable multiple regulator consumers</p>
<h2>Synopsis</h2>
<pre><code>int regulator_bulk_enable(int num_consumers, struct regulator_bulk_data *consumers);</code></pre>
<h2>Arguments</h2>
<p><i>num_consumers</i></p>
<dl>
<dd>
<dd>Number of consumers</dl>
<p> <i>consumers</i></p>
<dl>
<dd>Consumer data; clients are stored here. <i>return</i> 0 on success, an errno on failure</dl>
<h2>Description</h2>
<p>This convenience API allows consumers to enable multiple regulator clients in a single API call. If any consumers cannot be enabled then any others that were enabled will be disabled again prior to return.</p>
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
