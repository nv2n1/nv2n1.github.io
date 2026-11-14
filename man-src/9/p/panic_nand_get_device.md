---
title: "panic_nand_get_device(9)"
name: "panic_nand_get_device"
section: "9"
letter: "p"
url: "/docs/linux/man/9-panic_nand_get_device/"
description: "panic_nand_get_device – [GENERIC] Get chip for selected access"
---

<p>panic_nand_get_device &#8211; [GENERIC] Get chip for selected access</p>
<h2>Synopsis</h2>
<pre><code>void panic_nand_get_device(struct nand_chip *chip, struct mtd_info *mtd, int new_state);</code></pre>
<h2>Arguments</h2>
<p><i>chip</i></p>
<dl>
<dd>
<dd>the nand chip descriptor</dl>
<p> <i>mtd</i></p>
<dl>
<dd>MTD device structure</dl>
<p> <i>new_state</i></p>
<dl>
<dd>the state which is requested</dl>
<h2>Description</h2>
<p>Used when in panic, no locks are taken.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
