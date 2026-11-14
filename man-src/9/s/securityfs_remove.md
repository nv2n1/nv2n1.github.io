---
title: "securityfs_remove(9)"
name: "securityfs_remove"
section: "9"
letter: "s"
url: "/docs/linux/man/9-securityfs_remove/"
description: "securityfs_remove – removes a file or directory from the securityfs filesystem"
---

<p>securityfs_remove &#8211; removes a file or directory from the securityfs filesystem</p>
<h2>Synopsis</h2>
<pre><code>void securityfs_remove(struct dentry *dentry);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>a pointer to a the dentry of the file or directory to be removed.</dl>
<h2>Description</h2>
<p>This function removes a file or directory in securityfs that was previously created with a call to another securityfs function (like <code>securityfs_create_file</code> or variants thereof.) </p>
<p> This function is required to be called in order for the file to be removed. No automatic cleanup of files will happen when a module is removed; you are responsible here.</p>
<h2>Copyright</h2>
