---
title: "dget_dlock(9)"
name: "dget_dlock"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dget_dlock/"
description: "dget_dlock – get a reference to a dentry"
---

<p>dget_dlock &#8211; get a reference to a dentry</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *dget_dlock(struct dentry *dentry);</code></pre>
<h2>Arguments</h2>
<p><i>dentry</i></p>
<dl>
<dd>
<dd>dentry to get a reference to</dl>
<h2>Description</h2>
<p>Given a dentry or <code>NULL</code> pointer increment the reference count if appropriate and return the dentry. A dentry will not be destroyed when it has references.</p>
<h2>Copyright</h2>
