---
title: "d_inode_rcu(9)"
name: "d_inode_rcu"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_inode_rcu/"
description: "d_inode_rcu – Get the actual inode of this dentry with ACCESS_ONCE"
---

<p>d_inode_rcu &#8211; Get the actual inode of this dentry with <code>ACCESS_ONCE</code></p>
<h2>Synopsis</h2>
<pre><code>struct inode *d_inode_rcu(const struct dentry *dentry);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>The dentry to query</dl>
<h2>Description</h2>
<p>This is the helper normal filesystems should use to get at their own inodes in their own dentries and ignore the layering superimposed upon them.</p>
<h2>Copyright</h2>
