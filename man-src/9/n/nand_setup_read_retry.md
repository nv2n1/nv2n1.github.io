---
title: "nand_setup_read_retry(9)"
name: "nand_setup_read_retry"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_setup_read_retry/"
description: "nand_setup_read_retry – [INTERN] Set the READ RETRY mode"
---

<p>nand_setup_read_retry &#8211; [INTERN] Set the READ RETRY mode</p>
<h2>Synopsis</h2>
<pre><code>int nand_setup_read_retry(struct mtd_info *mtd, int retry_mode);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>MTD device structure</dl>
<p> <i>retry_mode</i></p>
<dl>
<dd>the retry mode to use</dl>
<h2>Description</h2>
<p>Some vendors supply a special command to shift the Vt threshold, to be used when there are too many bitflips in a page (i.e., ECC error). After setting a new threshold, the host should retry reading the page.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
