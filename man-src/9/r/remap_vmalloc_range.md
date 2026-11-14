---
title: "remap_vmalloc_range(9)"
name: "remap_vmalloc_range"
section: "9"
letter: "r"
url: "/docs/linux/man/9-remap_vmalloc_range/"
description: "remap_vmalloc_range – map vmalloc pages to userspace"
---

<p>remap_vmalloc_range &#8211; map vmalloc pages to userspace</p>
<h2>Synopsis</h2>
<pre><code>int remap_vmalloc_range(struct vm_area_struct *vma, void *addr, unsigned long pgoff);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>vma to cover (map full range of vma)</dl>
<p> <i>addr</i></p>
<dl>
<dd>vmalloc memory</dl>
<p> <i>pgoff</i></p>
<dl>
<dd>number of pages into addr before first page to map</dl>
<h2>Return</h2>
<p>0 for success, -Exxx on failure </p>
<p> This function checks that addr is a valid vmalloc&#8217;ed area, and that it is big enough to cover the vma. Will return failure if that criteria isn&#8217;t met. </p>
<p> Similar to <code>remap_pfn_range</code> (see mm/memory.c)</p>
<h2>Copyright</h2>
