---
title: "acl_delete_perm(3)"
name: "acl_delete_perm"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_delete_perm/"
description: "acl_delete_perm – delete a permission from an ACL permission set"
---

<h2 class="name">NAME</h2>
<p> <code>acl_delete_perm</code> &#8211; delete a permission from an ACL permission set </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_delete_perm acl_permset_t permset_d acl_perm_t perm</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_delete_perm function deletes the permission contained in the argument <i>perm</i> from the permission set referred to by the argument <i>permset_d</i> An attempt to delete a permission that is not contained in the permission set is not considered an error. </p>
<p> Any existing descriptors that refer to <i>permset_d</i> continue to refer to that permission set.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_delete_perm</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_delete_perm function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>permset_d</i> is not a valid descriptor for a permission set within an ACL entry. </p>
<p> The argument <i>perm</i> does not contain a valid <i>acl_perm_t</i> value.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_add_perm3, acl_clear_perms3, acl_get_perm3, acl_get_permset3, acl_set_permset3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
