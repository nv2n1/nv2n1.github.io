---
title: "mpage_writepages(9)"
name: "mpage_writepages"
section: "9"
letter: "m"
url: "/docs/linux/man/9-mpage_writepages/"
description: "mpage_writepages – walk the list of dirty pages of the given address space & writepage all of them"
---

<p>mpage_writepages &#8211; walk the list of dirty pages of the given address space &amp; <code>writepage</code> all of them</p>
<h2>Synopsis</h2>
<pre><code>int mpage_writepages(struct address_space *mapping, struct writeback_control *wbc, get_block_t get_block);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>address space structure to write</dl>
<p> <i>wbc</i></p>
<dl>
<dd>subtract the number of written pages from *<i>wbc</i>-&gt;nr_to_write</dl>
<p> <i>get_block</i></p>
<dl>
<dd>the filesystem&#8217;s block mapper function. If this is NULL then use a_ops-&gt;writepage. Otherwise, go direct-to-BIO.</dl>
<h2>Description</h2>
<p>This is a library function, which implements the <code>writepages</code> address_space_operation. </p>
<p> If a page is already under I/O, <code>generic_writepages</code> skips it, even if it&#8217;s dirty. This is desirable behaviour for memory-cleaning writeback, but it is INCORRECT for data-integrity system calls such as <code>fsync</code>. <code>fsync</code> and <code>msync</code> need to guarantee that all the data which was dirty at the time the call was made get new I/O started against them. If wbc-&gt;sync_mode is WB_SYNC_ALL then we were called for data integrity and we must wait for existing IO to complete.</p>
<h2>Copyright</h2>
