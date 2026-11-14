---
title: "piix_set_piomode(9)"
name: "piix_set_piomode"
section: "9"
letter: "p"
url: "/docs/linux/man/9-piix_set_piomode/"
description: "piix_set_piomode – Initialize host controller PATA PIO timings"
---

<p>piix_set_piomode &#8211; Initialize host controller PATA PIO timings</p>
<h2>Synopsis</h2>
<pre><code>void piix_set_piomode(struct ata_port *ap, struct ata_device *adev);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Port whose timings we are configuring</dl>
<p> <i>adev</i></p>
<dl>
<dd>Drive in question</dl>
<h2>Description</h2>
<p>Set PIO mode for device, in host controller PCI config space. </p>
<p> LOCKING: None (inherited from caller).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
