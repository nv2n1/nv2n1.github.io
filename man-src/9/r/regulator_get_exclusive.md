---
title: "regulator_get_exclusive(9)"
name: "regulator_get_exclusive"
section: "9"
letter: "r"
url: "/docs/linux/man/9-regulator_get_exclusive/"
description: "regulator_get_exclusive – obtain exclusive access to a regulator."
---

<p>regulator_get_exclusive &#8211; obtain exclusive access to a regulator.</p>
<h2>Synopsis</h2>
<pre><code>struct regulator *regulator_get_exclusive(struct device *dev, const char *id);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device for regulator &#8220;consumer&#8221;</dl>
<p> <i>id</i></p>
<dl>
<dd>Supply name or regulator ID.</dl>
<h2>Description</h2>
<p>Returns a struct regulator corresponding to the regulator producer, or <code>IS_ERR</code> condition containing errno. Other consumers will be unable to obtain this regulator while this reference is held and the use count for the regulator will be initialised to reflect the current state of the regulator. </p>
<p> This is intended for use by consumers which cannot tolerate shared use of the regulator such as those which need to force the regulator off for correct operation of the hardware they are controlling. </p>
<p> Use of supply names configured via <code>regulator_set_device_supply</code> is strongly encouraged. It is recommended that the supply name used should match the name used for the supply and/or the relevant device pins in the datasheet.</p>
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
