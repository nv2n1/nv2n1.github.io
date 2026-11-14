---
title: "page_cache_sync_readahead(9)"
name: "page_cache_sync_readahead"
section: "9"
letter: "p"
url: "/docs/linux/man/9-page_cache_sync_readahead/"
description: "page_cache_sync_readahead – generic file readahead"
---

<p>page_cache_sync_readahead &#8211; generic file readahead</p>
<h2>Synopsis</h2>
<pre><code>void page_cache_sync_readahead(struct address_space *mapping, struct file_ra_state *ra, struct file *filp, pgoff_t offset, unsigned long req_size);</code></pre>
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
<p> <i>offset</i></p>
<dl>
<dd>start offset into <i>mapping</i>, in pagecache page-sized units</dl>
<p> <i>req_size</i></p>
<dl>
<dd>hint: total size of the read which the caller is performing in pagecache pages</dl>
<h2>Description</h2>
<p><code>page_cache_sync_readahead</code> should be called when a cache miss happened: it will submit the read. The readahead logic may decide to piggyback more pages onto the read request if access patterns suggest it will improve performance.</p>
<h2>Copyright</h2>
