---
title: "regulator_bulk_free(9)"
name: "regulator_bulk_free"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_bulk_free/"
description: "regulator_bulk_free – free multiple regulator consumers"
---

<p>regulator_bulk_free &#8211; free multiple regulator consumers</p>
<h2>Synopsis</h2>
<pre><code>void regulator_bulk_free(int num_consumers, struct regulator_bulk_data *consumers);</code></pre>
<h2>Arguments</h2>
<p><i>num_consumers</i></p>
<dl>
<dd>
<dd>Number of consumers</dl>
<p> <i>consumers</i></p>
<dl>
<dd>Consumer data; clients are stored here.</dl>
<h2>Description</h2>
<p>This convenience API allows consumers to free multiple regulator clients in a single API call.</p>
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
