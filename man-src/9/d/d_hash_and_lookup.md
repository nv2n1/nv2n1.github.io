---
title: "d_hash_and_lookup(9)"
name: "d_hash_and_lookup"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_hash_and_lookup/"
---

d_hash_and_lookup - hash the qstr then search for a dentry

<h2>Synopsis</h2>

<pre><code>struct dentry *d_hash_and_lookup(struct dentry *dir, struct qstr *name);</code></pre>

<h2>Arguments</h2>

<i>dir</i>
<dl><dd><dd>Directory to search in</dl>
 

 <i>name</i>
<dl><dd>qstr of name we wish to find</dl>

<h2>Description</h2>

On lookup failure NULL is returned; on bad name - ERR_PTR(-error)

<h2>Copyright</h2>


