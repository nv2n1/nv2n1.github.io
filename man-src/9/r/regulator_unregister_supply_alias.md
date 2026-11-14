---
title: "regulator_unregister_supply_alias(9)"
name: "regulator_unregister_supply_alias"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_unregister_supply_alias/"
description: "regulator_unregister_supply_alias – Remove device alias"
---

<p>regulator_unregister_supply_alias &#8211; Remove device alias</p>
<h2>Synopsis</h2>
<pre><code>void regulator_unregister_supply_alias(struct device *dev, const char *id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device that will be given as the regulator &#8220;consumer&#8221;</dl>
<p> <i>id</i></p>
<dl>
<dd>Supply name or regulator ID</dl>
<h2>Description</h2>
<p>Remove a lookup alias if one exists for id on dev.</p>
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
