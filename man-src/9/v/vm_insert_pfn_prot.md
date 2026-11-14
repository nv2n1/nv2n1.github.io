---
title: "vm_insert_pfn_prot(9)"
name: "vm_insert_pfn_prot"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_insert_pfn_prot/"
---

vm_insert_pfn_prot - insert single pfn into user vma with specified pgprot

<h2>Synopsis</h2>

<pre><code>int vm_insert_pfn_prot(struct vm_area_struct *vma, unsigned long addr, unsigned long pfn, pgprot_t pgprot);</code></pre>

<h2>Arguments</h2>

<i>vma</i>
<dl><dd><dd>user vma to map to</dl>
 

 <i>addr</i>
<dl><dd>target user address of this page</dl>
 

 <i>pfn</i>
<dl><dd>source kernel pfn</dl>
 

 <i>pgprot</i>
<dl><dd>pgprot flags for the inserted page</dl>

<h2>Description</h2>

This is exactly like vm_insert_pfn, except that it allows drivers to to override pgprot on a per-page basis. 

 This only makes sense for IO mappings, and it makes no sense for cow mappings. In general, using multiple vmas is preferable; vm_insert_pfn_prot should only be used if using multiple VMAs is impractical.

<h2>Copyright</h2>


