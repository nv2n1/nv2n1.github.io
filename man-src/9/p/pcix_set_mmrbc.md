---
title: "pcix_set_mmrbc(9)"
name: "pcix_set_mmrbc"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcix_set_mmrbc/"
---

pcix_set_mmrbc - set PCI-X maximum memory read byte count

<h2>Synopsis</h2>

<pre><code>int pcix_set_mmrbc(struct pci_dev *dev, int mmrbc);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>
 

 <i>mmrbc</i>
<dl><dd>maximum memory read count in bytes valid values are 512, 1024, 2048, 4096</dl>

<h2>Description</h2>

If possible sets maximum memory read byte count, some bridges have erratas that prevent this.

<h2>Copyright</h2>


