---
title: "kmalloc(9)"
name: "kmalloc"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kmalloc/"
description: "kmalloc – allocate memory"
---

<p>kmalloc &#8211; allocate memory</p>
<h2>Synopsis</h2>
<pre><code>void *kmalloc(size_t size, gfp_t flags);</code></pre>
<h2>Arguments</h2>
<p><i>size</i></p>
<dl>
<dd>
<dd>how many bytes of memory are required.</dl>
<p> <i>flags</i></p>
<dl>
<dd>the type of memory to allocate.</dl>
<h2>Description</h2>
<p>kmalloc is the normal method of allocating memory for objects smaller than page size in the kernel. </p>
<p> The <i>flags</i> argument may be one of: </p>
<p> <code>GFP_USER</code> &#8211; Allocate memory on behalf of user. May sleep. </p>
<p> <code>GFP_KERNEL</code> &#8211; Allocate normal kernel ram. May sleep. </p>
<p> <code>GFP_ATOMIC</code> &#8211; Allocation will not sleep. May use emergency pools. For example, use this inside interrupt handlers. </p>
<p> <code>GFP_HIGHUSER</code> &#8211; Allocate pages from high memory. </p>
<p> <code>GFP_NOIO</code> &#8211; Do not do any I/O at all while trying to get memory. </p>
<p> <code>GFP_NOFS</code> &#8211; Do not make any fs calls while trying to get memory. </p>
<p> <code>GFP_NOWAIT</code> &#8211; Allocation will not sleep. </p>
<p> <code>__GFP_THISNODE</code> &#8211; Allocate node-local memory only. </p>
<p> <code>GFP_DMA</code> &#8211; Allocation suitable for DMA. Should only be used for <code>kmalloc</code> caches. Otherwise, use a slab created with SLAB_DMA. </p>
<p> Also it is possible to set different flags by OR&#8217;ing in one or more of the following additional <i>flags</i>: </p>
<p> <code>__GFP_COLD</code> &#8211; Request cache-cold pages instead of trying to return cache-warm pages. </p>
<p> <code>__GFP_HIGH</code> &#8211; This allocation has high priority and may use emergency pools. </p>
<p> <code>__GFP_NOFAIL</code> &#8211; Indicate that this allocation is in no way allowed to fail (think twice before using). </p>
<p> <code>__GFP_NORETRY</code> &#8211; If memory is not immediately available, then give up at once. </p>
<p> <code>__GFP_NOWARN</code> &#8211; If allocation fails, don&#8217;t issue any warnings. </p>
<p> <code>__GFP_REPEAT</code> &#8211; If allocation fails initially, try once more before failing. </p>
<p> There are other flags available as well, but these are not intended for general use, and so are not documented here. For a full list of potential flags, always refer to linux/gfp.h.</p>
<h2>Copyright</h2>
