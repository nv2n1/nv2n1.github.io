---
title: "nand_scan_tail(9)"
name: "nand_scan_tail"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_scan_tail/"
description: "nand_scan_tail – [NAND Interface] Scan for the NAND device"
---

<p>nand_scan_tail &#8211; [NAND Interface] Scan for the NAND device</p>
<h2>Synopsis</h2>
<pre><code>int nand_scan_tail(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>This is the second phase of the normal <code>nand_scan</code> function. It fills out all the uninitialized function pointers with the defaults and scans for a bad block table if appropriate.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
