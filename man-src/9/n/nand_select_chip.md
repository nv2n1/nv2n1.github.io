---
title: "nand_select_chip(9)"
name: "nand_select_chip"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_select_chip/"
description: "nand_select_chip – [DEFAULT] control CE line"
---

<p>nand_select_chip &#8211; [DEFAULT] control CE line</p>
<h2>Synopsis</h2>
<pre><code>void nand_select_chip(struct mtd_info *mtd, int chipnr);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>chipnr</i></p>
<dl>
<dd>chipnumber to select, -1 for deselect</dl>
<h2>Description</h2>
<p>Default select function for 1 chip devices.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
