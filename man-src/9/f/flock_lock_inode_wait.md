---
title: "flock_lock_inode_wait(9)"
name: "flock_lock_inode_wait"
section: "9"
letter: "f"
url: "/docs/linux/man/9-flock_lock_inode_wait/"
---

flock_lock_inode_wait - Apply a FLOCK-style lock to a file

<h2>Synopsis</h2>

<pre><code>int flock_lock_inode_wait(struct inode *inode, struct file_lock *fl);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode of the file to apply to</dl>
 

 <i>fl</i>
<dl><dd>The lock to be applied</dl>

<h2>Description</h2>

Apply a FLOCK style lock request to an inode.

<h2>Copyright</h2>


