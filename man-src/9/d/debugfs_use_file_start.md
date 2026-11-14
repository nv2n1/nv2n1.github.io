---
title: "debugfs_use_file_start(9)"
name: "debugfs_use_file_start"
section: "9"
letter: "d"
url: "/docs/linux/man/9-debugfs_use_file_start/"
description: "debugfs_use_file_start – mark the beginning of file data access"
---

<p>debugfs_use_file_start &#8211; mark the beginning of file data access</p>
<h2>Synopsis</h2>
<pre><code>int debugfs_use_file_start(const struct dentry *dentry, int *srcu_idx);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>the dentry object whose data is being accessed.</dl>
<p> <i>srcu_idx</i></p>
<dl>
<dd>a pointer to some memory to store a SRCU index in.</dl>
<h2>Description</h2>
<p>Up to a matching call to <code>debugfs_use_file_finish</code>, any successive call into the file removing functions <code>debugfs_remove</code> and <code>debugfs_remove_recursive</code> will block. Since associated private file data may only get freed after a successful return of any of the removal functions, you may safely access it after a successful call to <code>debugfs_use_file_start</code> without worrying about lifetime issues. </p>
<p> If &#8211;<code>EIO</code> is returned, the file has already been removed and thus, it is not safe to access any of its data. If, on the other hand, it is allowed to access the file data, zero is returned. </p>
<p> Regardless of the return code, any call to <code>debugfs_use_file_start</code> must be followed by a matching call to <code>debugfs_use_file_finish</code>.</p>
<h2>Copyright</h2>
