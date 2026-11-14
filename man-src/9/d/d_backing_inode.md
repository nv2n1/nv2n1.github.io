---
title: "d_backing_inode(9)"
name: "d_backing_inode"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_backing_inode/"
---

d_backing_inode - Get upper or lower inode we should be using

<h2>Synopsis</h2>

<pre><code>struct inode *d_backing_inode(const struct dentry *upper);</code></pre>

<h2>Arguments</h2>

<i>upper</i>
<dl><dd><dd>The upper layer</dl>

<h2>Description</h2>

This is the helper that should be used to get at the inode that will be used if this dentry were to be opened as a file. The inode may be on the upper dentry or it may be on a lower dentry pinned by the upper. 

 Normal filesystems should not use this to access their own inodes.

<h2>Copyright</h2>


