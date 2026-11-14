---
title: "acl_free(3)"
name: "acl_free"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_free/"
description: "acl_free – release memory allocated to an ACL data object"
---

<h2 class="name">NAME</h2>
<p> <code>acl_free</code> &#8211; release memory allocated to an ACL data object </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_free void *obj_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_free function frees any releasable memory currently allocated by to the ACL data object identified by <i>obj_p</i> The argument <i>obj_p</i> may identify an ACL, an ACL entry qualifier, or a pointer to a string allocated by the Fn acl_to_text function.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_free</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_free function returns the value <code>-1</code> and and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The value of the argument <i>obj_p</i> is invalid.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_copy_int3, acl_create_entry3, acl_dup3, acl_from_text3, acl_get_fd, acl_get_file3, acl_init3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
