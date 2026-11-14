---
title: "sockfd_lookup(9)"
name: "sockfd_lookup"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sockfd_lookup/"
---

sockfd_lookup - Go from a file number to its socket slot

<h2>Synopsis</h2>

<pre><code>struct socket *sockfd_lookup(int fd, int *err);</code></pre>

<h2>Arguments</h2>

<i>fd</i>
<dl><dd><dd>file handle</dl>
 

 <i>err</i>
<dl><dd>pointer to an error code return</dl>

<h2>Description</h2>

The file handle passed in is locked and the socket it is bound too is returned. If an error occurs the err pointer is overwritten with a negative errno code and NULL is returned. The function checks for both invalid handles and passing a handle which is not a socket. 

 On a success the socket object pointer is returned.

<h2>Copyright</h2>


