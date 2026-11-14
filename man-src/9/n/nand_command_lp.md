---
title: "nand_command_lp(9)"
name: "nand_command_lp"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_command_lp/"
description: "nand_command_lp – [DEFAULT] Send command to NAND large page device"
---

<p>nand_command_lp &#8211; [DEFAULT] Send command to NAND large page device</p>
<h2>Synopsis</h2>
<pre><code>void nand_command_lp(struct mtd_info *mtd, unsigned int command, int column, int page_addr);</code></pre>
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
<p>Send command to NAND device. This is the version for the new large page devices. We don&#8217;t have the separate regions as we have in the small page devices. We must emulate NAND_CMD_READOOB to keep the code compatible.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
