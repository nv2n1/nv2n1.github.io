---
title: "d_splice_alias(9)"
name: "d_splice_alias"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_splice_alias/"
---

d_splice_alias - splice a disconnected dentry into the tree if one exists

<h2>Synopsis</h2>

<pre><code>struct dentry *d_splice_alias(struct inode *inode, struct dentry *dentry);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>the inode which may have a disconnected dentry</dl>
 

 <i>dentry</i>
<dl><dd>a negative dentry which we want to point to the inode.</dl>

<h2>Description</h2>

If inode is a directory and has an IS_ROOT alias, then d_move that in place of the given dentry and return it, else simply d_add the inode to the dentry and return NULL. 

 If a non-IS_ROOT directory is found, the filesystem is corrupt, and we should error out: directories can't have multiple aliases. 

 This is needed in the lookup routine of any filesystem that is exportable (via knfsd) so that we can build dcache paths to directories effectively. 

 If a dentry was found and moved, then it is returned. Otherwise NULL is returned. This matches the expected return value of -&gt;lookup. 

 Cluster filesystems may call this function with a negative, hashed dentry. In that case, we know that the inode will be a regular file, and also this will only occur during atomic_open. So we need to check for the dentry being already hashed only in the final case.

<h2>Copyright</h2>


