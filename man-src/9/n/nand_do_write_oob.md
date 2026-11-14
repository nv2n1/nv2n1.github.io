---
title: "nand_do_write_oob(9)"
name: "nand_do_write_oob"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_do_write_oob/"
description: "nand_do_write_oob – [MTD Interface] NAND write out-of-band"
---

<p>nand_do_write_oob &#8211; [MTD Interface] NAND write out-of-band</p>
<h2>Synopsis</h2>
<pre><code>int nand_do_write_oob(struct mtd_info *mtd, loff_t to, struct mtd_oob_ops *ops);</code></pre>
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
<dd>oob operation description structure</dl>
<h2>Description</h2>
<p>NAND write out-of-band.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
