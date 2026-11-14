---
title: "vfs_get_link(9)"
name: "vfs_get_link"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_get_link/"
description: "vfs_get_link – get symlink body"
---

<p>vfs_get_link &#8211; get symlink body</p>
<h2>Synopsis</h2>
<pre><code>const char *vfs_get_link(struct dentry *dentry, struct delayed_call *done);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>dentry on which to get symbolic link</dl>
<p> <i>done</i></p>
<dl>
<dd>caller needs to free returned data with this</dl>
<h2>Description</h2>
<p>Calls security hook and i_op-&gt;<code>get_link</code> on the supplied inode. </p>
<p> It does not touch atime. That&#8217;s up to the caller if necessary. </p>
<p> Does not work on &#8220;special&#8221; symlinks like /proc/$$/fd/N</p>
<h2>Copyright</h2>
