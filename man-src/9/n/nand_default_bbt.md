---
title: "nand_default_bbt(9)"
name: "nand_default_bbt"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_default_bbt/"
description: "nand_default_bbt – [NAND Interface] Select a default bad block table for the device"
---

<p>nand_default_bbt &#8211; [NAND Interface] Select a default bad block table for the device</p>
<h2>Synopsis</h2>
<pre><code>int nand_default_bbt(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>This function selects the default bad block table support for the device and calls the nand_scan_bbt function.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
