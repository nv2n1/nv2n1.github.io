---
title: "regulator_get_drvdata(9)"
name: "regulator_get_drvdata"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_get_drvdata/"
description: "regulator_get_drvdata – get regulator driver data"
---

<p>regulator_get_drvdata &#8211; get regulator driver data</p>
<h2>Synopsis</h2>
<pre><code>void *regulator_get_drvdata(struct regulator *regulator);</code></pre>
<h2>Arguments</h2>
<p><i>regulator</i></p>
<dl>
<dd>
<dd>regulator</dl>
<h2>Description</h2>
<p>Get regulator driver private data. This call can be used in the consumer driver context when non API regulator specific functions need to be called.</p>
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
