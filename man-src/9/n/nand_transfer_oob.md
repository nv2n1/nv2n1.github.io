---
title: "nand_transfer_oob(9)"
name: "nand_transfer_oob"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_transfer_oob/"
description: "nand_transfer_oob – [INTERN] Transfer oob to client buffer"
---

<p>nand_transfer_oob &#8211; [INTERN] Transfer oob to client buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>uint8_t * nand_transfer_oob(struct mtd_info&nbsp;<wbr>*&nbsp;<wbr></code><i>mtd</i><code>, uint8_t&nbsp;<wbr>*&nbsp;<wbr></code><i>oob</i><code>, struct mtd_oob_ops&nbsp;<wbr>*&nbsp;<wbr></code><i>ops</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>mtd info structure</dl>
<p> <i>oob</i></p>
<dl>
<dd>oob destination address</dl>
<p> <i>ops</i></p>
<dl>
<dd>oob ops structure</dl>
<p> <i>len</i></p>
<dl>
<dd>size of oob to transfer</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
