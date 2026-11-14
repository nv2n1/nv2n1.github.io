---
title: "deactivate_locked_super(9)"
name: "deactivate_locked_super"
section: "9"
letter: "d"
url: "/docs/linux/man/9-deactivate_locked_super/"
---

deactivate_locked_super - drop an active reference to superblock

<h2>Synopsis</h2>

<pre><code>void deactivate_locked_super(struct super_block *s);</code></pre>

<h2>Arguments</h2>

<i>s</i>
<dl><dd><dd>superblock to deactivate</dl>

<h2>Description</h2>

Drops an active reference to superblock, converting it into a temporary one if there is no other active references left. In that case we tell fs driver to shut it down and drop the temporary reference we had just acquired. 

 Caller holds exclusive lock on superblock; that lock is released.

<h2>Copyright</h2>


