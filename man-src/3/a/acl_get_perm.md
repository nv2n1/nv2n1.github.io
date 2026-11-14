---
title: "acl_get_perm(3)"
name: "acl_get_perm"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_get_perm/"
description: "acl_get_perm – test for a permission in an ACL permission set"
---

<h2 class="name">NAME</h2>
<p> <code>acl_get_perm</code> &#8211; test for a permission in an ACL permission set </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft int Fn acl_get_perm acl_permset_t permset_d acl_perm_t perm</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_get_perm function tests if the permission specified by the argument <i>perm</i> is contained in the ACL permission set pointed to by the argument <i>permset_d</i> </p>
<p> Any existing descriptors that refer to <i>permset_d</i> continue to refer to that permission set.</p>
<h2>RETURN VALUE</h2>
<p> If successful, the Fn acl_get_perm function returns <code>1</code> if the permission specified by <i>perm</i> is contained in the ACL permission set <i>permset_d</i> and <code>0</code> if the permission is not contained in the permission set. Otherwise, the value <code>-1</code> is returned and the global variable <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_get_perm function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>permset_d</i> is not a valid descriptor for a permission set within an ACL entry. </p>
<p> The argument <i>perm</i> is not a valid <i>acl_perm_t</i> value.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> acl_add_perm3, acl_clear_perms3, acl_delete_perm3, acl_get_permset3, acl_set_permset3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
