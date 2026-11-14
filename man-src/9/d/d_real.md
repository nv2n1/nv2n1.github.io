---
title: "d_real(9)"
name: "d_real"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_real/"
---

d_real - Return the real dentry

<h2>Synopsis</h2>

<pre><code>struct dentry *d_real(struct dentry *dentry, const struct inode *inode, unsigned int flags);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>the dentry to query</dl>
 

 <i>inode</i>
<dl><dd>inode to select the dentry from multiple layers (can be NULL)</dl>
 

 <i>flags</i>
<dl><dd>open flags to control copy-up behavior</dl>

<h2>Description</h2>

If dentry is on an union/overlay, then return the underlying, real dentry. Otherwise return the dentry itself. 

 See also: Documentation/filesystems/vfs.txt

<h2>Copyright</h2>


