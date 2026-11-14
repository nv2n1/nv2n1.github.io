---
title: "remap_pfn_range(9)"
name: "remap_pfn_range"
section: "9"
letter: "r"
url: "/docs/linux/man/9-remap_pfn_range/"
---

remap_pfn_range - remap kernel memory to userspace

<h2>Synopsis</h2>

<pre><code>int remap_pfn_range(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, unsigned long size, pgprot_t prot);</code></pre>

<h2>Arguments</h2>

<i>vma</i>
<dl><dd><dd>user vma to map to</dl>
 

 <i>addr</i>
<dl><dd>target user address to start at</dl>
 

 <i>pfn</i>
<dl><dd>physical address of kernel memory</dl>
 

 <i>size</i>
<dl><dd>size of map area</dl>
 

 <i>prot</i>
<dl><dd>page protection flags for this mapping</dl>

<h2>Note</h2>

this is only safe if the mm semaphore is held when called.

<h2>Copyright</h2>


