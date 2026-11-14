---
title: "shrink_dcache_parent(9)"
name: "shrink_dcache_parent"
section: "9"
letter: "s"
url: "/docs/linux/man/9-shrink_dcache_parent/"
---

shrink_dcache_parent - prune dcache

<h2>Synopsis</h2>

<pre><code>void shrink_dcache_parent(struct dentry *parent);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>parent of entries to prune</dl>

<h2>Description</h2>

Prune the dcache to remove unused children of the parent dentry.

<h2>Copyright</h2>


