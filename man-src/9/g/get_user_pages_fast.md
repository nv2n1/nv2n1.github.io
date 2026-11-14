---
title: "get_user_pages_fast(9)"
name: "get_user_pages_fast"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_user_pages_fast/"
description: "get_user_pages_fast – pin user pages in memory"
---

<p>get_user_pages_fast &#8211; pin user pages in memory</p>
<h2>Synopsis</h2>
<pre><code>int get_user_pages_fast(unsigned long start, int nr_pages, int write, struct page **pages);</code></pre>
<h2>Arguments</h2>
<p><i>start</i></p>
<dl>
<dd>
<dd>starting user address</dl>
<p> <i>nr_pages</i></p>
<dl>
<dd>number of pages from start to pin</dl>
<p> <i>write</i></p>
<dl>
<dd>whether pages will be written to</dl>
<p> <i>pages</i></p>
<dl>
<dd>array that receives pointers to the pages pinned. Should be at least nr_pages long.</dl>
<h2>Description</h2>
<p>Returns number of pages pinned. This may be fewer than the number requested. If nr_pages is 0 or negative, returns 0. If no pages were pinned, returns -errno. </p>
<p> get_user_pages_fast provides equivalent functionality to get_user_pages, operating on current and current-&gt;mm, with force=0 and vma=NULL. However unlike get_user_pages, it must be called without mmap_sem held. </p>
<p> get_user_pages_fast may take mmap_sem and page table locks, so no assumptions can be made about lack of locking. get_user_pages_fast is to be implemented in a way that is advantageous (vs <code>get_user_pages</code>) when the user memory area is already faulted in and present in ptes. However if the pages have to be faulted in, it may turn out to be slightly slower so callers need to carefully consider what to use. On many architectures, get_user_pages_fast simply falls back to get_user_pages.</p>
<h2>Copyright</h2>
