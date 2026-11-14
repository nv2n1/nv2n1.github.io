---
title: "nand_sync(9)"
name: "nand_sync"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_sync/"
description: "nand_sync – [MTD Interface] sync"
---

<p>nand_sync &#8211; [MTD Interface] sync</p>
<h2>Synopsis</h2>
<pre><code>void nand_sync(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>Sync is actually a wait for chip ready function.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
