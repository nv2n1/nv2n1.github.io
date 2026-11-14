---
title: "inode_init_owner(9)"
name: "inode_init_owner"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_init_owner/"
---

inode_init_owner - Init uid,gid,mode for new inode according to posix standards

<h2>Synopsis</h2>

<pre><code>void inode_init_owner(struct inode *inode, const struct inode *dir, umode_t mode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>New inode</dl>
 

 <i>dir</i>
<dl><dd>Directory inode</dl>
 

 <i>mode</i>
<dl><dd>mode of the new inode</dl>

<h2>Copyright</h2>


