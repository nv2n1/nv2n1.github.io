---
title: "nand_check_wp(9)"
name: "nand_check_wp"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_check_wp/"
description: "nand_check_wp – [GENERIC] check if the chip is write protected"
---

<p>nand_check_wp &#8211; [GENERIC] check if the chip is write protected</p>
<h2>Synopsis</h2>
<pre><code>int nand_check_wp(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>Check, if the device is write protected. The function expects, that the device is already selected.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
