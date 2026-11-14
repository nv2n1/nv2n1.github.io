---
title: "piix_check_450nx_errata(9)"
name: "piix_check_450nx_errata"
section: "9"
letter: "p"
url: "/docs/linux/man/9-piix_check_450nx_errata/"
description: "piix_check_450nx_errata – Check for problem 450NX setup"
---

<p>piix_check_450nx_errata &#8211; Check for problem 450NX setup</p>
<h2>Synopsis</h2>
<pre><code>int piix_check_450nx_errata(struct pci_dev *ata_dev);</code></pre>
<h2>Arguments</h2>
<p><i>ata_dev</i></p>
<dl>
<dd>
<dd>the PCI device to check</dl>
<h2>Description</h2>
<p>Check for the present of 450NX errata #19 and errata #25. If they are found return an error code so we can turn off DMA</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
