---
title: "write_inode_now(9)"
name: "write_inode_now"
section: "9"
letter: "w"
url: "/docs/linux/man/9-write_inode_now/"
---

write_inode_now - write an inode to disk

<h2>Synopsis</h2>

<pre><code>int write_inode_now(struct inode *inode, int sync);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode to write to disk</dl>
 

 <i>sync</i>
<dl><dd>whether the write should be synchronous or not</dl>

<h2>Description</h2>

This function commits an inode to disk immediately if it is dirty. This is primarily needed by knfsd. 

 The caller must either have a ref on the inode or must have set I_WILL_FREE.

<h2>Copyright</h2>


