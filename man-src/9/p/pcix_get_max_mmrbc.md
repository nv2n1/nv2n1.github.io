---
title: "pcix_get_max_mmrbc(9)"
name: "pcix_get_max_mmrbc"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pcix_get_max_mmrbc/"
---

pcix_get_max_mmrbc - get PCI-X maximum designed memory read byte count

<h2>Synopsis</h2>

<pre><code>int pcix_get_max_mmrbc(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>PCI device to query</dl>

<h2>Description</h2>

Returns mmrbc: maximum designed memory read count in bytes or appropriate error value.

<h2>Copyright</h2>


