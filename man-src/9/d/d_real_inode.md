---
title: "d_real_inode(9)"
name: "d_real_inode"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_real_inode/"
description: "d_real_inode – Return the real inode"
---

<p>d_real_inode &#8211; Return the real inode</p>
<h2>Synopsis</h2>
<pre><code>struct inode *d_real_inode(const struct dentry *dentry);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>The dentry to query</dl>
<h2>Description</h2>
<p>If dentry is on an union/overlay, then return the underlying, real inode. Otherwise return <code>d_inode</code>.</p>
<h2>Copyright</h2>
