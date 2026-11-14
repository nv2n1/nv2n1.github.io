---
title: "debugfs_create_dir(9)"
name: "debugfs_create_dir"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_dir/"
description: "debugfs_create_dir – create a directory in the debugfs filesystem"
---

<p>debugfs_create_dir &#8211; create a directory in the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_dir(const char *name, struct dentry *parent);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>a pointer to a string containing the name of the directory to create.</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is NULL, then the directory will be created in the root of the debugfs filesystem.</dl>
<h2>Description</h2>
<p>This function creates a directory in debugfs with the given name. </p>
<p> This function will return a pointer to a dentry if it succeeds. This pointer must be passed to the <code>debugfs_remove</code> function when the file is to be removed (no automatic cleanup happens if your module is unloaded, you are responsible here.) If an error occurs, <code>NULL</code> will be returned. </p>
<p> If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned.</p>
<h2>Copyright</h2>
