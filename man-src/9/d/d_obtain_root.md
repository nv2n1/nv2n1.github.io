---
title: "d_obtain_root(9)"
name: "d_obtain_root"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_obtain_root/"
description: "d_obtain_root – find or allocate a dentry for a given inode"
---

<p>d_obtain_root &#8211; find or allocate a dentry for a given inode</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *d_obtain_root(struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode to allocate the dentry for</dl>
<h2>Description</h2>
<p>Obtain an IS_ROOT dentry for the root of a filesystem. </p>
<p> We must ensure that directory inodes only ever have one dentry. If a dentry is found, that is returned instead of allocating a new one. </p>
<p> On successful return, the reference to the inode has been transferred to the dentry. In case of an error the reference on the inode is released. A <code>NULL</code> or IS_ERR inode may be passed in and will be the error will be propagate to the return value, with a <code>NULL</code><i>inode</i> replaced by ERR_PTR(-ESTALE).</p>
<h2>Copyright</h2>
