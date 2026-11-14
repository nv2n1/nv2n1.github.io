---
title: "nand_wait_status_ready(9)"
name: "nand_wait_status_ready"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_wait_status_ready/"
description: "nand_wait_status_ready – [GENERIC] Wait for the ready status after commands."
---

<p>nand_wait_status_ready &#8211; [GENERIC] Wait for the ready status after commands.</p>
<h2>Synopsis</h2>
<pre><code>void nand_wait_status_ready(struct mtd_info *mtd, unsigned long timeo);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>timeo</i></p>
<dl>
<dd>Timeout in ms</dl>
<h2>Description</h2>
<p>Wait for status ready (i.e. command done) or timeout.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
