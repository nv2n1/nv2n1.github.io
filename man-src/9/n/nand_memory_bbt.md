---
title: "nand_memory_bbt(9)"
name: "nand_memory_bbt"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_memory_bbt/"
description: "nand_memory_bbt – [GENERIC] create a memory based bad block table"
---

<p>nand_memory_bbt &#8211; [GENERIC] create a memory based bad block table</p>
<h2>Synopsis</h2>
<pre><code>int nand_memory_bbt(struct mtd_info *mtd, struct nand_bbt_descr *bd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>bd</i></p>
<dl>
<dd>descriptor for the good/bad block search pattern</dl>
<h2>Description</h2>
<p>The function creates a memory based bbt by scanning the device for manufacturer / software marked good / bad blocks.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
