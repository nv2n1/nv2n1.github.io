---
title: "pci_mmap_resource(9)"
name: "pci_mmap_resource"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_mmap_resource/"
---

pci_mmap_resource - map a PCI resource into user memory space

<h2>Synopsis</h2>

<pre><code>int pci_mmap_resource(struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma, int write_combine);</code></pre>

<h2>Arguments</h2>

<i>kobj</i>
<dl><dd><dd>kobject for mapping</dl>
 

 <i>attr</i>
<dl><dd>struct bin_attribute for the file being mapped</dl>
 

 <i>vma</i>
<dl><dd>struct vm_area_struct passed into the mmap</dl>
 

 <i>write_combine</i>
<dl><dd>1 for write_combine mapping</dl>

<h2>Description</h2>

Use the regular PCI mapping routines to map a PCI resource into userspace.

<h2>Copyright</h2>


