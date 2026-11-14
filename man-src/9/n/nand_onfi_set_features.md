---
title: "nand_onfi_set_features(9)"
name: "nand_onfi_set_features"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_onfi_set_features/"
description: "nand_onfi_set_features – [REPLACEABLE] set features for ONFI nand"
---

<p>nand_onfi_set_features &#8211; [REPLACEABLE] set features for ONFI nand</p>
<h2>Synopsis</h2>
<pre><code>int nand_onfi_set_features(struct mtd_info *mtd, struct nand_chip *chip, int addr, uint8_t *subfeature_param);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>chip</i></p>
<dl>
<dd>nand chip info structure</dl>
<p> <i>addr</i></p>
<dl>
<dd>feature address.</dl>
<p> <i>subfeature_param</i></p>
<dl>
<dd>the subfeature parameters, a four bytes array.</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
