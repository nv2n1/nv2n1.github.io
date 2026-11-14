---
title: "zap_page_range(9)"
name: "zap_page_range"
section: "9"
letter: "z"
url: "/docs/linux/man/9-zap_page_range/"
description: "zap_page_range – remove user pages in a given range"
---

<p>zap_page_range &#8211; remove user pages in a given range</p>
<h2>Synopsis</h2>
<pre><code>void zap_page_range(struct vm_area_struct *vma, unsigned long start, unsigned long size, struct zap_details *details);</code></pre>
<h2>Arguments</h2>
<p><i>vma</i></p>
<dl>
<dd>
<dd>vm_area_struct holding the applicable pages</dl>
<p> <i>start</i></p>
<dl>
<dd>starting address of pages to zap</dl>
<p> <i>size</i></p>
<dl>
<dd>number of bytes to zap</dl>
<p> <i>details</i></p>
<dl>
<dd>details of shared cache invalidation</dl>
<h2>Description</h2>
<p>Caller must protect the VMA list</p>
<h2>Copyright</h2>


