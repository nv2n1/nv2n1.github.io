---
title: "have_submounts(9)"
name: "have_submounts"
section: "9"
letter: "h"
url: "/docs/linux/man/9-have_submounts/"
---

have_submounts - check for mounts over a dentry

<h2>Synopsis</h2>

<pre><code>int have_submounts(struct dentry *parent);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>dentry to check.</dl>

<h2>Description</h2>

Return true if the parent or its subdirectories contain a mount point

<h2>Copyright</h2>


