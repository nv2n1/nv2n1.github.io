---
title: "nand_scan(9)"
name: "nand_scan"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_scan/"
description: "nand_scan – [NAND Interface] Scan for the NAND device"
---

<p>nand_scan &#8211; [NAND Interface] Scan for the NAND device</p>
<h2>Synopsis</h2>
<pre><code>int nand_scan(struct mtd_info *mtd, int maxchips);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>maxchips</i></p>
<dl>
<dd>number of chips to scan for</dl>
<h2>Description</h2>
<p>This fills out all the uninitialized function pointers with the defaults. The flash ID is read and the mtd/chip structures are filled with the appropriate values.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
