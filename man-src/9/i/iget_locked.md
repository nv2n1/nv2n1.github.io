---
title: "iget_locked(9)"
name: "iget_locked"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iget_locked/"
description: "iget_locked – obtain an inode from a mounted file system"
---

<p>iget_locked &#8211; obtain an inode from a mounted file system</p>
<h2>Synopsis</h2>
<pre><code>struct inode *iget_locked(struct super_block *sb, unsigned long ino);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>super block of file system</dl>
<p> <i>ino</i></p>
<dl>
<dd>inode number to get</dl>
<h2>Description</h2>
<p>Search for the inode specified by <i>ino</i> in the inode cache and if present return it with an increased reference count. This is for file systems where the inode number is sufficient for unique identification of an inode. </p>
<p> If the inode is not in cache, allocate a new inode and return it locked, hashed, and with the I_NEW flag set. The file system gets to fill it in before unlocking it via <code>unlock_new_inode</code>.</p>
<h2>Copyright</h2>
