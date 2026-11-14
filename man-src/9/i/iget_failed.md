---
title: "iget_failed(9)"
name: "iget_failed"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iget_failed/"
---

iget_failed - Mark an under-construction inode as dead and release it

<h2>Synopsis</h2>

<pre><code>void iget_failed(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>The inode to discard</dl>

<h2>Description</h2>

Mark an under-construction inode as dead and release it.

<h2>Copyright</h2>


