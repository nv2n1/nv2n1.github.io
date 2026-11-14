---
title: "drop_nlink(9)"
name: "drop_nlink"
section: "9"
letter: "d"
url: "/docs/linux/man/9-drop_nlink/"
---

drop_nlink - directly drop an inode's link count

<h2>Synopsis</h2>

<pre><code>void drop_nlink(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode</dl>

<h2>Description</h2>

This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink. In cases where we are attempting to track writes to the filesystem, a decrement to zero means an imminent write when the file is truncated and actually unlinked on the filesystem.

<h2>Copyright</h2>


