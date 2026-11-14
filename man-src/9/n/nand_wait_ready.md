---
title: "nand_wait_ready(9)"
name: "nand_wait_ready"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_wait_ready/"
description: "nand_wait_ready – [GENERIC] Wait for the ready pin after commands."
---

<p>nand_wait_ready &#8211; [GENERIC] Wait for the ready pin after commands.</p>
<h2>Synopsis</h2>
<pre><code>void nand_wait_ready(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>Wait for the ready pin after a command, and warn if a timeout occurs.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
