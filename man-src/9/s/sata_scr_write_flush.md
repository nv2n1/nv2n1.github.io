---
title: "sata_scr_write_flush(9)"
name: "sata_scr_write_flush"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_scr_write_flush/"
description: "sata_scr_write_flush – write SCR register of the specified port and flush"
---

<p>sata_scr_write_flush &#8211; write SCR register of the specified port and flush</p>
<h2>Synopsis</h2>
<pre><code>int sata_scr_write_flush(struct ata_link *link, int reg, u32 val);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to write SCR for</dl>
<p> <i>reg</i></p>
<dl>
<dd>SCR to write</dl>
<p> <i>val</i></p>
<dl>
<dd>value to write</dl>
<h2>Description</h2>
<p>This function is identical to <code>sata_scr_write</code> except that this function performs flush after writing to the register. </p>
<p> LOCKING: None if <i>link</i> is ap-&gt;link. Kernel thread context otherwise.</p>
<h2>Return</h2>
<p>0 on success, negative errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
