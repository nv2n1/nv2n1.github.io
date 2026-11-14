---
title: "panic_nand_wait_ready(9)"
name: "panic_nand_wait_ready"
section: "9"
letter: "p"
url: "/docs/linux/man/9-panic_nand_wait_ready/"
description: "panic_nand_wait_ready – [GENERIC] Wait for the ready pin after commands."
---

<p>panic_nand_wait_ready &#8211; [GENERIC] Wait for the ready pin after commands.</p>
<h2>Synopsis</h2>
<pre><code>void panic_nand_wait_ready(struct mtd_info *mtd, unsigned long timeo);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>timeo</i></p>
<dl>
<dd>Timeout</dl>
<h2>Description</h2>
<p>Helper function for nand_wait_ready used when needing to wait in interrupt context.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
