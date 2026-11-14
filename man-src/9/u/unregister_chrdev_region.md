---
title: "unregister_chrdev_region(9)"
name: "unregister_chrdev_region"
section: "9"
letter: "u"
url: "/docs/linux/man/9-unregister_chrdev_region/"
---

unregister_chrdev_region - unregister a range of device numbers

<h2>Synopsis</h2>

<pre><code>void unregister_chrdev_region(dev_t from, unsigned count);</code></pre>

<h2>Arguments</h2>

<i>from</i>
<dl><dd><dd>the first in the range of numbers to unregister</dl>
 

 <i>count</i>
<dl><dd>the number of device numbers to unregister</dl>

<h2>Description</h2>

This function will unregister a range of <i>count</i> device numbers, starting with <i>from</i>. The caller should normally be the one who allocated those numbers in the first place...

<h2>Copyright</h2>


