---
title: "pagecache_isize_extended(9)"
name: "pagecache_isize_extended"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pagecache_isize_extended/"
description: "pagecache_isize_extended – update pagecache after extension of i_size"
---

<p>pagecache_isize_extended &#8211; update pagecache after extension of i_size</p>
<h2>Synopsis</h2>
<pre><code>void pagecache_isize_extended(struct inode *inode, loff_t from, loff_t to);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode for which i_size was extended</dl>
<p> <i>from</i></p>
<dl>
<dd>original inode size</dl>
<p> <i>to</i></p>
<dl>
<dd>new inode size</dl>
<h2>Description</h2>
<p>Handle extension of inode size either caused by extending truncate or by write starting after current i_size. We mark the page straddling current i_size RO so that <code>page_mkwrite</code> is called on the nearest write access to the page. This way filesystem can be sure that <code>page_mkwrite</code> is called on the page before user writes to the page via mmap after the i_size has been changed. </p>
<p> The function must be called after i_size is updated so that page fault coming after we unlock the page will already see the new i_size. The function must be called while we still hold i_mutex &#8211; this not only makes sure i_size is stable but also that userspace cannot observe new i_size value before we are prepared to store mmap writes at new inode size.</p>
<h2>Copyright</h2>
