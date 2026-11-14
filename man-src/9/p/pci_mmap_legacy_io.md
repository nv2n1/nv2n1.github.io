---
title: "pci_mmap_legacy_io(9)"
name: "pci_mmap_legacy_io"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_mmap_legacy_io/"
---

pci_mmap_legacy_io - map legacy PCI IO into user memory space

<h2>Synopsis</h2>

<pre><code>int pci_mmap_legacy_io(struct file *filp, struct kobject *kobj, struct bin_attribute *attr, struct vm_area_struct *vma);</code></pre>

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

Uses an arch specific callback, pci_mmap_legacy_io_page_range, to mmap legacy IO space (first meg of bus space) into application virtual memory space. Returns -ENOSYS if the operation isn't supported

<h2>Copyright</h2>


