---
title: "set_nlink(9)"
name: "set_nlink"
section: "9"
letter: "s"
url: "/docs/linux/man/9-set_nlink/"
---

set_nlink - directly set an inode's link count

<h2>Synopsis</h2>

<pre><code>void set_nlink(struct inode *inode, unsigned int nlink);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd></dd><dd>inode</dd></dl>
 

 <i>nlink</i>
<dl><dd>new nlink (should be non-zero)</dd></dl>

<h2>Description</h2>

This is a low-level filesystem helper to replace any direct filesystem manipulation of i_nlink.

<h2>Copyright</h2>


