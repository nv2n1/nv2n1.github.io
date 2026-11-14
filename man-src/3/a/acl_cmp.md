---
title: "acl_cmp(3)"
name: "acl_cmp"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_cmp/"
description: "acl_cmp – compare two ACLs"
---

<h2 class="name">NAME</h2>
<p> <code>acl_cmp</code> &#8211; compare two ACLs </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_cmp acl_t acl1 acl_t acl2</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_cmp function compares the ACLs pointed to by the arguments <i>acl1</i> and <i>acl2</i> for equality. The two ACLs are considered equal if for each entry in <i>acl1</i> there is an entry in <i>acl2</i> with matching tag type, qualifier, and permissions, and vice versa.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the Fn acl_cmp function returns <code>0</code> if the two ACLs <i>acl1</i> and <i>acl2</i> are equal, and <code>1</code> if they differ. Otherwise, the value <code>-1</code> is returned and the global variable <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_cmp function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl1</i> is not a valid pointer to an ACL. </p>
<p> The argument <i>acl2</i> is not a valid pointer to an ACL.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
