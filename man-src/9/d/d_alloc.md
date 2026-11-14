---
title: "d_alloc(9)"
name: "d_alloc"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_alloc/"
description: "d_alloc – allocate a dcache entry"
---

<p>d_alloc &#8211; allocate a dcache entry</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *d_alloc(struct dentry *parent, const struct qstr *name);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>parent of entry to allocate</dl>
<p> <i>name</i></p>
<dl>
<dd>qstr of the name</dl>
<h2>Description</h2>
<p>Allocates a dentry. It returns <code>NULL</code> if there is insufficient memory available. On a success the dentry is returned. The name passed in is copied and the copy passed in may be reused after this call.</p>
<h2>Copyright</h2>
