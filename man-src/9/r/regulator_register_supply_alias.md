---
title: "regulator_register_supply_alias(9)"
name: "regulator_register_supply_alias"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_register_supply_alias/"
description: "regulator_register_supply_alias – Provide device alias for supply lookup"
---

<p>regulator_register_supply_alias &#8211; Provide device alias for supply lookup</p>
<h2>Synopsis</h2>
<pre><code>int regulator_register_supply_alias(struct device *dev, const char *id, struct device *alias_dev, const char *alias_id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device that will be given as the regulator &#8220;consumer&#8221;</dl>
<p> <i>id</i></p>
<dl>
<dd>Supply name or regulator ID</dl>
<p> <i>alias_dev</i></p>
<dl>
<dd>device that should be used to lookup the supply</dl>
<p> <i>alias_id</i></p>
<dl>
<dd>Supply name or regulator ID that should be used to lookup the supply</dl>
<h2>Description</h2>
<p>All lookups for id on dev will instead be conducted for alias_id on alias_dev.</p>
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
