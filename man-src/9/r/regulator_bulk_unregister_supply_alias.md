---
title: "regulator_bulk_unregister_supply_alias(9)"
name: "regulator_bulk_unregister_supply_alias"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_bulk_unregister_supply_alias/"
description: "regulator_bulk_unregister_supply_alias – unregister multiple aliases"
---

<p>regulator_bulk_unregister_supply_alias &#8211; unregister multiple aliases</p>
<h2>Synopsis</h2>
<pre><code>void regulator_bulk_unregister_supply_alias(struct device *dev, const char *const *id, int num_id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device that will be given as the regulator &#8220;consumer&#8221;</dl>
<p> <i>id</i></p>
<dl>
<dd>List of supply names or regulator IDs</dl>
<p> <i>num_id</i></p>
<dl>
<dd>Number of aliases to unregister</dl>
<h2>Description</h2>
<p>This helper function allows drivers to unregister several supply aliases in one operation.</p>
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
