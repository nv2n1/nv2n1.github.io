---
title: "d_alloc_pseudo(9)"
name: "d_alloc_pseudo"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_alloc_pseudo/"
---

d_alloc_pseudo - allocate a dentry (for lookup-less filesystems)

<h2>Synopsis</h2>

<pre><code>struct dentry *d_alloc_pseudo(struct super_block *sb, const struct qstr *name);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>the superblock</dl>
 

 <i>name</i>
<dl><dd>qstr of the name</dl>

<h2>Description</h2>

For a filesystem that just pins its dentries in memory and never performs lookups at all, return an unhashed IS_ROOT dentry.

<h2>Copyright</h2>


