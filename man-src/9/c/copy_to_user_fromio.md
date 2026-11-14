---
title: "copy_to_user_fromio(9)"
name: "copy_to_user_fromio"
section: "9"
letter: "c"
url: "/docs/linux/man/9-copy_to_user_fromio/"
---

copy_to_user_fromio - copy data from mmio-space to user-space

<h2>Synopsis</h2>

<pre><code>int copy_to_user_fromio(void __user *dst, const volatile void __iomem *src, size_t count);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>the destination pointer on user-space</dl>
 

 <i>src</i>
<dl><dd>the source pointer on mmio</dl>
 

 <i>count</i>
<dl><dd>the data size to copy in bytes</dl>

<h2>Description</h2>

Copies the data from mmio-space to user-space.

<h2>Return</h2>

Zero if successful, or non-zero on failure.

<h2>Copyright</h2>


