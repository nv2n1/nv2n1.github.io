---
title: "nand_erase(9)"
name: "nand_erase"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_erase/"
description: "nand_erase – [MTD Interface] erase block(s)"
---

<p>nand_erase &#8211; [MTD Interface] erase block(s)</p>
<h2>Synopsis</h2>
<pre><code>int nand_erase(struct mtd_info *mtd, struct erase_info *instr);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>instr</i></p>
<dl>
<dd>erase instruction</dl>
<h2>Description</h2>
<p>Erase one ore more blocks.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
