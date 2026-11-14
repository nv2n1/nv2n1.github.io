---
title: "nand_release_device(9)"
name: "nand_release_device"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_release_device/"
description: "nand_release_device – [GENERIC] release chip"
---

<p>nand_release_device &#8211; [GENERIC] release chip</p>
<h2>Synopsis</h2>
<pre><code>void nand_release_device(struct mtd_info *mtd);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<h2>Description</h2>
<p>Release chip lock and wake up anyone waiting on the device.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
