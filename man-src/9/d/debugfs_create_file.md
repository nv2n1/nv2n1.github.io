---
title: "debugfs_create_file(9)"
name: "debugfs_create_file"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_file/"
description: "debugfs_create_file – create a file in the debugfs filesystem"
---

<p>debugfs_create_file &#8211; create a file in the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_file(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>a pointer to a string containing the name of the file to create.</dl>
<p> <i>mode</i></p>
<dl>
<dd>the permission that the file should have.</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is NULL, then the file will be created in the root of the debugfs filesystem.</dl>
<p> <i>data</i></p>
<dl>
<dd>a pointer to something that the caller will want to get to later on. The inode.i_private pointer will point to this value on the <code>open</code> call.</dl>
<p> <i>fops</i></p>
<dl>
<dd>a pointer to a struct file_operations that should be used for this file.</dl>
<h2>Description</h2>
<p>This is the basic &#8220;create a file&#8221; function for debugfs. It allows for a wide range of flexibility in creating a file, or a directory (if you want to create a directory, the <code>debugfs_create_dir</code> function is recommended to be used instead.) </p>
<p> This function will return a pointer to a dentry if it succeeds. This pointer must be passed to the <code>debugfs_remove</code> function when the file is to be removed (no automatic cleanup happens if your module is unloaded, you are responsible here.) If an error occurs, <code>NULL</code> will be returned. </p>
<p> If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned.</p>
<h2>Copyright</h2>
