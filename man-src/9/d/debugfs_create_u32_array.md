---
title: "debugfs_create_u32_array(9)"
name: "debugfs_create_u32_array"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_u32_array/"
description: "debugfs_create_u32_array – create a debugfs file that is used to read u32 array."
---

<p>debugfs_create_u32_array &#8211; create a debugfs file that is used to read u32 array.</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_u32_array(const char *name, umode_t mode, struct dentry *parent, u32 *array, u32 elements);</code></pre>
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
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is <code>NULL</code>, then the file will be created in the root of the debugfs filesystem.</dl>
<p> <i>array</i></p>
<dl>
<dd>u32 array that provides data.</dl>
<p> <i>elements</i></p>
<dl>
<dd>total number of elements in the array.</dl>
<h2>Description</h2>
<p>This function creates a file in debugfs with the given name that exports <i>array</i> as data. If the <i>mode</i> variable is so set it can be read from. Writing is not supported. Seek within the file is also not supported. Once array is created its size can not be changed. </p>
<p> The function returns a pointer to dentry on success. If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned.</p>
<h2>Copyright</h2>
