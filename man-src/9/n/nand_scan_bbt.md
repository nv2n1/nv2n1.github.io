---
title: "nand_scan_bbt(9)"
name: "nand_scan_bbt"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_scan_bbt/"
description: "nand_scan_bbt – [NAND Interface] scan, find, read and maybe create bad block table(s)"
---

<p>nand_scan_bbt &#8211; [NAND Interface] scan, find, read and maybe create bad block table(s)</p>
<h2>Synopsis</h2>
<pre><code>int nand_scan_bbt(struct mtd_info *mtd, struct nand_bbt_descr *bd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>bd</i></p>
<dl>
<dd>descriptor for the good/bad block search pattern</dl>
<h2>Description</h2>
<p>The function checks, if a bad block table(s) is/are already available. If not it scans the device for manufacturer marked good / bad blocks and writes the bad block table(s) to the selected place. </p>
<p> The bad block table memory is allocated here. It must be freed by calling the nand_free_bbt function.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
