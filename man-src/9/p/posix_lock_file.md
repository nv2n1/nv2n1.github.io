---
title: "posix_lock_file(9)"
name: "posix_lock_file"
section: "9"
letter: "p"
url: "/docs/linux/man/9-posix_lock_file/"
---

posix_lock_file - Apply a POSIX-style lock to a file

<h2>Synopsis</h2>

<pre><code>int posix_lock_file(struct file *filp, struct file_lock *fl, struct file_lock *conflock);</code></pre>

<h2>Arguments</h2>

<i>filp</i>
<dl><dd><dd>The file to apply the lock to</dl>
 

 <i>fl</i>
<dl><dd>The lock to be applied</dl>
 

 <i>conflock</i>
<dl><dd>Place to return a copy of the conflicting lock, if found.</dl>

<h2>Description</h2>

Add a POSIX style lock to a file. We merge adjacent &amp; overlapping locks whenever possible. POSIX locks are sorted by owner task, then by starting address 

 Note that if called with an FL_EXISTS argument, the caller may determine whether or not a lock was successfully freed by testing the return value for -ENOENT.

<h2>Copyright</h2>


