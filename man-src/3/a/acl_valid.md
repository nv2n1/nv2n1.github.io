---
title: "acl_valid(3)"
name: "acl_valid"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_valid/"
description: "acl_valid – validate an ACL"
---

<h2 class="name">NAME</h2>
<p> <code>acl_valid</code> &#8211; validate an ACL </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_valid acl_t acl</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_valid function checks the ACL referred to by the argument <i>acl</i> for validity. </p>
<p> The three required entries ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER must exist exactly once in the ACL. If the ACL contains any ACL_USER or ACL_GROUP entries, then an ACL_MASK entry is also required. The ACL may contain at most one ACL_MASK entry. </p>
<p> The user identifiers must be unique among all entries of type ACL_USER. The group identifiers must be unique among all entries of type ACL_GROUP.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_valid</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_valid function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL. </p>
<p> The argument <i>acl</i> does not point to a valid ACL. </p>
<p> One or more of the required ACL entries is not present in <i>acl</i> </p>
<p> The ACL contains entries that are not unique.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_check3, acl_set_file3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
