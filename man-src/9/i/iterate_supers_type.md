---
title: "iterate_supers_type(9)"
name: "iterate_supers_type"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iterate_supers_type/"
---

iterate_supers_type - call function for superblocks of given type

<h2>Synopsis</h2>

<pre><code>void iterate_supers_type(struct file_system_type *type, void (*f)(struct super_block *, void *), void *arg);</code></pre>

<h2>Arguments</h2>

<i>type</i>
<dl><dd><dd>fs type</dl>
 

 <i>f</i>
<dl><dd>function to call</dl>
 

 <i>arg</i>
<dl><dd>argument to pass to it</dl>

<h2>Description</h2>

Scans the superblock list and calls given function, passing it locked superblock and given argument.

<h2>Copyright</h2>


