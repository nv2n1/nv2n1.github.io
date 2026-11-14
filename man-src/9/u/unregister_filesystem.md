---
title: "unregister_filesystem(9)"
name: "unregister_filesystem"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unregister_filesystem/"
---

unregister_filesystem - unregister a file system

<h2>Synopsis</h2>

<pre><code>int unregister_filesystem(struct file_system_type *fs);</code></pre>

<h2>Arguments</h2>

<i>fs</i>
<dl><dd><dd>filesystem to unregister</dl>

<h2>Description</h2>

Remove a file system that was previously successfully registered with the kernel. An error is returned if the file system is not found. Zero is returned on a success. 

 Once this function has returned the struct file_system_type structure may be freed or reused.

<h2>Copyright</h2>


