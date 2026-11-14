---
title: "create_bbt(9)"
name: "create_bbt"
section: "9"
letter: "c"
url: "/docs/linux/man/9-create_bbt/"
description: "create_bbt – [GENERIC] Create a bad block table by scanning the device"
---

<p>create_bbt &#8211; [GENERIC] Create a bad block table by scanning the device</p>
<h2>Synopsis</h2>
<pre><code>int create_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *bd, int chip);</code></pre>
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
<p> <i>chip</i></p>
<dl>
<dd>create the table for a specific chip, -1 read all chips; applies only if NAND_BBT_PERCHIP option is set</dl>
<h2>Description</h2>
<p>Create a bad block table by scanning the device for the given good/bad block identify pattern.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
