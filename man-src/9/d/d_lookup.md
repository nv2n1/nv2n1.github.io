---
title: "d_lookup(9)"
name: "d_lookup"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_lookup/"
description: "d_lookup – search for a dentry"
---

<p>d_lookup &#8211; search for a dentry</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *d_lookup(const struct dentry *parent, const struct qstr *name);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>parent dentry</dl>
<p> <i>name</i></p>
<dl>
<dd>qstr of name we wish to find</dl>
<h2>Return</h2>
<p>dentry, or NULL </p>
<p> d_lookup searches the children of the parent dentry for the name in question. If the dentry is found its reference count is incremented and the dentry is returned. The caller must use dput to free the entry when it has finished using it. <code>NULL</code> is returned if the dentry does not exist.</p>
<h2>Copyright</h2>
