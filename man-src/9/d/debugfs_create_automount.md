---
title: "debugfs_create_automount(9)"
name: "debugfs_create_automount"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_create_automount/"
description: "debugfs_create_automount – create automount point in the debugfs filesystem"
---

<p>debugfs_create_automount &#8211; create automount point in the debugfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *debugfs_create_automount(const char *name, struct dentry *parent, struct vfsmount *(*f)(void *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>a pointer to a string containing the name of the file to create.</dl>
<p> <i>parent</i></p>
<dl>
<dd>a pointer to the parent dentry for this file. This should be a directory dentry if set. If this parameter is NULL, then the file will be created in the root of the debugfs filesystem.</dl>
<p> <i>f</i></p>
<dl>
<dd>function to be called when pathname resolution steps on that one.</dl>
<p> <i>data</i></p>
<dl>
<dd>opaque argument to pass to <code>f</code>.</dl>
<h2>Description</h2>
<p><i>f</i> should return what -&gt;<code>d_automount</code> would.</p>
<h2>Copyright</h2>
