---
title: "acl_clear_perms(3)"
name: "acl_clear_perms"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_clear_perms/"
description: "acl_clear_perms – clear all permissions from an ACL permission set"
---

<h2 class="name">NAME</h2>
<p> <code>acl_clear_perms</code> &#8211; clear all permissions from an ACL permission set </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_clear_perms acl_permset_t permset_d</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_clear_perms function clears all permissions from the permission set referred to by the argument <i>permset_d</i> </p>
<p> Any existing descriptors that refer to <i>permset_d</i> shall continue to refer to that permission set.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_clear_perms</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_clear_perms function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>permset_d</i> is not a valid descriptor for a permission set within an ACL entry.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_add_perm3, acl_delete_perm3, acl_get_perm3, acl_get_permset3, acl_set_permset3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
