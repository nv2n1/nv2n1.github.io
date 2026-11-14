---
title: "path_put(9)"
name: "path_put"
section: "9"
letter: "p"
url: "/docs/linux/man/9-path_put/"
---

path_put - put a reference to a path

<h2>Synopsis</h2>

<pre><code>void path_put(const struct path *path);</code></pre>

<h2>Arguments</h2>

<i>path</i>
<dl><dd><dd>path to put the reference to</dl>

<h2>Description</h2>

Given a path decrement the reference count to the dentry and the vfsmount.

<h2>Copyright</h2>


