---
title: "vm_map_ram(9)"
name: "vm_map_ram"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vm_map_ram/"
description: "vm_map_ram – map pages linearly into kernel virtual address (vmalloc space)"
---

<p>vm_map_ram &#8211; map pages linearly into kernel virtual address (vmalloc space)</p>
<h2>Synopsis</h2>
<pre><code>void *vm_map_ram(struct page **pages, unsigned int count, int node, pgprot_t prot);</code></pre>
<h2>Arguments</h2>
<p><i>pages</i></p>
<dl>
<dd>
<dd>an array of pointers to the pages to be mapped</dl>
<p> <i>count</i></p>
<dl>
<dd>number of pages</dl>
<p> <i>node</i></p>
<dl>
<dd>prefer to allocate data structures on this node</dl>
<p> <i>prot</i></p>
<dl>
<dd>memory protection to use. PAGE_KERNEL for regular RAM</dl>
<h2>Description</h2>
<p>If you use this function for less than VMAP_MAX_ALLOC pages, it could be faster than vmap so it&#8217;s good. But if you mix long-life and short-life objects with <code>vm_map_ram</code>, it could consume lots of address space through fragmentation (especially on a 32bit machine). You could see failures in the end. Please use this function for short-lived objects.</p>
<h2>Return</h2>
<p>a pointer to the address that has been mapped, or <code>NULL</code> on failure</p>
<h2>Copyright</h2>
