---
title: "nand_fill_oob(9)"
name: "nand_fill_oob"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_fill_oob/"
description: "nand_fill_oob – [INTERN] Transfer client buffer to oob"
---

<p>nand_fill_oob &#8211; [INTERN] Transfer client buffer to oob</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>uint8_t * nand_fill_oob(struct mtd_info&nbsp;<wbr>*&nbsp;<wbr></code><i>mtd</i><code>, uint8_t&nbsp;<wbr>*&nbsp;<wbr></code><i>oob</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>, struct mtd_oob_ops&nbsp;<wbr>*&nbsp;<wbr></code><i>ops</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>oob</i></p>
<dl>
<dd>oob data buffer</dl>
<p> <i>len</i></p>
<dl>
<dd>oob data write length</dl>
<p> <i>ops</i></p>
<dl>
<dd>oob ops structure</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
