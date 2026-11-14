---
title: "check_conflicting_open(9)"
name: "check_conflicting_open"
section: "9"
letter: "c"
url: "/docs/linux/man/9-check_conflicting_open/"
---

check_conflicting_open - see if the given dentry points to a file that has an existing open that would conflict with the desired lease.

<h2>Synopsis</h2>

<pre><code>int check_conflicting_open(const struct dentry *dentry, const long arg, int flags);</code></pre>

<h2>Arguments</h2>

<i>dentry</i>
<dl><dd><dd>dentry to check</dl>
 

 <i>arg</i>
<dl><dd>type of lease that we're trying to acquire</dl>
 

 <i>flags</i>
<dl><dd>current lock flags</dl>

<h2>Description</h2>

Check to see if there's an existing open fd on this file that would conflict with the lease we're trying to set.

<h2>Copyright</h2>


