---
title: "page_cache_async_readahead(9)"
name: "page_cache_async_readahead"
section: "9"
letter: "p"
url: "/docs/linux/man/9-page_cache_async_readahead/"
description: "page_cache_async_readahead – file readahead for marked pages"
---

<p>page_cache_async_readahead &#8211; file readahead for marked pages</p>
<h2>Synopsis</h2>
<pre><code>void page_cache_async_readahead(struct address_space *mapping, struct file_ra_state *ra, struct file *filp, struct page *page, pgoff_t offset, unsigned long req_size);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>address_space which holds the pagecache and I/O vectors</dl>
<p> <i>ra</i></p>
<dl>
<dd>file_ra_state which holds the readahead state</dl>
<p> <i>filp</i></p>
<dl>
<dd>passed on to -&gt;<code>readpage</code> and -&gt;<code>readpages</code></dl>
<p> <i>page</i></p>
<dl>
<dd>the page at <i>offset</i> which has the PG_readahead flag set</dl>
<p> <i>offset</i></p>
<dl>
<dd>start offset into <i>mapping</i>, in pagecache page-sized units</dl>
<p> <i>req_size</i></p>
<dl>
<dd>hint: total size of the read which the caller is performing in pagecache pages</dl>
<h2>Description</h2>
<p><code>page_cache_async_readahead</code> should be called when a page is used which has the PG_readahead flag; this is a marker to suggest that the application has used up enough of the readahead window that we should start pulling in more pages.</p>
<h2>Copyright</h2>
