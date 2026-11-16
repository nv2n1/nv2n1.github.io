---
title: "add_to_page_cache_locked(9)"
name: "add_to_page_cache_locked"
section: "9"
letter: "a"
url: "/docs/linux/man/9-add_to_page_cache_locked/"
---

add_to_page_cache_locked - add a locked page to the pagecache

<h2>Synopsis</h2>

<pre><code>int add_to_page_cache_locked(struct page *page, struct address_space *mapping, pgoff_t offset, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd></dd><dd>page to add</dd></dl>
 

 <i>mapping</i>
<dl><dd>the page's address_space</dd></dl>
 

 <i>offset</i>
<dl><dd>page index</dd></dl>
 

 <i>gfp_mask</i>
<dl><dd>page allocation mode</dd></dl>

<h2>Description</h2>

This function is used to add a page to the pagecache. It must be locked. This function does not add the page to the LRU. The caller must do that.

<h2>Copyright</h2>


