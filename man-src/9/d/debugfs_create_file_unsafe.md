---
title: "debugfs_create_file_unsafe(9)"
name: "debugfs_create_file_unsafe"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_file_unsafe/"
description: "debugfs_create_file_unsafe – create a file in the debugfs filesystem"
---

<p>debugfs_create_file_unsafe &#8211; create a file in the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_file_unsafe(const char *name, umode_t mode, struct dentry *parent, void *data, const struct file_operations *fops);</code></pre>
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
<p><code>debugfs_create_file_unsafe</code> is completely analogous to <code>debugfs_create_file</code>, the only difference being that the fops handed it will not get protected against file removals by the debugfs core. </p>
<p> It is your responsibility to protect your struct file_operation methods against file removals by means of <code>debugfs_use_file_start</code> and <code>debugfs_use_file_finish</code>. -&gt;<code>open</code> is still protected by debugfs though. </p>
<p> Any struct file_operations defined by means of <code>DEFINE_DEBUGFS_ATTRIBUTE</code> is protected against file removals and thus, may be used here.</p>
<h2>Copyright</h2>
