---
title: "write_cache_pages(9)"
name: "write_cache_pages"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_cache_pages/"
description: "write_cache_pages – walk the list of dirty pages of the given address space and write all of them."
---

<p>write_cache_pages &#8211; walk the list of dirty pages of the given address space and write all of them.</p>
<h2>Synopsis</h2>
<pre><code>int write_cache_pages(struct address_space *mapping, struct writeback_control *wbc, writepage_t writepage, void *data);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>address space structure to write</dl>
<p> <i>wbc</i></p>
<dl>
<dd>subtract the number of written pages from *<i>wbc</i>-&gt;nr_to_write</dl>
<p> <i>writepage</i></p>
<dl>
<dd>function called for each page</dl>
<p> <i>data</i></p>
<dl>
<dd>data passed to writepage function</dl>
<h2>Description</h2>
<p>If a page is already under I/O, <code>write_cache_pages</code> skips it, even if it&#8217;s dirty. This is desirable behaviour for memory-cleaning writeback, but it is INCORRECT for data-integrity system calls such as <code>fsync</code>. <code>fsync</code> and <code>msync</code> need to guarantee that all the data which was dirty at the time the call was made get new I/O started against them. If wbc-&gt;sync_mode is WB_SYNC_ALL then we were called for data integrity and we must wait for existing IO to complete. </p>
<p> To avoid livelocks (when other process dirties new pages), we first tag pages which should be written back with TOWRITE tag and only then start writing them. For data-integrity sync we have to be careful so that we do not miss some pages (e.g., because some other process has cleared TOWRITE tag we set). The rule we follow is that TOWRITE tag can be cleared only by the process clearing the DIRTY tag (and submitting the page for IO).</p>
<h2>Copyright</h2>
