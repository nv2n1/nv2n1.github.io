---
title: "nand_init_data_interface(9)"
name: "nand_init_data_interface"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_init_data_interface/"
description: "nand_init_data_interface – find the best data interface and timings"
---

<p>nand_init_data_interface &#8211; find the best data interface and timings</p>
<h2>Synopsis</h2>
<pre><code>int nand_init_data_interface(struct nand_chip *chip);</code></pre>
<h2>Arguments</h2>
<p><i>chip</i></p>
<dl>
<dd>
<dd>The NAND chip</dl>
<h2>Description</h2>
<p>Find the best data interface and NAND timings supported by the chip and the driver. First tries to retrieve supported timing modes from ONFI information, and if the NAND chip does not support ONFI, relies on the -&gt;onfi_timing_mode_default specified in the nand_ids table. After this function nand_chip-&gt;data_interface is initialized with the best timing mode available. </p>
<p> Returns 0 for success or negative error code otherwise.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
