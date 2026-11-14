---
title: "search_read_bbts(9)"
name: "search_read_bbts"
section: "9"
letter: "s"
url: "/docs/linux/man/9-search_read_bbts/"
description: "search_read_bbts – [GENERIC] scan the device for bad block table(s)"
---

<p>search_read_bbts &#8211; [GENERIC] scan the device for bad block table(s)</p>
<h2>Synopsis</h2>
<pre><code>void search_read_bbts(struct mtd_info *mtd, uint8_t *buf, struct nand_bbt_descr *td, struct nand_bbt_descr *md);</code></pre>
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
<p> <i>md</i></p>
<dl>
<dd>descriptor for the bad block table mirror</dl>
<h2>Description</h2>
<p>Search and read the bad block table(s).</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
