---
title: "ata_std_qc_defer(9)"
name: "ata_std_qc_defer"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_std_qc_defer/"
description: "ata_std_qc_defer – Check whether a qc needs to be deferred"
---

<p>ata_std_qc_defer &#8211; Check whether a qc needs to be deferred</p>
<h2>Synopsis</h2>
<pre><code>int ata_std_qc_defer(struct ata_queued_cmd *qc);</code></pre>
<h2>Arguments</h2>
<p><i>qc</i></p>
<dl>
<dd>
<dd>ATA command in question</dl>
<h2>Description</h2>
<p>Non-NCQ commands cannot run with any other command, NCQ or not. As upper layer only knows the queue depth, we are responsible for maintaining exclusion. This function checks whether a new command <i>qc</i> can be issued. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>ATA_DEFER_* if deferring is needed, 0 otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
