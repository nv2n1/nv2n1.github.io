---
title: "nand_create_badblock_pattern(9)"
name: "nand_create_badblock_pattern"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_create_badblock_pattern/"
description: "nand_create_badblock_pattern – [INTERN] Creates a BBT descriptor structure"
---

<p>nand_create_badblock_pattern &#8211; [INTERN] Creates a BBT descriptor structure</p>
<h2>Synopsis</h2>
<pre><code>int nand_create_badblock_pattern(struct nand_chip *this);</code></pre>
<h2>Arguments</h2>
<p><i>this</i></p>
<dl>
<dd>
<dd>NAND chip to create descriptor for</dl>
<h2>Description</h2>
<p>This function allocates and initializes a nand_bbt_descr for BBM detection based on the properties of <i>this</i>. The new descriptor is stored in this-&gt;badblock_pattern. Thus, this-&gt;badblock_pattern should be NULL when passed to this function.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
