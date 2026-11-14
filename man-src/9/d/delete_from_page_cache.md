---
title: "delete_from_page_cache(9)"
name: "delete_from_page_cache"
section: "9"
letter: "d"
url: "/docs/linux/man/9-delete_from_page_cache/"
---

delete_from_page_cache - delete page from page cache

<h2>Synopsis</h2>

<pre><code>void delete_from_page_cache(struct page *page);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd><dd>the page which the kernel is trying to remove from page cache</dl>

<h2>Description</h2>

This must be called only on pages that have been verified to be in the page cache and locked. It will never put the page into the free list, the caller has a reference on the page.

<h2>Copyright</h2>


