---
title: "pci_mmap_legacy_mem(9)"
name: "pci_mmap_legacy_mem"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_mmap_legacy_mem/"
---

pci_mmap_legacy_mem - map legacy PCI memory into user memory space

<h2>Synopsis</h2>

<pre><code>int pci_mmap_legacy_mem(struct file *filp, struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma);</code></pre>

<h2>Arguments</h2>

<i>filp</i>
<dl><dd><dd>open sysfs file</dl>
 

 <i>kobj</i>
<dl><dd>kobject corresponding to device to be mapped</dl>
 

 <i>attr</i>
<dl><dd>struct bin_attribute for this file</dl>
 

 <i>vma</i>
<dl><dd>struct vm_area_struct passed to mmap</dl>

<h2>Description</h2>

Uses an arch specific callback, pci_mmap_legacy_mem_page_range, to mmap legacy memory space (first meg of bus space) into application virtual memory space.

<h2>Copyright</h2>


