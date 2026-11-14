---
title: "do_pata_set_dmamode(9)"
name: "do_pata_set_dmamode"
section: "9"
letter: "d"
url: "/docs/linux/man/9-do_pata_set_dmamode/"
description: "do_pata_set_dmamode – Initialize host controller PATA PIO timings"
---

<p>do_pata_set_dmamode &#8211; Initialize host controller PATA PIO timings</p>
<h2>Synopsis</h2>
<pre><code>void do_pata_set_dmamode(struct ata_port *ap, struct ata_device *adev, int isich);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Port whose timings we are configuring</dl>
<p> <i>adev</i></p>
<dl>
<dd>Drive in question</dl>
<p> <i>isich</i></p>
<dl>
<dd>set if the chip is an ICH device</dl>
<h2>Description</h2>
<p>Set UDMA mode for device, in host controller PCI config space. </p>
<p> LOCKING: None (inherited from caller).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
