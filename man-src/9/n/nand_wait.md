---
title: "nand_wait(9)"
name: "nand_wait"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_wait/"
description: "nand_wait – [DEFAULT] wait until the command is done"
---

<p>nand_wait &#8211; [DEFAULT] wait until the command is done</p>
<h2>Synopsis</h2>
<pre><code>int nand_wait(struct mtd_info *mtd, struct nand_chip *chip);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>chip</i></p>
<dl>
<dd>NAND chip structure</dl>
<h2>Description</h2>
<p>Wait for command done. This applies to erase and program only.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
