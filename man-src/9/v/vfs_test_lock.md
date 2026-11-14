---
title: "vfs_test_lock(9)"
name: "vfs_test_lock"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_test_lock/"
---

vfs_test_lock - test file byte range lock

<h2>Synopsis</h2>

<pre><code>int vfs_test_lock(struct file *filp, struct file_lock *fl);</code></pre>

<h2>Arguments</h2>

<i>filp</i>
<dl><dd><dd>The file to test lock for</dl>
 

 <i>fl</i>
<dl><dd>The lock to test; also used to hold result</dl>

<h2>Description</h2>

Returns -ERRNO on failure. Indicates presence of conflicting lock by setting conf-&gt;fl_type to something other than F_UNLCK.

<h2>Copyright</h2>


