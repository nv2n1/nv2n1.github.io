---
title: "nand_get_device(9)"
name: "nand_get_device"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_get_device/"
description: "nand_get_device – [GENERIC] Get chip for selected access"
---

<p>nand_get_device &#8211; [GENERIC] Get chip for selected access</p>
<h2>Synopsis</h2>
<pre><code>int nand_get_device(struct mtd_info *mtd, int new_state);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>new_state</i></p>
<dl>
<dd>the state which is requested</dl>
<h2>Description</h2>
<p>Get the device and lock it for exclusive access</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
