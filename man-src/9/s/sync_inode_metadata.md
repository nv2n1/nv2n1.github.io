---
title: "sync_inode_metadata(9)"
name: "sync_inode_metadata"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sync_inode_metadata/"
---

sync_inode_metadata - write an inode to disk

<h2>Synopsis</h2>

<pre><code>int sync_inode_metadata(struct inode *inode, int wait);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>the inode to sync</dl>
 

 <i>wait</i>
<dl><dd>wait for I/O to complete.</dl>

<h2>Description</h2>

Write an inode to disk and adjust its dirty state after completion.

<h2>Note</h2>

only writes the actual inode, no associated data or other metadata.

<h2>Copyright</h2>


