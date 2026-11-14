---
title: "debugfs_create_regset32(9)"
name: "debugfs_create_regset32"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_regset32/"
description: "debugfs_create_regset32 – create a debugfs file that returns register values"
---

<p>debugfs_create_regset32 &#8211; create a debugfs file that returns register values</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_regset32(const char *name, umode_t mode, struct dentry *parent, struct debugfs_regset32 *regset);</code></pre>
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
<p> <i>regset</i></p>
<dl>
<dd>a pointer to a struct debugfs_regset32, which contains a pointer to an array of register definitions, the array size and the base address where the register bank is to be found.</dl>
<h2>Description</h2>
<p>This function creates a file in debugfs with the given name that reports the names and values of a set of 32-bit registers. If the <i>mode</i> variable is so set it can be read from. Writing is not supported. </p>
<p> This function will return a pointer to a dentry if it succeeds. This pointer must be passed to the <code>debugfs_remove</code> function when the file is to be removed (no automatic cleanup happens if your module is unloaded, you are responsible here.) If an error occurs, <code>NULL</code> will be returned. </p>
<p> If debugfs is not enabled in the kernel, the value &#8211;<code>ENODEV</code> will be returned. It is not wise to check for this value, but rather, check for <code>NULL</code> or !<code>NULL</code> instead as to eliminate the need for #ifdef in the calling code.</p>
<h2>Copyright</h2>
