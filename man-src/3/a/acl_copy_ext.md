---
title: "acl_copy_ext(3)"
name: "acl_copy_ext"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_copy_ext/"
description: "acl_copy_ext – copy an ACL from internal to external representation"
---

<h2 class="name">NAME</h2>
<p> <code>acl_copy_ext</code> &#8211; copy an ACL from internal to external representation </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft ssize_t Fn acl_copy_ext void *buf_p acl_t acl ssize_t size</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_copy_ext function copies the ACL pointed to by <i>acl</i> from system-managed space to the user managed space pointed to by <i>buf_p</i> The <i>size</i> parameter represents the size in bytes of the buffer pointed to by <i>buf_p</i> The format of the ACL placed in the buffer pointed to by <i>buf_p</i> is a contiguous, persistent data item, the format of which is unspecified. It is the responsibility of the invoker to allocate an area large enough to hold the copied ACL. The size of the exportable, contiguous, persistent form of the ACL may be obtained by invoking the Fn acl_size function. </p>
<p> Any ACL entry descriptors that refer to an entry in the ACL referenced by <i>acl</i> continue to refer to those entries. Any existing ACL pointers that refer to the ACL referenced by <i>acl</i> continue to refer to the ACL.</p>
<h2>RETURN VALUE</h2>
<p> Upon success, this function returns the number of bytes placed in the buffer pointed to by <i>buf_p</i> On error, a value of <code>(ssize_t)-1</code> is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_copy_ext function returns a value of <code>(ssize_t)-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The <i>size</i> parameter is zero or negative. </p>
<p> The argument <i>acl</i> is not a valid pointer to an ACL. </p>
<p> The ACL referenced by <i>acl</i> contains one or more improperly formed ACL entries, or for some other reason cannot be translated into the external form of an ACL.</p>
<dt><code>Bq </code>Er ERANGE</p>
<dd> The <i>size</i> parameter is greater than zero but smaller than the length of the contiguous, persistent form of the ACL.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_copy_int3, acl_size3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
