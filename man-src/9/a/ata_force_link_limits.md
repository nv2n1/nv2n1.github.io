---
title: "ata_force_link_limits(9)"
name: "ata_force_link_limits"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_force_link_limits/"
description: "ata_force_link_limits – force link limits according to libata.force"
---

<p>ata_force_link_limits &#8211; force link limits according to libata.force</p>
<h2>Synopsis</h2>
<pre><code>void ata_force_link_limits(struct ata_link *link);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link of interest</dl>
<h2>Description</h2>
<p>Force link flags and SATA spd limit according to libata.force and whine about it. When only the port part is specified (e.g. 1:), the limit applies to all links connected to both the host link and all fan-out ports connected via PMP. If the device part is specified as 0 (e.g. 1.00:), it specifies the first fan-out link not the host link. Device number 15 always points to the host link whether PMP is attached or not. If the controller has slave link, device number 16 points to it. </p>
<p> LOCKING: EH context.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
