---
title: "debugfs_remove(9)"
name: "debugfs_remove"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_remove/"
description: "debugfs_remove – removes a file or directory from the debugfs filesystem"
---

<p>debugfs_remove &#8211; removes a file or directory from the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>void debugfs_remove(struct dentry *dentry);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>a pointer to a the dentry of the file or directory to be removed. If this parameter is NULL or an error value, nothing will be done.</dl>
<h2>Description</h2>
<p>This function removes a file or directory in debugfs that was previously created with a call to another debugfs function (like <code>debugfs_create_file</code> or variants thereof.) </p>
<p> This function is required to be called in order for the file to be removed, no automatic cleanup of files will happen when a module is removed, you are responsible here.</p>
<h2>Copyright</h2>
