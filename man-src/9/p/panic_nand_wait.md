---
title: "panic_nand_wait(9)"
name: "panic_nand_wait"
section: "9"
letter: "p"
url: "/docs/linux/man/9-panic_nand_wait/"
description: "panic_nand_wait – [GENERIC] wait until the command is done"
---

<p>panic_nand_wait &#8211; [GENERIC] wait until the command is done</p>
<h2>Synopsis</h2>
<pre><code>void panic_nand_wait(struct mtd_info *mtd, struct nand_chip *chip, unsigned long timeo);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>chip</i></p>
<dl>
<dd>NAND chip structure</dl>
<p> <i>timeo</i></p>
<dl>
<dd>timeout</dl>
<h2>Description</h2>
<p>Wait for command done. This is a helper function for nand_wait used when we are in interrupt context. May happen when in panic and trying to write an oops through mtdoops.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
