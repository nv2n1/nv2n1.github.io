---
title: "remap_vmalloc_range_partial(9)"
name: "remap_vmalloc_range_partial"
section: "9"
letter: "r"
url: "/docs/linux/man/9-remap_vmalloc_range_partial/"
description: "remap_vmalloc_range_partial – map vmalloc pages to userspace"
---

<p>remap_vmalloc_range_partial &#8211; map vmalloc pages to userspace</p>
<h2>Synopsis</h2>
<pre><code>int remap_vmalloc_range_partial(struct vm_area_struct *vma, unsigned long uaddr, void *kaddr, unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>vma to cover</dl>
<p> <i>uaddr</i></p>
<dl>
<dd>target user address to start at</dl>
<p> <i>kaddr</i></p>
<dl>
<dd>virtual address of vmalloc kernel memory</dl>
<p> <i>size</i></p>
<dl>
<dd>size of map area</dl>
<h2>Return</h2>
<p>0 for success, -Exxx on failure </p>
<p> This function checks that <i>kaddr</i> is a valid vmalloc&#8217;ed area, and that it is big enough to cover the range starting at <i>uaddr</i> in <i>vma</i>. Will return failure if that criteria isn&#8217;t met. </p>
<p> Similar to <code>remap_pfn_range</code> (see mm/memory.c)</p>
<h2>Copyright</h2>
