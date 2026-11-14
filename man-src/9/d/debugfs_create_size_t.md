---
title: "debugfs_create_size_t(9)"
name: "debugfs_create_size_t"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_size_t/"
description: "debugfs_create_size_t – create a debugfs file that is used to read and write an size_t value"
---

<p>debugfs_create_size_t &#8211; create a debugfs file that is used to read and write an size_t value</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_size_t(const char *name, umode_t mode, struct dentry *parent, size_t *value);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>a pointer to a string containing the name of the file to create.</dl>
<p> <i>mode</i></p>
<dl>
<dd>the permission that the file should have</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is <code>NULL</code>, then the file will be created in the root of the debugfs filesystem.</dl>
<p> <i>value</i></p>
<dl>
<dd>a pointer to the variable that the file should read to and write from.</dl>
<h2>Copyright</h2>
