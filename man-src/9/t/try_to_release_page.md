---
title: "try_to_release_page(9)"
name: "try_to_release_page"
section: "9"
letter: "t"
url: "/docs/linux/man/9-try_to_release_page/"
---

try_to_release_page - release old fs-specific metadata on a page

<h2>Synopsis</h2>

<pre><code>int try_to_release_page(struct page *page, gfp_t gfp_mask);</code></pre>

<h2>Arguments</h2>

<i>page</i>
<dl><dd><dd>the page which the kernel is trying to free</dl>
 

 <i>gfp_mask</i>
<dl><dd>memory allocation flags (and I/O mode)</dl>

<h2>Description</h2>

The address_space is to try to release any data against the page (presumably at page-&gt;private). If the release was successful, return `1'. Otherwise return zero. 

 This may also be called if PG_fscache is set on a page, indicating that the page is known to the local caching routines. 

 The <i>gfp_mask</i> argument specifies whether I/O may be performed to release this page (__GFP_IO), and whether the call may block (__GFP_RECLAIM &amp; __GFP_FS).

<h2>Copyright</h2>


