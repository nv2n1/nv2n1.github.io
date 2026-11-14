---
title: "alloc_pages_exact_nid(9)"
name: "alloc_pages_exact_nid"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_pages_exact_nid/"
description: "alloc_pages_exact_nid – allocate an exact number of physically-contiguous pages on a node."
---

<p>alloc_pages_exact_nid &#8211; allocate an exact number of physically-contiguous pages on a node.</p>
<h2>Synopsis</h2>
<pre><code>void *alloc_pages_exact_nid(int nid, size_t size, gfp_t gfp_mask);</code></pre>
<h2>Arguments</h2>
<p><i>nid</i></p>
<dl>
<dd>
<dd>the preferred node ID where memory should be allocated</dl>
<p> <i>size</i></p>
<dl>
<dd>the number of bytes to allocate</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>GFP flags for the allocation</dl>
<h2>Description</h2>
<p>Like <code>alloc_pages_exact</code>, but try to allocate on node nid first before falling back.</p>
<h2>Copyright</h2>
