---
title: "inode_dio_wait(9)"
name: "inode_dio_wait"
section: "9"
letter: "i"
url: "/docs/linux/man/9-inode_dio_wait/"
---

inode_dio_wait - wait for outstanding DIO requests to finish

<h2>Synopsis</h2>

<pre><code>void inode_dio_wait(struct inode *inode);</code></pre>

<h2>Arguments</h2>

<i>inode</i>
<dl><dd><dd>inode to wait for</dl>

<h2>Description</h2>

Waits for all pending direct I/O requests to finish so that we can proceed with a truncate or equivalent operation. 

 Must be called under a lock that serializes taking new references to i_dio_count, usually by inode-&gt;i_mutex.

<h2>Copyright</h2>


