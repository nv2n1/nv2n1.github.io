---
title: "single_erase(9)"
name: "single_erase"
section: "9"
letter: "s"
url: "/docs/linux/man/9-single_erase/"
description: "single_erase – [GENERIC] NAND standard block erase command function"
---

<p>single_erase &#8211; [GENERIC] NAND standard block erase command function</p>
<h2>Synopsis</h2>
<pre><code>int single_erase(struct mtd_info *mtd, int page);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>page</i></p>
<dl>
<dd>the page address of the block which will be erased</dl>
<h2>Description</h2>
<p>Standard erase command for NAND chips. Returns NAND status.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
