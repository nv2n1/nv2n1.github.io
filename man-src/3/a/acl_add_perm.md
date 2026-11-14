---
title: "acl_add_perm(3)"
name: "acl_add_perm"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_add_perm/"
description: "acl_add_perm – add a permission to an ACL permission set"
---

<h2 class="name">NAME</h2>
<p> <code>acl_add_perm</code> &#8211; add a permission to an ACL permission set </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_add_perm acl_permset_t permset_d acl_perm_t perm</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_add_perm function adds the permission contained in the argument <i>perm</i> to the permission set referred to by the argument <i>permset_d</i> An attempt to add a permission that is already contained in the permission set is not considered an error. </p>
<p> Any existing descriptors that refer to <i>permset_d</i> continue to refer to that permission set.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_add_perm</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_add_perm function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>permset_d</i> is not a valid descriptor for a permission set within an ACL entry. </p>
<p> The argument <i>perm</i> does not contain a valid <i>acl_perm_t</i> value.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_clear_perms3, acl_delete_perm3, acl_get_perm3, acl_get_permset3, acl_set_permset3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
