---
title: "make_bad_inode(9)"
name: "make_bad_inode"
section: "9"
letter: "m"
url: "/docs/linux/man/9-make_bad_inode/"
---

make_bad_inode - mark an inode bad due to an I/O error

<h2>Synopsis</h2>

<pre><code>void make_bad_inode(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>Inode to mark bad</dl>

<h2>Description</h2>

When an inode cannot be read due to a media or remote network failure this function makes the inode "bad" and causes I/O operations on it to fail from this point on.

<h2>Copyright</h2>


