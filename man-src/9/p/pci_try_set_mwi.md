---
title: "pci_try_set_mwi(9)"
name: "pci_try_set_mwi"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_try_set_mwi/"
description: "pci_try_set_mwi – enables memory-write-invalidate PCI transaction"
---

<p>pci_try_set_mwi &#8211; enables memory-write-invalidate PCI transaction</p>
<h2>Synopsis</h2>
<pre><code>int pci_try_set_mwi(struct pci_dev *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the PCI device for which MWI is enabled</dl>
<h2>Description</h2>
<p>Enables the Memory-Write-Invalidate transaction in <code>PCI_COMMAND</code>. Callers are not required to check the return value.</p>
<h2>Return</h2>
<p>An appropriate -ERRNO error value on error, or zero for success.</p>
<h2>Copyright</h2>
