---
title: "struct_regulator_bulk_data(9)"
name: "struct_regulator_bulk_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_regulator_bulk_data/"
description: "struct_regulator_bulk_data – Data used for bulk regulator operations."
---

<p>struct_regulator_bulk_data &#8211; Data used for bulk regulator operations.</p>
<h2>Synopsis</h2>
<pre><code>struct regulator_bulk_data {
    const char *supply;
    struct regulator *consumer;
};</code></pre>
<h2>Members</h2>
<p>supply</p>
<dl>
<dd>The name of the supply. Initialised by the user before using the bulk regulator APIs.</dl>
<p> consumer</p>
<dl>
<dd>The regulator consumer for the supply. This will be managed by the bulk API.</dl>
<h2>Description</h2>
<p>The regulator APIs provide a series of <code>regulator_bulk_</code> API calls as a convenience to consumers which require multiple supplies. This structure is used to manage data for these calls.</p>
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
