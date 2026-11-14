---
title: "locks_lock_inode_wait(9)"
name: "locks_lock_inode_wait"
section: "9"
letter: "l"
url: "/docs/linux/man/9-locks_lock_inode_wait/"
---

locks_lock_inode_wait - Apply a lock to an inode

<h2>Synopsis</h2>

<pre><code>int locks_lock_inode_wait(struct inode *inode, struct file_lock *fl);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode of the file to apply to</dl>
 

 <i>fl</i>
<dl><dd>The lock to be applied</dl>

<h2>Description</h2>

Apply a POSIX or FLOCK style lock request to an inode.

<h2>Copyright</h2>


