---
title: "debugfs_remove_recursive(9)"
name: "debugfs_remove_recursive"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_remove_recursive/"
description: "debugfs_remove_recursive – recursively removes a directory"
---

<p>debugfs_remove_recursive &#8211; recursively removes a directory</p>
<h2>Synopsis</h2>
<pre><code>void debugfs_remove_recursive(struct dentry *dentry);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>a pointer to a the dentry of the directory to be removed. If this parameter is NULL or an error value, nothing will be done.</dl>
<h2>Description</h2>
<p>This function recursively removes a directory tree in debugfs that was previously created with a call to another debugfs function (like <code>debugfs_create_file</code> or variants thereof.) </p>
<p> This function is required to be called in order for the file to be removed, no automatic cleanup of files will happen when a module is removed, you are responsible here.</p>
<h2>Copyright</h2>
