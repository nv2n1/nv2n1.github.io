---
title: "invalidate_mapping_pages(9)"
name: "invalidate_mapping_pages"
section: "9"
letter: "i"
url: "/docs/linux/man/9-invalidate_mapping_pages/"
description: "invalidate_mapping_pages – Invalidate all the unlocked pages of one inode"
---

<p>invalidate_mapping_pages &#8211; Invalidate all the unlocked pages of one inode</p>
<h2>Synopsis</h2>
<pre><code>unsigned long invalidate_mapping_pages(struct address_space *mapping, pgoff_t start, pgoff_t end);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the address_space which holds the pages to invalidate</dl>
<p> <i>start</i></p>
<dl>
<dd>the offset &#8216;from&#8217; which to invalidate</dl>
<p> <i>end</i></p>
<dl>
<dd>the offset &#8216;to&#8217; which to invalidate (inclusive)</dl>
<h2>Description</h2>
<p>This function only removes the unlocked pages, if you want to remove all the pages of one inode, you must call truncate_inode_pages. </p>
<p> <code>invalidate_mapping_pages</code> will not block on IO activity. It will not invalidate pages which are dirty, locked, under writeback or mapped into pagetables.</p>
<h2>Copyright</h2>
