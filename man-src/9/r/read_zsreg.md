---
title: "read_zsreg(9)"
name: "read_zsreg"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_zsreg/"
description: "read_zsreg – Read a register from a Z85230"
---

<p>read_zsreg &#8211; Read a register from a Z85230</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 read_zsreg(struct z8530_channel&nbsp;<wbr>*&nbsp;<wbr></code><i>c</i><code>, u8&nbsp;<wbr></code><i>reg</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>c</i></p>
<dl>
<dd>
<dd>Z8530 channel to read from (2 per chip)</dl>
<p> <i>reg</i></p>
<dl>
<dd>Register to read FIXME: Use a spinlock. </p>
<p> Most of the Z8530 registers are indexed off the control registers. A read is done by writing to the control register and reading the register back. The caller must hold the lock</dl>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
