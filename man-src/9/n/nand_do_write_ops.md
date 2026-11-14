---
title: "nand_do_write_ops(9)"
name: "nand_do_write_ops"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_do_write_ops/"
description: "nand_do_write_ops – [INTERN] NAND write with ECC"
---

<p>nand_do_write_ops &#8211; [INTERN] NAND write with ECC</p>
<h2>Synopsis</h2>
<pre><code>int nand_do_write_ops(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>to</i></p>
<dl>
<dd>offset to write to</dl>
<p> <i>ops</i></p>
<dl>
<dd>oob operations description structure</dl>
<h2>Description</h2>
<p>NAND write with ECC.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
