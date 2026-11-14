---
title: "ata_qc_issue(9)"
name: "ata_qc_issue"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_qc_issue/"
description: "ata_qc_issue – issue taskfile to device"
---

<p>ata_qc_issue &#8211; issue taskfile to device</p>
<h2>Synopsis</h2>
<pre><code>void ata_qc_issue(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>command to issue to device</dl>
<h2>Description</h2>
<p>Prepare an ATA command to submission to device. This includes mapping the data into a DMA-able area, filling in the S/G table, and finally writing the taskfile to hardware, starting the command. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
