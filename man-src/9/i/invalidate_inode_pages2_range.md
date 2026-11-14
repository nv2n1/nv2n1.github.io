---
title: "invalidate_inode_pages2_range(9)"
name: "invalidate_inode_pages2_range"
section: "9"
letter: "i"
url: "/docs/linux/man/9-invalidate_inode_pages2_range/"
---

invalidate_inode_pages2_range - remove range of pages from an address_space

<h2>Synopsis</h2>

<pre><code>int invalidate_inode_pages2_range(struct address_space *mapping, pgoff_t start, pgoff_t end);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the address_space</dl>
 

 <i>start</i>
<dl><dd>the page offset 'from' which to invalidate</dl>
 

 <i>end</i>
<dl><dd>the page offset 'to' which to invalidate (inclusive)</dl>

<h2>Description</h2>

Any pages which are found to be mapped into pagetables are unmapped prior to invalidation. 

 Returns -EBUSY if any pages could not be invalidated.

<h2>Copyright</h2>


