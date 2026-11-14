---
title: "ata_qc_complete_multiple(9)"
name: "ata_qc_complete_multiple"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_qc_complete_multiple/"
description: "ata_qc_complete_multiple – Complete multiple qcs successfully"
---

<p>ata_qc_complete_multiple &#8211; Complete multiple qcs successfully</p>
<h2>Synopsis</h2>
<pre><code>int ata_qc_complete_multiple(struct ata_port *ap, u32 qc_active);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>port in question</dl>
<p> <i>qc_active</i></p>
<dl>
<dd>new qc_active mask</dl>
<h2>Description</h2>
<p>Complete in-flight commands. This functions is meant to be called from low-level driver&#8217;s interrupt routine to complete requests normally. ap-&gt;qc_active and <i>qc_active</i> is compared and commands are completed accordingly. </p>
<p> Always use this function when completing multiple NCQ commands from IRQ handlers instead of calling <code>ata_qc_complete</code> multiple times to keep IRQ expect status properly in sync. </p>
<p> LOCKING: spin_lock_irqsave(host lock)</p>
<h2>Return</h2>
<p>Number of completed commands on success, -errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
