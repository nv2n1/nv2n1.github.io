---
title: "pci_set_cacheline_size(9)"
name: "pci_set_cacheline_size"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_set_cacheline_size/"
---

pci_set_cacheline_size - ensure the CACHE_LINE_SIZE register is programmed

<h2>Synopsis</h2>

<pre><code>int pci_set_cacheline_size(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device for which MWI is to be enabled</dl>

<h2>Description</h2>

Helper function for pci_set_mwi. Originally copied from drivers/net/acenic.c. Copyright 1998-2001 by Jes Sorensen, &lt;jes<i>trained</i>-monkey.org&gt;.

<h2>Return</h2>

An appropriate -ERRNO error value on error, or zero for success.

<h2>Copyright</h2>


