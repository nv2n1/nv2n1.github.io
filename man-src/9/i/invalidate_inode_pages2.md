---
title: "invalidate_inode_pages2(9)"
name: "invalidate_inode_pages2"
section: "9"
letter: "i"
url: "/docs/linux/man/9-invalidate_inode_pages2/"
---

invalidate_inode_pages2 - remove all pages from an address_space

<h2>Synopsis</h2>

<pre><code>int invalidate_inode_pages2(struct address_space *mapping);</code></pre>

<h2>Arguments</h2>

<i>mapping</i>
<dl><dd><dd>the address_space</dl>

<h2>Description</h2>

Any pages which are found to be mapped into pagetables are unmapped prior to invalidation. 

 Returns -EBUSY if any pages could not be invalidated.

<h2>Copyright</h2>


