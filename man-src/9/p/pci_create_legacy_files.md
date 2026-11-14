---
title: "pci_create_legacy_files(9)"
name: "pci_create_legacy_files"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_create_legacy_files/"
---

pci_create_legacy_files - create legacy I/O port and memory files

<h2>Synopsis</h2>

<pre><code>void pci_create_legacy_files(struct pci_bus *b);</code></pre>

<h2>Arguments</h2>

<i>b</i>
<dl><dd><dd>bus to create files under</dl>

<h2>Description</h2>

Some platforms allow access to legacy I/O port and ISA memory space on a per-bus basis. This routine creates the files and ties them into their associated read, write and mmap files from pci-sysfs.c 

 On error unwind, but don't propagate the error to the caller as it is ok to set up the PCI bus without these files.

<h2>Copyright</h2>


