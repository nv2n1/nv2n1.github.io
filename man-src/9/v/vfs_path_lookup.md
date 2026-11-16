---
title: "vfs_path_lookup(9)"
name: "vfs_path_lookup"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_path_lookup/"
---

vfs_path_lookup - lookup a file path relative to a dentry-vfsmount pair

<h2>Synopsis</h2>

<pre><code>int vfs_path_lookup(struct dentry *dentry, struct vfsmount *mnt, const char *name, unsigned int flags, struct path *path);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd></dd><dd>pointer to dentry of the base directory</dd></dl>
 

 <i>mnt</i>
<dl><dd>pointer to vfs mount of the base directory</dd></dl>
 

 <i>name</i>
<dl><dd>pointer to file name</dd></dl>
 

 <i>flags</i>
<dl><dd>lookup flags</dd></dl>
 

 <i>path</i>
<dl><dd>pointer to struct path to fill</dd></dl>

<h2>Copyright</h2>


