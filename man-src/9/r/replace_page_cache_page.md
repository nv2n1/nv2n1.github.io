---
title: "replace_page_cache_page(9)"
name: "replace_page_cache_page"
section: "9"
letter: "r"
url: "/docs/linux/man/9-replace_page_cache_page/"
---

replace_page_cache_page - replace a pagecache page with a new one

<h2>Synopsis</h2>

<pre><code>int replace_page_cache_page(struct page *old, struct page *new, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>old</i>
<dl><dd><dd>page to be replaced</dl>
 

 <i>new</i>
<dl><dd>page to replace with</dl>
 

 <i>gfp_mask</i>
<dl><dd>allocation mode</dl>

<h2>Description</h2>

This function replaces a page in the pagecache with a new one. On success it acquires the pagecache reference for the new page and drops it for the old page. Both the old and new pages must be locked. This function does not add the new page to the LRU, the caller must do that. 

 The remove + add is atomic. The only way this function can fail is memory allocation failure.

<h2>Copyright</h2>


