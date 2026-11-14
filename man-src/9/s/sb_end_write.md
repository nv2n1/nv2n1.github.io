---
title: "sb_end_write(9)"
name: "sb_end_write"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sb_end_write/"
---

sb_end_write - drop write access to a superblock

<h2>Synopsis</h2>

<pre><code>void sb_end_write(struct super_block *sb);</code></pre>

<h2>Arguments</h2>

<i>sb</i>
<dl><dd><dd>the super we wrote to</dl>

<h2>Description</h2>

Decrement number of writers to the filesystem. Wake up possible waiters wanting to freeze the filesystem.

<h2>Copyright</h2>


