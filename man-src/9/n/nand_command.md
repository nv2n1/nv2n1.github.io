---
title: "nand_command(9)"
name: "nand_command"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_command/"
description: "nand_command – [DEFAULT] Send command to NAND device"
---

<p>nand_command &#8211; [DEFAULT] Send command to NAND device</p>
<h2>Synopsis</h2>
<pre><code>void nand_command(struct mtd_info *mtd, unsigned int command, int column, int page_addr);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>command</i></p>
<dl>
<dd>the command to be sent</dl>
<p> <i>column</i></p>
<dl>
<dd>the column address for this command, -1 if none</dl>
<p> <i>page_addr</i></p>
<dl>
<dd>the page address for this command, -1 if none</dl>
<h2>Description</h2>
<p>Send command to NAND device. This function is used for small page devices (512 Bytes per page).</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
