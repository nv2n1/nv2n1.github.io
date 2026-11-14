---
title: "shrink_dcache_sb(9)"
name: "shrink_dcache_sb"
section: "9"
letter: "s"
url: "/docs/linux/man/9-shrink_dcache_sb/"
---

shrink_dcache_sb - shrink dcache for a superblock

<h2>Synopsis</h2>

<pre><code>void shrink_dcache_sb(struct super_block *sb);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>superblock</dl>

<h2>Description</h2>

Shrink the dcache for the specified super block. This is used to free the dcache before unmounting a file system.

<h2>Copyright</h2>


