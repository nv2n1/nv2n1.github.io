---
title: "debugfs_create_symlink(9)"
name: "debugfs_create_symlink"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_symlink/"
description: "debugfs_create_symlink – create a symbolic link in the debugfs filesystem"
---

<p>debugfs_create_symlink &#8211; create a symbolic link in the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_symlink(const char *name, struct dentry *parent, const char *target);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>a pointer to a string containing the name of the symbolic link to create.</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this symbolic link. This should be a directory dentry if set. If this parameter is NULL, then the symbolic link will be created in the root of the debugfs filesystem.</dl>
<p> <i>target</i></p>
<dl>
<dd>a pointer to a string containing the path to the target of the symbolic link.</dl>
<h2>Description</h2>
<p>This function creates a symbolic link with the given name in debugfs that links to the given target path. </p>
<p> This function will return a pointer to a dentry if it succeeds. This pointer must be passed to the <code>debugfs_remove</code> function when the symbolic link is to be removed (no automatic cleanup happens if your module is unloaded, you are responsible here.) If an error occurs, <code>NULL</code> will be returned. </p>
<p> If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned.</p>
<h2>Copyright</h2>
