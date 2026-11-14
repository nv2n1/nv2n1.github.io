---
title: "new_inode(9)"
name: "new_inode"
section: "9"
letter: "n"
url: "/docs/linux/man/9-new_inode/"
description: "new_inode – obtain an inode"
---

<p>new_inode &#8211; obtain an inode</p>
<h2>Synopsis</h2>
<pre><code>struct inode *new_inode(struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>superblock</dl>
<h2>Description</h2>
<p>Allocates a new inode for given superblock. The default gfp_mask for allocations related to inode-&gt;i_mapping is GFP_HIGHUSER_MOVABLE. If HIGHMEM pages are unsuitable or it is known that pages allocated for the page cache are not reclaimable or migratable, <code>mapping_set_gfp_mask</code> must be called with suitable flags on the newly created inode&#8217;s mapping</p>
<h2>Copyright</h2>
