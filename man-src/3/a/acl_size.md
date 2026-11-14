---
title: "acl_size(3)"
name: "acl_size"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_size/"
description: "acl_size – get the size of the external representation of an ACL"
---

<h2 class="name">NAME</h2>
<p> <code>acl_size</code> &#8211; get the size of the external representation of an ACL </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft ssize_t Fn acl_size acl_t acl</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_size function return the size, in bytes, of the buffer required to hold the exportable, contiguous, persistent form of the ACL pointed to by the argument <i>acl</i> when converted by Fn acl_copy_ext . </p>
<p> Any existing ACL entry descriptors that refer to entries in <i>acl</i> continue to refer to the same entries. Any existing ACL pointers that refer to the ACL referred to by <i>acl</i> continue to refer to the ACL. The order of ACL entries within <i>acl</i> remains unchanged.</p>
<h2>RETURN VALUE</h2>
<p> On success, the Fn acl_size function returns the size in bytes of the contiguous, persistent form of the ACL. On error, a value of <code>(ssize_t)-1</code> is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_size function returns a value of <code>(ssize_t)-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_copy_ext3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
