---
title: "inode_init_always(9)"
name: "inode_init_always"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_init_always/"
---

inode_init_always - perform inode structure intialisation

<h2>Synopsis</h2>

<pre><code>int inode_init_always(struct super_block *sb, struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>superblock inode belongs to</dl>
 

 <i>inode</i>
<dl><dd>inode to initialise</dl>

<h2>Description</h2>

These are initializations that need to be done on every inode allocation as the fields are not initialised by slab allocation.

<h2>Copyright</h2>


