---
title: "d_instantiate_no_diralias(9)"
name: "d_instantiate_no_diralias"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_instantiate_no_diralias/"
description: "d_instantiate_no_diralias – instantiate a non-aliased dentry"
---

<p>d_instantiate_no_diralias &#8211; instantiate a non-aliased dentry</p>
<h2>Synopsis</h2>
<pre><code>int d_instantiate_no_diralias(struct dentry *entry, struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>entry</i></p>
<dl>
<dd>
<dd>dentry to complete</dl>
<p> <i>inode</i></p>
<dl>
<dd>inode to attach to this dentry</dl>
<h2>Description</h2>
<p>Fill in inode information in the entry. If a directory alias is found, then return an error (and drop inode). Together with <code>d_materialise_unique</code> this guarantees that a directory inode may never have more than one alias.</p>
<h2>Copyright</h2>
