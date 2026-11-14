---
title: "acl_equiv_mode(3)"
name: "acl_equiv_mode"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_equiv_mode/"
description: "acl_equiv_mode – check for an equivalent ACL"
---

<h2 class="name">NAME</h2>
<p> <code>acl_equiv_mode</code> &#8211; check for an equivalent ACL </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_equiv_mode acl_t acl mode_t *mode_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_equiv_mode function checks if the ACL pointed to by the argument <i>acl</i> contains only the required ACL entries of tag types ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER, and contains no permissions other that ACL_READ, ACL_WRITE or ACL_EXECUTE. If the ACL has this form, it can can be fully represented with the traditional file permission bits, and is considered equivalent with the traditional file permission bits. </p>
<p> If <i>acl</i> is an equivalent ACL and the pointer <i>mode_p</i> is not <code>NULL , </code> the value pointed to by <i>mode_p</i> is set to the value that defines the same owner, group and other permissions as contained in the ACL.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns the value <code>0</code> if <i>acl</i> is an equivalent ACL, and the value <code>1</code> if <i>acl</i> is not an equivalent ACL. On error, the value <code>-1</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_equiv_mode function returns the value <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> acl_from_mode3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
