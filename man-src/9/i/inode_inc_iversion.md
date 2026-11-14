---
title: "inode_inc_iversion(9)"
name: "inode_inc_iversion"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_inc_iversion/"
---

inode_inc_iversion - increments i_version

<h2>Synopsis</h2>

<pre><code>void inode_inc_iversion(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode that need to be updated</dl>

<h2>Description</h2>

Every time the inode is modified, the i_version field will be incremented. The filesystem has to be mounted with i_version flag

<h2>Copyright</h2>


