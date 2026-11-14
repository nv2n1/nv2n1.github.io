---
title: "acl_check(3)"
name: "acl_check"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_check/"
description: "acl_check – check an ACL for validity"
---

<h2 class="name">NAME</h2>
<p> <code>acl_check</code> &#8211; check an ACL for validity </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_check acl_t acl int *last</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_check function checks the ACL referred to by the argument <i>acl</i> for validity. </p>
<p> The three required entries ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER must exist exactly once in the ACL. If the ACL contains any ACL_USER or ACL_GROUP entries, then an ACL_MASK entry is also required. The ACL may contain at most one ACL_MASK entry. </p>
<p> The user identifiers must be unique among all entries of type ACL_USER. The group identifiers must be unique among all entries of type ACL_GROUP. </p>
<p> If the ACL referred to by <i>acl</i> is invalid, Fn acl_check returns a positive error code that indicates which type of error was detected. The following symbolic error codes are defined:</p>
<dl>
<dt><code>ACL_MULTI_ERROR</code></p>
<dd> The ACL contains multiple entries that have a tag type that may occur at most once.</p>
<dt><code>ACL_DUPLICATE_ERROR</code></p>
<dd> The ACL contains multiple ACL_USER entries with the same user ID, or multiple ACL_GROUP entries with the same group ID.</p>
<dt><code>ACL_MISS_ERROR</code></p>
<dd> A required entry is missing.</p>
<dt><code>ACL_ENTRY_ERROR</code></p>
<dd> The ACL contains an invalid entry tag type.</dl>
<p> The Fn acl_error function can be used to translate error codes to text messages. </p>
<p> In addition, if the pointer <i>last</i> is not <code>NULL</code> Fn acl_check assigns the number of the ACL entry at which the error was detected to the value pointed to by <i>last</i> Entries are numbered starting with zero, in the order in which they would be returned by the Fn acl_get_entry function.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the Fn acl_check function returns <code>0</code> if the ACL referred to by <i>acl</i> is valid, and a positive error code if the ACL is invalid. Otherwise, a value of <code>-1</code> is returned and the global variable <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_check function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> acl_valid3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
