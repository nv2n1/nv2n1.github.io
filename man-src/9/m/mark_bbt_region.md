---
title: "mark_bbt_region(9)"
name: "mark_bbt_region"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mark_bbt_region/"
description: "mark_bbt_region – [GENERIC] mark the bad block table regions"
---

<p>mark_bbt_region &#8211; [GENERIC] mark the bad block table regions</p>
<h2>Synopsis</h2>
<pre><code>void mark_bbt_region(struct mtd_info *mtd, struct nand_bbt_descr *td);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>td</i></p>
<dl>
<dd>bad block table descriptor</dl>
<h2>Description</h2>
<p>The bad block table regions are marked as &#8220;bad&#8221; to prevent accidental erasures / writes. The regions are identified by the mark 0x02.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
