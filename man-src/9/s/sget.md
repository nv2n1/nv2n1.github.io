---
title: "sget(9)"
name: "sget"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sget/"
---

sget - find or create a superblock

<h2>Synopsis</h2>

<pre><code>struct super_block *sget(struct file_system_type *type, int (*test)(struct super_block *, void *), int (*set)(struct super_block *, void *), int flags, void *data);</code></pre>

<h2>Arguments</h2>

<i>type</i>
<dl><dd><dd>filesystem type superblock should belong to</dl>
 

 <i>test</i>
<dl><dd>comparison callback</dl>
 

 <i>set</i>
<dl><dd>setup callback</dl>
 

 <i>flags</i>
<dl><dd>mount flags</dl>
 

 <i>data</i>
<dl><dd>argument to each of them</dl>

<h2>Copyright</h2>


