---
title: "bitmap_parselist_user(9)"
name: "bitmap_parselist_user"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_parselist_user/"
description: "bitmap_parselist_user –"
---

<p>bitmap_parselist_user &#8211;</p>
<h2>Synopsis</h2>
<pre><code>int bitmap_parselist_user(const char __user *ubuf, unsigned int ulen, unsigned long *maskp, int nmaskbits);</code></pre>
<h2>Arguments</h2>
<p><i>ubuf</i></p>
<dl>
<dd>
<dd>pointer to user buffer containing string.</dl>
<p> <i>ulen</i></p>
<dl>
<dd>buffer size in bytes. If string is smaller than this then it must be terminated with a 
