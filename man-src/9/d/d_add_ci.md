---
title: "d_add_ci(9)"
name: "d_add_ci"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_add_ci/"
---

d_add_ci - lookup or allocate new dentry with case-exact name

<h2>Synopsis</h2>

<pre><code>struct dentry *d_add_ci(struct dentry *dentry, struct inode *inode, struct qstr *name);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>the negative dentry that was passed to the parent's lookup func</dl>
 

 <i>inode</i>
<dl><dd>the inode case-insensitive lookup has found</dl>
 

 <i>name</i>
<dl><dd>the case-exact name to be associated with the returned dentry</dl>

<h2>Description</h2>

This is to avoid filling the dcache with case-insensitive names to the same inode, only the actual correct case is stored in the dcache for case-insensitive filesystems. 

 For a case-insensitive lookup match and if the the case-exact dentry already exists in in the dcache, use it and return it. 

 If no entry exists with the exact case name, allocate new dentry with the exact case, and return the spliced entry.

<h2>Copyright</h2>


