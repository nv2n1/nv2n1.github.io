---
title: "vfs_link(9)"
name: "vfs_link"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_link/"
---

vfs_link - create a new link

<h2>Synopsis</h2>

<pre><code>int vfs_link(struct dentry *old_dentry, struct inode *dir, struct dentry *new_dentry, struct inode **delegated_inode);</code></pre>

<h2>Arguments</h2>

<i>old_dentry</i>
<dl><dd><dd>object to be linked</dl>
 

 <i>dir</i>
<dl><dd>new parent</dl>
 

 <i>new_dentry</i>
<dl><dd>where to create the new link</dl>
 

 <i>delegated_inode</i>
<dl><dd>returns inode needing a delegation break</dl>

<h2>Description</h2>

The caller must hold dir-&gt;i_mutex 

 If vfs_link discovers a delegation on the to-be-linked file in need of breaking, it will return -EWOULDBLOCK and return a reference to the inode in delegated_inode. The caller should then break the delegation and retry. Because breaking a delegation may take a long time, the caller should drop the i_mutex before doing so. 

 Alternatively, a caller may pass NULL for delegated_inode. This may be appropriate for callers that expect the underlying filesystem not to be NFS exported.

<h2>Copyright</h2>


