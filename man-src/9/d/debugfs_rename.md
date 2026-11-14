---
title: "debugfs_rename(9)"
name: "debugfs_rename"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_rename/"
description: "debugfs_rename – rename a file/directory in the debugfs filesystem"
---

<p>debugfs_rename &#8211; rename a file/directory in the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_rename(struct dentry *old_dir, struct dentry *old_dentry, struct dentry *new_dir, const char *new_name);</code></pre>
<h2>Arguments</h2>
<p><i>old_dir</i></p>
<dl>
<dd>
<dd>a pointer to the parent dentry for the renamed object. This should be a directory dentry.</dl>
<p> <i>old_dentry</i></p>
<dl>
<dd>dentry of an object to be renamed.</dl>
<p> <i>new_dir</i></p>
<dl>
<dd>a pointer to the parent dentry where the object should be moved. This should be a directory dentry.</dl>
<p> <i>new_name</i></p>
<dl>
<dd>a pointer to a string containing the target name.</dl>
<h2>Description</h2>
<p>This function renames a file/directory in debugfs. The target must not exist for rename to succeed. </p>
<p> This function will return a pointer to old_dentry (which is updated to reflect renaming) if it succeeds. If an error occurs, <code>NULL</code> will be returned. </p>
<p> If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned.</p>
<h2>Copyright</h2>
