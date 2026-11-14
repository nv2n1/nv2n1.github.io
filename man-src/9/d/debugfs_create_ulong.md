---
title: "debugfs_create_ulong(9)"
name: "debugfs_create_ulong"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_ulong/"
description: "debugfs_create_ulong – create a debugfs file that is used to read and write an unsigned long value."
---

<p>debugfs_create_ulong &#8211; create a debugfs file that is used to read and write an unsigned long value.</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_ulong(const char *name, umode_t mode, struct dentry *parent, unsigned long *value);</code></pre>
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
<h2>Description</h2>
<p>This function creates a file in debugfs with the given name that contains the value of the variable <i>value</i>. If the <i>mode</i> variable is so set, it can be read from, and written to. </p>
<p> This function will return a pointer to a dentry if it succeeds. This pointer must be passed to the <code>debugfs_remove</code> function when the file is to be removed (no automatic cleanup happens if your module is unloaded, you are responsible here.) If an error occurs, <code>NULL</code> will be returned. </p>
<p> If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned. It is not wise to check for this value, but rather, check for <code>NULL</code> or !<code>NULL</code> instead as to eliminate the need for #ifdef in the calling code.</p>
<h2>Copyright</h2>
