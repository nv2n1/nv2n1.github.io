---
title: "acl_create_entry(3)"
name: "acl_create_entry"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_create_entry/"
description: "acl_create_entry – create a new ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_create_entry</code> &#8211; create a new ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_create_entry acl_t *acl_p acl_entry_t *entry_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_create_entry function creates a new ACL entry in the ACL pointed to by the contents of the pointer argument <i>acl_p</i> On success, the function returns a descriptor for the new ACL entry via <i>entry_p</i> </p>
<p> This function may cause memory to be allocated. The caller should free any releasable memory, when the new ACL is no longer required, by calling acl_free3 with <i>(void*)*acl_p</i> as an argument. If the ACL working storage cannot be increased in the current location, then the working storage for the ACL pointed to by <i>acl_p</i> may be relocated and the previous working storage is released. A pointer to the new working storage is returned via <i>acl_p</i> </p>
<p> The components of the new ACL entry are initialized in the following ways: the ACL tag type component contains ACL_UNDEFINED_TAG, the qualifier component contains ACL_UNDEFINED_ID, and the set of permissions has no permissions enabled. Any existing ACL entry descriptors that refer to entries in the ACL continue to refer to those entries.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_create_entry</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_create_entry function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl_p</i> is not a valid pointer to an ACL.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The ACL working storage requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_init3, acl_delete_entry3, acl_free3, acl_create_entry3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
