---
title: "register_filesystem(9)"
name: "register_filesystem"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_filesystem/"
---

register_filesystem - register a new filesystem

<h2>Synopsis</h2>

<pre><code>int register_filesystem(struct file_system_type *fs);</code></pre>

<h2>Arguments</h2>

<i>fs</i>
<dl><dd><dd>the file system structure</dl>

<h2>Description</h2>

Adds the file system passed to the list of file systems the kernel is aware of for mount and other syscalls. Returns 0 on success, or a negative errno code on an error. 

 The struct file_system_type that is passed is linked into the kernel structures and must not be freed until the file system has been unregistered.

<h2>Copyright</h2>


