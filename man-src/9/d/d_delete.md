---
title: "d_delete(9)"
name: "d_delete"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_delete/"
---

d_delete - delete a dentry

<h2>Synopsis</h2>

<pre><code>void d_delete(struct dentry *dentry);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>The dentry to delete</dl>

<h2>Description</h2>

Turn the dentry into a negative dentry if possible, otherwise remove it from the hash queues so it can be deleted later

<h2>Copyright</h2>


