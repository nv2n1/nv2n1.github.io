---
title: "copy_from_user_toio(9)"
name: "copy_from_user_toio"
section: "9"
letter: "c"
url: "/docs/linux/man/9-copy_from_user_toio/"
---

copy_from_user_toio - copy data from user-space to mmio-space

<h2>Synopsis</h2>

<pre><code>int copy_from_user_toio(volatile void __iomem *dst, const void __user *src, size_t count);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>the destination pointer on mmio-space</dl>
 

 <i>src</i>
<dl><dd>the source pointer on user-space</dl>
 

 <i>count</i>
<dl><dd>the data size to copy in bytes</dl>

<h2>Description</h2>

Copies the data from user-space to mmio-space.

<h2>Return</h2>

Zero if successful, or non-zero on failure.

<h2>Copyright</h2>


