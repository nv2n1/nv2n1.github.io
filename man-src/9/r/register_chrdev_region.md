---
title: "register_chrdev_region(9)"
name: "register_chrdev_region"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_chrdev_region/"
---

register_chrdev_region - register a range of device numbers

<h2>Synopsis</h2>

<pre><code>int register_chrdev_region(dev_t from, unsigned count, const char *name);</code></pre>

<h2>Arguments</h2>

<i>from</i>
<dl><dd><dd>the first in the desired range of device numbers; must include the major number.</dl>
 

 <i>count</i>
<dl><dd>the number of consecutive device numbers required</dl>
 

 <i>name</i>
<dl><dd>the name of the device or driver.</dl>

<h2>Description</h2>

Return value is zero on success, a negative error code on failure.

<h2>Copyright</h2>


