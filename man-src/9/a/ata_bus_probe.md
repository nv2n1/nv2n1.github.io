---
title: "ata_bus_probe(9)"
name: "ata_bus_probe"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_bus_probe/"
description: "ata_bus_probe – Reset and probe ATA bus"
---

<p>ata_bus_probe &#8211; Reset and probe ATA bus</p>
<h2>Synopsis</h2>
<pre><code>int ata_bus_probe(struct ata_port *ap);</code></pre>
<h2>Arguments</h2>
<p><i>ap</i></p>
<dl>
<dd>
<dd>Bus to probe</dl>
<h2>Description</h2>
<p>Master ATA bus probing function. Initiates a hardware-dependent bus reset, then attempts to identify any devices found on the bus. </p>
<p> LOCKING: PCI/etc. bus probe sem.</p>
<h2>Return</h2>
<p>Zero on success, negative errno otherwise.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
