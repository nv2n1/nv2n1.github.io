---
title: "clear_user(9)"
name: "clear_user"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clear_user/"
---

clear_user - Zero a block of memory in user space.

<h2>Synopsis</h2>

<pre><code>unsigned long clear_user(void __user *to, unsigned long n);</code></pre>

<h2>Arguments</h2>

<i>to</i>
<dl><dd><dd>Destination address, in user space.</dl>
 

 <i>n</i>
<dl><dd>Number of bytes to zero.</dl>

<h2>Description</h2>

Zero a block of memory in user space. 

 Returns number of bytes that could not be cleared. On success, this will be zero.

<h2>Copyright</h2>


