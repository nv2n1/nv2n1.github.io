---
title: "sock_alloc(9)"
name: "sock_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sock_alloc/"
---

sock_alloc - allocate a socket

<h2>Synopsis</h2>

<pre><code>struct socket *sock_alloc(void);</code></pre>

<h2>Arguments</h2>

<i>void</i>
<dl><dd><dd>no arguments</dl>

<h2>Description</h2>

Allocate a new inode and socket object. The two are bound together and initialised. The socket is then returned. If we are out of inodes NULL is returned.

<h2>Copyright</h2>


