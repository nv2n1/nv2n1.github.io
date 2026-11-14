---
title: "iget5_locked(9)"
name: "iget5_locked"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iget5_locked/"
description: "iget5_locked – obtain an inode from a mounted file system"
---

<p>iget5_locked &#8211; obtain an inode from a mounted file system</p>
<h2>Synopsis</h2>
<pre><code>struct inode *iget5_locked(struct super_block *sb, unsigned long hashval, int (*test)(struct inode *, void *), int (*set)(struct inode *, void *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>super block of file system</dl>
<p> <i>hashval</i></p>
<dl>
<dd>hash value (usually inode number) to get</dl>
<p> <i>test</i></p>
<dl>
<dd>callback used for comparisons between inodes</dl>
<p> <i>set</i></p>
<dl>
<dd>callback used to initialize a new struct inode</dl>
<p> <i>data</i></p>
<dl>
<dd>opaque data pointer to pass to <i>test</i> and <i>set</i></dl>
<h2>Description</h2>
<p>Search for the inode specified by <i>hashval</i> and <i>data</i> in the inode cache, and if present it is return it with an increased reference count. This is a generalized version of <code>iget_locked</code> for file systems where the inode number is not sufficient for unique identification of an inode. </p>
<p> If the inode is not in cache, allocate a new inode and return it locked, hashed, and with the I_NEW flag set. The file system gets to fill it in before unlocking it via <code>unlock_new_inode</code>. </p>
<p> Note both <i>test</i> and <i>set</i> are called with the inode_hash_lock held, so can&#8217;t sleep.</p>
<h2>Copyright</h2>
