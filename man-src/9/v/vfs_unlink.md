---
title: "vfs_unlink(9)"
name: "vfs_unlink"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_unlink/"
---

vfs_unlink - unlink a filesystem object

<h2>Synopsis</h2>

<pre><code>int vfs_unlink(struct inode *dir, struct dentry *dentry, struct inode **delegated_inode);</code></pre>

<h2>Arguments</h2>

<i>dir</i>
<dl><dd><dd>parent directory</dl>
 

 <i>dentry</i>
<dl><dd>victim</dl>
 

 <i>delegated_inode</i>
<dl><dd>returns victim inode, if the inode is delegated.</dl>

<h2>Description</h2>

The caller must hold dir-&gt;i_mutex. 

 If vfs_unlink discovers a delegation, it will return -EWOULDBLOCK and return a reference to the inode in delegated_inode. The caller should then break the delegation on that inode and retry. Because breaking a delegation may take a long time, the caller should drop dir-&gt;i_mutex before doing so. 

 Alternatively, a caller may pass NULL for delegated_inode. This may be appropriate for callers that expect the underlying filesystem not to be NFS exported.

<h2>Copyright</h2>


