---
title: "d_invalidate(9)"
name: "d_invalidate"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_invalidate/"
---

d_invalidate - detach submounts, prune dcache, and drop

<h2>Synopsis</h2>

<pre><code>void d_invalidate(struct dentry *dentry);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>dentry to invalidate (aka detach, prune and drop)</dl>

<h2>Description</h2>

no dcache lock. 

 The final d_drop is done as an atomic operation relative to rename_lock ensuring there are no races with d_set_mounted. This ensures there are no unhashed dentries on the path to a mountpoint.

<h2>Copyright</h2>


