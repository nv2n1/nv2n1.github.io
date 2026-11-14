---
title: "audit_compare_dname_path(9)"
name: "audit_compare_dname_path"
section: "9"
letter: "a"
url: "/docs/linux/man/9-audit_compare_dname_path/"
---

audit_compare_dname_path - compare given dentry name with last component in given path. Return of 0 indicates a match.

<h2>Synopsis</h2>

<pre><code>int audit_compare_dname_path(const char *dname, const char *path, int parentlen);</code></pre>

<h2>Arguments</h2>

<i>dname</i>
<dl><dd><dd>dentry name that we're comparing</dl>
 

 <i>path</i>
<dl><dd>full pathname that we're comparing</dl>
 

 <i>parentlen</i>
<dl><dd>length of the parent if known. Passing in AUDIT_NAME_FULL here indicates that we must compute this value.</dl>

<h2>Copyright</h2>


