---
title: "d_add(9)"
name: "d_add"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_add/"
description: "d_add – add dentry to hash queues"
---

<p>d_add &#8211; add dentry to hash queues</p>
<h2>Synopsis</h2>
<pre><code>void d_add(struct dentry *entry, struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>entry</i></p>
<dl>
<dd>
<dd>dentry to add</dl>
<p> <i>inode</i></p>
<dl>
<dd>The inode to attach to this dentry</dl>
<h2>Description</h2>
<p>This adds the entry to the hash queues and initializes <i>inode</i>. The entry was actually filled in earlier during <code>d_alloc</code>.</p>
<h2>Copyright</h2>
