---
title: "vm_iomap_memory(9)"
name: "vm_iomap_memory"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_iomap_memory/"
description: "vm_iomap_memory – remap memory to userspace"
---

<p>vm_iomap_memory &#8211; remap memory to userspace</p>
<h2>Synopsis</h2>
<pre><code>int vm_iomap_memory(struct vm_area_struct *vma, phys_addr_t start, unsigned long len);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>user vma to map to</dl>
<p> <i>start</i></p>
<dl>
<dd>start of area</dl>
<p> <i>len</i></p>
<dl>
<dd>size of area</dl>
<h2>Description</h2>
<p>This is a simplified <code>io_remap_pfn_range</code> for common driver use. The driver just needs to give us the physical memory range to be mapped, we&#8217;ll figure out the rest from the vma information. </p>
<p> NOTE! Some drivers might want to tweak vma-&gt;vm_page_prot first to get whatever write-combining details or similar.</p>
<h2>Copyright</h2>
