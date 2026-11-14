---
title: "read_cache_page_gfp(9)"
name: "read_cache_page_gfp"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_cache_page_gfp/"
---

read_cache_page_gfp - read into page cache, using specified page allocation flags.

<h2>Synopsis</h2>

<pre><code>struct page *read_cache_page_gfp(struct address_space *mapping, pgoff_t index, gfp_t gfp);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the page's address_space</dl>
 

 <i>index</i>
<dl><dd>the page index</dl>
 

 <i>gfp</i>
<dl><dd>the page allocator flags to use if allocating</dl>

<h2>Description</h2>

This is the same as "read_mapping_page(mapping, index, NULL)", but with any new page allocations done using the specified allocation flags. 

 If the page does not get brought uptodate, return -EIO.

<h2>Copyright</h2>


