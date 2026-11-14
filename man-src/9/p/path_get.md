---
title: "path_get(9)"
name: "path_get"
section: "9"
letter: "p"
url: "/docs/linux/man/9-path_get/"
---

path_get - get a reference to a path

<h2>Synopsis</h2>

<pre><code>void path_get(const struct path *path);</code></pre>

<h2>Arguments</h2>

<i>path</i>
<dl><dd><dd>path to get the reference to</dl>

<h2>Description</h2>

Given a path increment the reference count to the dentry and the vfsmount.

<h2>Copyright</h2>


