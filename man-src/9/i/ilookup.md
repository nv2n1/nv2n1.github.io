---
title: "ilookup(9)"
name: "ilookup"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ilookup/"
---

ilookup - search for an inode in the inode cache

<h2>Synopsis</h2>

<pre><code>struct inode *ilookup(struct super_block *sb, unsigned long ino);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>super block of file system to search</dl>
 

 <i>ino</i>
<dl><dd>inode number to search for</dl>

<h2>Description</h2>

Search for the inode <i>ino</i> in the inode cache, and if the inode is in the cache, the inode is returned with an incremented reference count.

<h2>Copyright</h2>


