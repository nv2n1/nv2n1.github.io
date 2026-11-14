---
title: "d_exact_alias(9)"
name: "d_exact_alias"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_exact_alias/"
---

d_exact_alias - find and hash an exact unhashed alias

<h2>Synopsis</h2>

<pre><code>struct dentry *d_exact_alias(struct dentry *entry, struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>entry</i>
<dl><dd><dd>dentry to add</dl>
 

 <i>inode</i>
<dl><dd>The inode to go with this dentry</dl>

<h2>Description</h2>

If an unhashed dentry with the same name/parent and desired inode already exists, hash and return it. Otherwise, return NULL. 

 Parent directory should be locked.

<h2>Copyright</h2>


