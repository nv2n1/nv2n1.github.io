---
title: "sata_print_link_status(9)"
name: "sata_print_link_status"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_print_link_status/"
description: "sata_print_link_status – Print SATA link status"
---

<p>sata_print_link_status &#8211; Print SATA link status</p>
<h2>Synopsis</h2>
<pre><code>void sata_print_link_status(struct ata_link *link);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>SATA link to printk link status about</dl>
<h2>Description</h2>
<p>This function prints link speed and status of a SATA link. </p>
<p> LOCKING: None.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
