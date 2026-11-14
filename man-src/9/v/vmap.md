---
title: "vmap(9)"
name: "vmap"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vmap/"
---

vmap - map an array of pages into virtually contiguous space

<h2>Synopsis</h2>

<pre><code>void *vmap(struct page **pages, unsigned int count, unsigned long flags, pgprot_t prot);</code></pre>

<h2>Arguments</h2>

<i>pages</i>
<dl><dd><dd>array of page pointers</dl>
 

 <i>count</i>
<dl><dd>number of pages to map</dl>
 

 <i>flags</i>
<dl><dd>vm_area-&gt;flags</dl>
 

 <i>prot</i>
<dl><dd>page protection for the mapping</dl>

<h2>Description</h2>

Maps <i>count</i> pages from <i>pages</i> into contiguous kernel virtual space.

<h2>Copyright</h2>


