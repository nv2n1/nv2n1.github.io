---
title: "nand_reset(9)"
name: "nand_reset"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_reset/"
description: "nand_reset – Reset and initialize a NAND device"
---

<p>nand_reset &#8211; Reset and initialize a NAND device</p>
<h2>Synopsis</h2>
<pre><code>int nand_reset(struct nand_chip *chip, int chipnr);</code></pre>
<h2>Arguments</h2>
<p><i>chip</i></p>
<dl>
<dd>
<dd>The NAND chip</dl>
<p> <i>chipnr</i></p>
<dl>
<dd>Internal die id</dl>
<h2>Description</h2>
<p>Returns 0 for success or negative error code otherwise</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
