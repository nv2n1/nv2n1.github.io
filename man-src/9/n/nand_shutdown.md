---
title: "nand_shutdown(9)"
name: "nand_shutdown"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_shutdown/"
description: "nand_shutdown – [MTD Interface] Finish the current NAND operation and prevent further operations"
---

<p>nand_shutdown &#8211; [MTD Interface] Finish the current NAND operation and prevent further operations</p>
<h2>Synopsis</h2>
<pre><code>void nand_shutdown(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
