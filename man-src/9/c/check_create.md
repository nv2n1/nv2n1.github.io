---
title: "check_create(9)"
name: "check_create"
section: "9"
letter: "c"
url: "/docs/linux/man/9-check_create/"
description: "check_create – [GENERIC] create and write bbt(s) if necessary"
---

<p>check_create &#8211; [GENERIC] create and write bbt(s) if necessary</p>
<h2>Synopsis</h2>
<pre><code>int check_create(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *bd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>temporary buffer</dl>
<p> <i>bd</i></p>
<dl>
<dd>descriptor for the good/bad block search pattern</dl>
<h2>Description</h2>
<p>The function checks the results of the previous call to read_bbt and creates / updates the bbt(s) if necessary. Creation is necessary if no bbt was found for the chip/device. Update is necessary if one of the tables is missing or the version nr. of one table is less than the other.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
