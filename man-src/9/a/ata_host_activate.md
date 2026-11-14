---
title: "ata_host_activate(9)"
name: "ata_host_activate"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_activate/"
description: "ata_host_activate – start host, request IRQ and register it"
---

<p>ata_host_activate &#8211; start host, request IRQ and register it</p>
<h2>Synopsis</h2>
<pre><code>int ata_host_activate(struct ata_host *host, int irq, irq_handler_t irq_handler, unsigned long irq_flags, struct scsi_host_template *sht);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>target ATA host</dl>
<p> <i>irq</i></p>
<dl>
<dd>IRQ to request</dl>
<p> <i>irq_handler</i></p>
<dl>
<dd>irq_handler used when requesting IRQ</dl>
<p> <i>irq_flags</i></p>
<dl>
<dd>irq_flags used when requesting IRQ</dl>
<p> <i>sht</i></p>
<dl>
<dd>scsi_host_template to use when registering the host</dl>
<h2>Description</h2>
<p>After allocating an ATA host and initializing it, most libata LLDs perform three steps to activate the host &#8211; start host, request IRQ and register it. This helper takes necessary arguments and performs the three steps in one go. </p>
<p> An invalid IRQ skips the IRQ registration and expects the host to have set polling mode on the port. In this case, <i>irq_handler</i> should be NULL. </p>
<p> LOCKING: Inherited from calling layer (may sleep).</p>
<h2>Return</h2>
<p>0 on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
