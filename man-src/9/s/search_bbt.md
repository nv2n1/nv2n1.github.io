---
title: "search_bbt(9)"
name: "search_bbt"
section: "9"
letter: "s"
url: "/docs/linux/man/9-search_bbt/"
description: "search_bbt – [GENERIC] scan the device for a specific bad block table"
---

<p>search_bbt &#8211; [GENERIC] scan the device for a specific bad block table</p>
<h2>Synopsis</h2>
<pre><code>int search_bbt(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>buf</i></p>
<dl>
<dd>temporary buffer</dl>
<p> <i>td</i></p>
<dl>
<dd>descriptor for the bad block table</dl>
<h2>Description</h2>
<p>Read the bad block table by searching for a given ident pattern. Search is preformed either from the beginning up or from the end of the device downwards. The search starts always at the start of a block. If the option NAND_BBT_PERCHIP is given, each chip is searched for a bbt, which contains the bad block information of this chip. This is necessary to provide support for certain DOC devices. </p>
<p> The bbt ident pattern resides in the oob area of the first page in a block.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
