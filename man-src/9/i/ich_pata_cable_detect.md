---
title: "ich_pata_cable_detect(9)"
name: "ich_pata_cable_detect"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ich_pata_cable_detect/"
description: "ich_pata_cable_detect – Probe host controller cable detect info"
---

<p>ich_pata_cable_detect &#8211; Probe host controller cable detect info</p>
<h2>Synopsis</h2>
<pre><code>int ich_pata_cable_detect(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Port for which cable detect info is desired</dl>
<h2>Description</h2>
<p>Read 80c cable indicator from ATA PCI device&#8217;s PCI config register. This register is normally set by firmware (BIOS). </p>
<p> LOCKING: None (inherited from caller).</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
