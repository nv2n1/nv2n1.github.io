---
title: "verify_bbt_descr(9)"
name: "verify_bbt_descr"
section: "9"
letter: "v"
url: "/docs/linux/man/9-verify_bbt_descr/"
description: "verify_bbt_descr – verify the bad block description"
---

<p>verify_bbt_descr &#8211; verify the bad block description</p>
<h2>Synopsis</h2>
<pre><code>void verify_bbt_descr(struct mtd_info *mtd, struct nand_bbt_descr *bd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>bd</i></p>
<dl>
<dd>the table to verify</dl>
<h2>Description</h2>
<p>This functions performs a few sanity checks on the bad block description table.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
