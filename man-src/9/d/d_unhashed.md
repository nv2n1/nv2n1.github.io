---
title: "d_unhashed(9)"
name: "d_unhashed"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_unhashed/"
---

d_unhashed - is dentry hashed

<h2>Synopsis</h2>

<pre><code>int d_unhashed(const struct dentry *dentry);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>entry to check</dl>

<h2>Description</h2>

Returns true if the dentry passed is not currently hashed.

<h2>Copyright</h2>


