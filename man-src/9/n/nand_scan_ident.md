---
title: "nand_scan_ident(9)"
name: "nand_scan_ident"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_scan_ident/"
description: "nand_scan_ident – [NAND Interface] Scan for the NAND device"
---

<p>nand_scan_ident &#8211; [NAND Interface] Scan for the NAND device</p>
<h2>Synopsis</h2>
<pre><code>int nand_scan_ident(struct mtd_info *mtd, int maxchips, struct nand_flash_dev *table);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>maxchips</i></p>
<dl>
<dd>number of chips to scan for</dl>
<p> <i>table</i></p>
<dl>
<dd>alternative NAND ID table</dl>
<h2>Description</h2>
<p>This is the first phase of the normal <code>nand_scan</code> function. It reads the flash ID and sets up MTD fields accordingly.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
