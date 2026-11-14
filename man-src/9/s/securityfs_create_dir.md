---
title: "securityfs_create_dir(9)"
name: "securityfs_create_dir"
section: "9"
letter: "s"
url: "/docs/linux/man/9-securityfs_create_dir/"
description: "securityfs_create_dir – create a directory in the securityfs filesystem"
---

<p>securityfs_create_dir &#8211; create a directory in the securityfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *securityfs_create_dir(const char *name, struct dentry *parent);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>a pointer to a string containing the name of the directory to create.</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is <code>NULL</code>, then the directory will be created in the root of the securityfs filesystem.</dl>
<h2>Description</h2>
<p>This function creates a directory in securityfs with the given <i>name</i>. </p>
<p> This function returns a pointer to a dentry if it succeeds. This pointer must be passed to the <code>securityfs_remove</code> function when the file is to be removed (no automatic cleanup happens if your module is unloaded, you are responsible here). If an error occurs, the function will return the error value (via ERR_PTR). </p>
<p> If securityfs is not enabled in the kernel, the value <code>-ENODEV</code> is returned.</p>
<h2>Copyright</h2>
