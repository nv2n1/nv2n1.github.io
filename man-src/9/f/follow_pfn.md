---
title: "follow_pfn(9)"
name: "follow_pfn"
section: "9"
letter: "f"
url: "/docs/linux/man/9-follow_pfn/"
---

follow_pfn - look up PFN at a user virtual address

<h2>Synopsis</h2>

<pre><code>int follow_pfn(struct vm_area_struct *vma, unsigned long address, unsigned long *pfn);</code></pre>

<h2>Arguments</h2>

<i>vma</i>
<dl><dd><dd>memory mapping</dl>
 

 <i>address</i>
<dl><dd>user virtual address</dl>
 

 <i>pfn</i>
<dl><dd>location to store found PFN</dl>

<h2>Description</h2>

Only IO mappings and raw PFN mappings are allowed. 

 Returns zero and the pfn at <i>pfn</i> on success, -ve otherwise.

<h2>Copyright</h2>


