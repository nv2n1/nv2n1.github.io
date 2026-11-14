---
title: "lock_two_nondirectories(9)"
name: "lock_two_nondirectories"
section: "9"
letter: "l"
url: "/docs/linux/man/9-lock_two_nondirectories/"
---

lock_two_nondirectories - take two i_mutexes on non-directory objects

<h2>Synopsis</h2>

<pre><code>void lock_two_nondirectories(struct inode *inode1, struct inode *inode2);</code></pre>

<h2>Arguments</h2>

<i>inode1</i>
<dl><dd><dd>first inode to lock</dl>
 

 <i>inode2</i>
<dl><dd>second inode to lock</dl>

<h2>Description</h2>

Lock any non-NULL argument that is not a directory. Zero, one or two objects may be locked by this function.

<h2>Copyright</h2>


