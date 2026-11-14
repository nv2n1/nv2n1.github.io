---
title: "kernel_recvmsg(9)"
name: "kernel_recvmsg"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kernel_recvmsg/"
---

kernel_recvmsg - Receive a message from a socket (kernel space)

<h2>Synopsis</h2>

<pre><code>int kernel_recvmsg(struct socket *sock, struct msghdr *msg, struct kvec *vec, size_t num, size_t size, int flags);</code></pre>

<h2>Arguments</h2>

<i>sock</i>
<dl><dd><dd>The socket to receive the message from</dl>
 

 <i>msg</i>
<dl><dd>Received message</dl>
 

 <i>vec</i>
<dl><dd>Input s/g array for message data</dl>
 

 <i>num</i>
<dl><dd>Size of input s/g array</dl>
 

 <i>size</i>
<dl><dd>Number of bytes to read</dl>
 

 <i>flags</i>
<dl><dd>Message flags (MSG_DONTWAIT, etc...)</dl>

<h2>Description</h2>

On return the msg structure contains the scatter/gather array passed in the vec argument. The array is modified so that it consists of the unfilled portion of the original array. 

 The returned value is the total number of bytes received, or an error.

<h2>Copyright</h2>


