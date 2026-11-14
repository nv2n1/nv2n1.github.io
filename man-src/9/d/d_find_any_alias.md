---
title: "d_find_any_alias(9)"
name: "d_find_any_alias"
section: "9"
letter: "d"
url: "/docs/linux/man/9-d_find_any_alias/"
description: "d_find_any_alias – find any alias for a given inode"
---

<p>d_find_any_alias &#8211; find any alias for a given inode</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *d_find_any_alias(struct inode *inode);</code></pre>
<h2>Arguments</h2>
<p><i>inode</i></p>
<dl>
<dd>
<dd>inode to find an alias for</dl>
<h2>Description</h2>
<p>If any aliases exist for the given inode, take and return a reference for one of them. If no aliases exist, return <code>NULL</code>.</p>
<h2>Copyright</h2>
