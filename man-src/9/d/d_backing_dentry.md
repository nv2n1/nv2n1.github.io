---
title: "d_backing_dentry(9)"
name: "d_backing_dentry"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_backing_dentry/"
---

d_backing_dentry - Get upper or lower dentry we should be using

<h2>Synopsis</h2>

<pre><code>struct dentry *d_backing_dentry(struct dentry *upper);</code></pre>

<h2>Arguments</h2>

<i>upper</i>
<dl><dd><dd>The upper layer</dl>

<h2>Description</h2>

This is the helper that should be used to get the dentry of the inode that will be used if this dentry were opened as a file. It may be the upper dentry or it may be a lower dentry pinned by the upper. 

 Normal filesystems should not use this to access their own dentries.

<h2>Copyright</h2>


