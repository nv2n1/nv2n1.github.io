---
title: "truncate_inode_pages_range(9)"
name: "truncate_inode_pages_range"
section: "9"
letter: "t"
url: "/docs/linux/man/9-truncate_inode_pages_range/"
description: "truncate_inode_pages_range – truncate range of pages specified by start & end byte offsets"
---

<p>truncate_inode_pages_range &#8211; truncate range of pages specified by start &amp; end byte offsets</p>
<h2>Synopsis</h2>
<pre><code>void truncate_inode_pages_range(struct address_space *mapping, loff_t lstart, loff_t lend);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>mapping to truncate</dl>
<p> <i>lstart</i></p>
<dl>
<dd>offset from which to truncate</dl>
<p> <i>lend</i></p>
<dl>
<dd>offset to which to truncate (inclusive)</dl>
<h2>Description</h2>
<p>Truncate the page cache, removing the pages that are between specified offsets (and zeroing out partial pages if lstart or lend + 1 is not page aligned). </p>
<p> Truncate takes two passes &#8211; the first pass is nonblocking. It will not block on page locks and it will not block on writeback. The second pass will wait. This is to prevent as much IO as possible in the affected region. The first pass will remove most pages, so the search cost of the second pass is low. </p>
<p> We pass down the cache-hot hint to the page freeing code. Even if the mapping is large, it is probably the case that the final pages are the most recently touched, and freeing happens in ascending file offset order. </p>
<p> Note that since -&gt;<code>invalidatepage</code> accepts range to invalidate truncate_inode_pages_range is able to handle cases where lend + 1 is not page aligned properly.</p>
<h2>Copyright</h2>
