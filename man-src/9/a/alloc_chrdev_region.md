---
title: "alloc_chrdev_region(9)"
name: "alloc_chrdev_region"
section: "9"
letter: "a"
url: "/docs/linux/man/9-alloc_chrdev_region/"
---

alloc_chrdev_region - register a range of char device numbers

<h2>Synopsis</h2>

<pre><code>int alloc_chrdev_region(dev_t *dev, unsigned baseminor, unsigned count, const char *name);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>output parameter for first assigned number</dl>
 

 <i>baseminor</i>
<dl><dd>first of the requested range of minor numbers</dl>
 

 <i>count</i>
<dl><dd>the number of minor numbers required</dl>
 

 <i>name</i>
<dl><dd>the name of the associated device or driver</dl>

<h2>Description</h2>

Allocates a range of char device numbers. The major number will be chosen dynamically, and returned (along with the first minor number) in <i>dev</i>. Returns zero or a negative error code.

<h2>Copyright</h2>


