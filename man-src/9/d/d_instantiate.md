---
title: "d_instantiate(9)"
name: "d_instantiate"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_instantiate/"
---

d_instantiate - fill in inode information for a dentry

<h2>Synopsis</h2>

<pre><code>void d_instantiate(struct dentry *entry, struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>entry</i>
<dl><dd><dd>dentry to complete</dl>
 

 <i>inode</i>
<dl><dd>inode to attach to this dentry</dl>

<h2>Description</h2>

Fill in inode information in the entry. 

 This turns negative dentries into productive full members of society. 

 NOTE! This assumes that the inode count has been incremented (or otherwise set) by the caller to indicate that it is now in use by the dcache.

<h2>Copyright</h2>


