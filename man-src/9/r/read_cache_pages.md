---
title: "read_cache_pages(9)"
name: "read_cache_pages"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_cache_pages/"
---

read_cache_pages - populate an address space with some pages &amp; start reads against them

<h2>Synopsis</h2>

<pre><code>int read_cache_pages(struct address_space *mapping, struct list_head *pages, int (*filler)(void *, struct page *), void *data);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the address_space</dl>
 

 <i>pages</i>
<dl><dd>The address of a list_head which contains the target pages. These pages have their -&gt;index populated and are otherwise uninitialised.</dl>
 

 <i>filler</i>
<dl><dd>callback routine for filling a single page.</dl>
 

 <i>data</i>
<dl><dd>private data for the callback routine.</dl>

<h2>Description</h2>

Hides the details of the LRU cache etc from the filesystems.

<h2>Copyright</h2>


