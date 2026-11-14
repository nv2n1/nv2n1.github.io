---
title: "sock_release(9)"
name: "sock_release"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sock_release/"
---

sock_release - close a socket

<h2>Synopsis</h2>

<pre><code>void sock_release(struct socket *sock);</code></pre>

<h2>Arguments</h2>

<i>sock</i>
<dl><dd><dd>socket to close</dl>

<h2>Description</h2>

The socket is released from the protocol stack if it has a release callback, and the inode is then released if the socket is bound to an inode not a file.

<h2>Copyright</h2>


