---
title: "sata_scr_write(9)"
name: "sata_scr_write"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_scr_write/"
description: "sata_scr_write – write SCR register of the specified port"
---

<p>sata_scr_write &#8211; write SCR register of the specified port</p>
<h2>Synopsis</h2>
<pre><code>int sata_scr_write(struct ata_link *link, int reg, u32 val);</code></pre>
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
<p>Write <i>val</i> to SCR register <i>reg</i> of <i>link</i>. This function is guaranteed to succeed if <i>link</i> is ap-&gt;link, the cable type of the port is SATA and the port implements -&gt;scr_read. </p>
<p> LOCKING: None if <i>link</i> is ap-&gt;link. Kernel thread context otherwise.</p>
<h2>Return</h2>
<p>0 on success, negative errno on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
