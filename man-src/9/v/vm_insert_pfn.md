---
title: "vm_insert_pfn(9)"
name: "vm_insert_pfn"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_insert_pfn/"
---

vm_insert_pfn - insert single pfn into user vma

<h2>Synopsis</h2>

<pre><code>int vm_insert_pfn(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn);</code></pre>

<h2>Arguments</h2>

<i>vma</i>
<dl><dd><dd>user vma to map to</dl>
 

 <i>addr</i>
<dl><dd>target user address of this page</dl>
 

 <i>pfn</i>
<dl><dd>source kernel pfn</dl>

<h2>Description</h2>

Similar to vm_insert_page, this allows drivers to insert individual pages they've allocated into a user vma. Same comments apply. 

 This function should only be called from a vm_ops-&gt;fault handler, and in that case the handler should return NULL. 

 vma cannot be a COW mapping. 

 As this is called only for pages that do not currently exist, we do not need to flush old virtual caches or the TLB.

<h2>Copyright</h2>


