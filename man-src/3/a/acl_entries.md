---
title: "acl_entries(3)"
name: "acl_entries"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_entries/"
description: "acl_entries – return the number of entries in an ACL"
---

<h2 class="name">NAME</h2>
<p> <code>acl_entries</code> &#8211; return the number of entries in an ACL </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_entries acl_t acl</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_entries function returns the number of ACL entries that are contained in the ACL referred to by the argument <i>acl</i></p>
<h2>RETURN VALUE</h2>
<p> The Fn acl_entries function returns the number of entries in <i>acl</i> if successful; otherwise the value <code>-1</code> is returned and the global variable <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_entries function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
