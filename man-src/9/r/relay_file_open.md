---
title: "relay_file_open(9)"
name: "relay_file_open"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_file_open/"
---

relay_file_open - open file op for relay files

<h2>Synopsis</h2>

<pre><code>int relay_file_open(struct inode *inode, struct file *filp);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>the inode</dl>
 

 <i>filp</i>
<dl><dd>the file</dl>

<h2>Description</h2>

Increments the channel buffer refcount.

<h2>Copyright</h2>


