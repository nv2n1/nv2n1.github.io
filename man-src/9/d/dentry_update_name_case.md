---
title: "dentry_update_name_case(9)"
name: "dentry_update_name_case"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dentry_update_name_case/"
---

dentry_update_name_case - update case insensitive dentry with a new name

<h2>Synopsis</h2>

<pre><code>void dentry_update_name_case(struct dentry *dentry, const struct qstr *name);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>dentry to be updated</dl>
 

 <i>name</i>
<dl><dd>new name</dl>

<h2>Description</h2>

Update a case insensitive dentry with new case of name. 

 dentry must have been returned by d_lookup with name <i>name</i>. Old and new name lengths must match (ie. no d_compare which allows mismatched name lengths). 

 Parent inode i_mutex must be held over d_lookup and into this call (to keep renames and concurrent inserts, and <a HREF="/docs/linux/man/2-readdir/">readdir</a>(2) away).

<h2>Copyright</h2>


