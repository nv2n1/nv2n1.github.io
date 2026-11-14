---
title: "d_inode(9)"
name: "d_inode"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_inode/"
---

d_inode - Get the actual inode of this dentry

<h2>Synopsis</h2>

<pre><code>struct inode *d_inode(const struct dentry *dentry);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>The dentry to query</dl>

<h2>Description</h2>

This is the helper normal filesystems should use to get at their own inodes in their own dentries and ignore the layering superimposed upon them.

<h2>Copyright</h2>


