---
title: "rdev_get_drvdata(9)"
name: "rdev_get_drvdata"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rdev_get_drvdata/"
description: "rdev_get_drvdata – get rdev regulator driver data"
---

<p>rdev_get_drvdata &#8211; get rdev regulator driver data</p>
<h2>Synopsis</h2>
<pre><code>void *rdev_get_drvdata(struct regulator_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>regulator</dl>
<h2>Description</h2>
<p>Get rdev regulator driver private data. This call can be used in the regulator driver context.</p>
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
