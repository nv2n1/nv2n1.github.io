---
title: "sync_inode(9)"
name: "sync_inode"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sync_inode/"
description: "sync_inode – write an inode and its pages to disk."
---

<p>sync_inode &#8211; write an inode and its pages to disk.</p>
<h2>Synopsis</h2>
<pre><code>int sync_inode(struct inode *inode, struct writeback_control *wbc);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>the inode to sync</dl>
<p> <i>wbc</i></p>
<dl>
<dd>controls the writeback mode</dl>
<h2>Description</h2>
<p><code>sync_inode</code> will write an inode and its pages to disk. It will also correctly update the inode on its superblock&#8217;s dirty inode lists and will update inode-&gt;i_state. </p>
<p> The caller must have a ref on the inode.</p>
<h2>Copyright</h2>
