---
title: "acl_copy_int(3)"
name: "acl_copy_int"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_copy_int/"
description: "acl_copy_int – copy an ACL from external to internal representation"
---

<h2 class="name">NAME</h2>
<p> <code>acl_copy_int</code> &#8211; copy an ACL from external to internal representation </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft acl_t Fn acl_copy_int const void *buf_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_copy_int function copies an exportable, contiguous, persistent form of an ACL, pointed to by <i>buf_p</i> to the internal representation. </p>
<p> This function may cause memory to be allocated. The caller should free any releasable memory, when the new ACL is no longer required, by calling acl_free3 with the <i>(void*)acl_t</i> returned by Fn acl_copy_int as an argument.</p>
<h2>RETURN VALUE</h2>
<p> Upon success, the Fn acl_copy_int function returns a pointer that references the ACL in working storage. On error, a value of <code>(acl_t)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_copy_int function returns a value of <code>(acl_t)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The buffer pointed to by the argument <i>buf_p</i> does not contain a valid external form ACL.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The ACL working storage requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_copy_ext3, acl_get_entry3, acl_free3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
