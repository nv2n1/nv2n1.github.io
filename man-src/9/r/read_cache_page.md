---
title: "read_cache_page(9)"
name: "read_cache_page"
section: "9"
letter: "r"
url: "/docs/linux/man/9-read_cache_page/"
description: "read_cache_page – read into page cache, fill it if needed"
---

<p>read_cache_page &#8211; read into page cache, fill it if needed</p>
<h2>Synopsis</h2>
<pre><code>struct page *read_cache_page(struct address_space *mapping, pgoff_t index, int (*filler)(void *, struct page *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the page&#8217;s address_space</dl>
<p> <i>index</i></p>
<dl>
<dd>the page index</dl>
<p> <i>filler</i></p>
<dl>
<dd>function to perform the read</dl>
<p> <i>data</i></p>
<dl>
<dd>first arg to filler(data, page) function, often left as NULL</dl>
<h2>Description</h2>
<p>Read into the page cache. If a page already exists, and <code>PageUptodate</code> is not set, try to fill the page and wait for it to become unlocked. </p>
<p> If the page does not get brought uptodate, return -EIO.</p>
<h2>Copyright</h2>
