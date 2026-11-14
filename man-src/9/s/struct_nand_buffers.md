---
title: "struct_nand_buffers(9)"
name: "struct_nand_buffers"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_nand_buffers/"
description: "struct_nand_buffers – buffer structure for read/write"
---

<p>struct_nand_buffers &#8211; buffer structure for read/write</p>
<h2>Synopsis</h2>
<pre><code>struct nand_buffers {
    uint8_t *ecccalc;
    uint8_t *ecccode;
    uint8_t *databuf;
};</code></pre>
<h2>Members</h2>
<p>ecccalc</p>
<dl>
<dd>buffer pointer for calculated ECC, size is oobsize.</dl>
<p> ecccode</p>
<dl>
<dd>buffer pointer for ECC read from flash, size is oobsize.</dl>
<p> databuf</p>
<dl>
<dd>buffer pointer for data, size is (page size + oobsize).</dl>
<h2>Description</h2>
<p>Do not change the order of buffers. databuf and oobrbuf must be in consecutive order.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
