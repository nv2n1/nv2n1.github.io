---
title: "vfs_cancel_lock(9)"
name: "vfs_cancel_lock"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_cancel_lock/"
---

vfs_cancel_lock - file byte range unblock lock

<h2>Synopsis</h2>

<pre><code>int vfs_cancel_lock(struct file *filp, struct file_lock *fl);</code></pre>

<h2>Arguments</h2>

<i>filp</i>
<dl><dd><dd>The file to apply the unblock to</dl>
 

 <i>fl</i>
<dl><dd>The lock to be unblocked</dl>

<h2>Description</h2>

Used by lock managers to cancel blocked requests

<h2>Copyright</h2>


