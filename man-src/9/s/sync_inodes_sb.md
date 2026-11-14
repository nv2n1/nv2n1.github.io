---
title: "sync_inodes_sb(9)"
name: "sync_inodes_sb"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sync_inodes_sb/"
---

sync_inodes_sb - sync sb inode pages

<h2>Synopsis</h2>

<pre><code>void sync_inodes_sb(struct super_block *sb);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>the superblock</dl>

<h2>Description</h2>

This function writes and waits on any dirty inode belonging to this super_block.

<h2>Copyright</h2>


