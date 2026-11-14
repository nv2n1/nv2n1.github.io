---
title: "struct_regulator_consumer_supply(9)"
name: "struct_regulator_consumer_supply"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_consumer_supply/"
description: "struct_regulator_consumer_supply – supply -> device mapping"
---

<p>struct_regulator_consumer_supply &#8211; supply -&gt; device mapping</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_consumer_supply {
    const char *dev_name;
    const char *supply;
};</code></pre>
<h2>Members</h2>
<p>dev_name</p>
<dl>
<dd>Result of <code>dev_name</code> for the consumer.</dl>
<p> supply</p>
<dl>
<dd>Name for the supply.</dl>
<h2>Description</h2>
<p>This maps a supply name to a device. Use of dev_name allows support for buses which make struct device available late such as I2C.</p>
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
