---
title: "ata_sas_port_alloc(9)"
name: "ata_sas_port_alloc"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_sas_port_alloc/"
description: "ata_sas_port_alloc – Allocate port for a SAS attached SATA device"
---

<p>ata_sas_port_alloc &#8211; Allocate port for a SAS attached SATA device</p>
<h2>Synopsis</h2>
<pre><code>struct ata_port *ata_sas_port_alloc(struct ata_host *host, struct ata_port_info *port_info, struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>ATA host container for all SAS ports</dl>
<p> <i>port_info</i></p>
<dl>
<dd>Information from low-level host driver</dl>
<p> <i>shost</i></p>
<dl>
<dd>SCSI host that the scsi device is attached to</dl>
<h2>Description</h2>
<p>LOCKING: PCI/etc. bus probe sem.</p>
<h2>Return</h2>
<p>ata_port pointer on success / NULL on failure.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
