---
title: "ata_scsi_report_zones_complete(9)"
name: "ata_scsi_report_zones_complete"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_scsi_report_zones_complete/"
description: "ata_scsi_report_zones_complete – convert ATA output"
---

<p>ata_scsi_report_zones_complete &#8211; convert ATA output</p>
<h2>Synopsis</h2>
<pre><code>void ata_scsi_report_zones_complete(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>command structure returning the data</dl>
<h2>Description</h2>
<p>Convert T-13 little-endian field representation into T-10 big-endian field representation. What a mess.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
