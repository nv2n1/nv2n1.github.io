---
title: "pci_enable_sriov(9)"
name: "pci_enable_sriov"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_enable_sriov/"
---

pci_enable_sriov - enable the SR-IOV capability

<h2>Synopsis</h2>

<pre><code>int pci_enable_sriov(struct pci_dev *dev, int nr_virtfn);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device</dl>
 

 <i>nr_virtfn</i>
<dl><dd>number of virtual functions to enable</dl>

<h2>Description</h2>

Returns 0 on success, or negative on failure.

<h2>Copyright</h2>


