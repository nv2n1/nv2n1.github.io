---
title: "pci_adjust_legacy_attr(9)"
name: "pci_adjust_legacy_attr"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_adjust_legacy_attr/"
---

pci_adjust_legacy_attr - adjustment of legacy file attributes

<h2>Synopsis</h2>

<pre><code>void pci_adjust_legacy_attr(struct pci_bus *b, enum pci_mmap_state mmap_type);</code></pre>

<h2>Arguments</h2>

<i>b</i>
<dl><dd><dd>bus to create files under</dl>
 

 <i>mmap_type</i>
<dl><dd>I/O port or memory</dl>

<h2>Description</h2>

Stub implementation. Can be overridden by arch if necessary.

<h2>Copyright</h2>


