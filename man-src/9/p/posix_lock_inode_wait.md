---
title: "posix_lock_inode_wait(9)"
name: "posix_lock_inode_wait"
section: "9"
letter: "p"
url: "/docs/linux/man/9-posix_lock_inode_wait/"
---

posix_lock_inode_wait - Apply a POSIX-style lock to a file

<h2>Synopsis</h2>

<pre><code>int posix_lock_inode_wait(struct inode *inode, struct file_lock *fl);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode of file to which lock request should be applied</dl>
 

 <i>fl</i>
<dl><dd>The lock to be applied</dl>

<h2>Description</h2>

Apply a POSIX style lock request to an inode.

<h2>Copyright</h2>


