---
title: "nand_reset_data_interface(9)"
name: "nand_reset_data_interface"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_reset_data_interface/"
description: "nand_reset_data_interface – Reset data interface and timings"
---

<p>nand_reset_data_interface &#8211; Reset data interface and timings</p>
<h2>Synopsis</h2>
<pre><code>int nand_reset_data_interface(struct nand_chip *chip);</code></pre>
<h2>Arguments</h2>
<p><i>chip</i></p>
<dl>
<dd>
<dd>The NAND chip</dl>
<h2>Description</h2>
<p>Reset the Data interface and timings to ONFI mode 0. </p>
<p> Returns 0 for success or negative error code otherwise.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
