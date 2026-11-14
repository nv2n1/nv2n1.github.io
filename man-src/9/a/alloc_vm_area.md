---
title: "alloc_vm_area(9)"
name: "alloc_vm_area"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_vm_area/"
---

alloc_vm_area - allocate a range of kernel address space

<h2>Synopsis</h2>

<pre><code>struct vm_struct *alloc_vm_area(size_t size, pte_t **ptes);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>size of the area</dl>
 

 <i>ptes</i>
<dl><dd>returns the PTEs for the address space</dl>

<h2>Return</h2>

NULL on failure, vm_struct on success 

 This function reserves a range of kernel address space, and allocates pagetables to map that range. No actual mappings are created. 

 If <i>ptes</i> is non-NULL, pointers to the PTEs (in init_mm) allocated for the VM area are returned.

<h2>Copyright</h2>


