---
title: "acl_get_qualifier(3)"
name: "acl_get_qualifier"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_get_qualifier/"
description: "acl_get_qualifier – retrieve the qualifier from an ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_get_qualifier</code> &#8211; retrieve the qualifier from an ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft void * Fn acl_get_qualifier acl_entry_t entry_d</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_get_qualifier function retrieves the qualifier from the ACL entry indicated by the argument <i>entry_d</i> into working storage and returns a pointer to that storage. </p>
<p> If the value of the tag type in the ACL entry referred to by <i>entry_d</i> is ACL_USER, then the value returned by Fn acl_get_qualifier is a pointer to type <i>uid_t</i> If the value of the tag type in the ACL entry referred to by <i>entry_d</i> is ACL_GROUP, then the value returned by Fn acl_get_qualifier is a pointer to type <i>gid_t</i> If the tag type in the ACL entry referred to by <i>entry_d</i> is a tag type for which a qualifier is not supported, Fn acl_get_qualifier returns a value of <code>(void *)NULL</code> and the function fails. Subsequent operations using the returned pointer operate on an independent copy of the qualifier in working storage, and will not change the qualifier of the ACL entry. </p>
<p> This function may cause memory to be allocated. The caller should free any releasable memory, when the new qualifier is no longer required, by calling Fn acl_free with the <i>void</i> value returned by Fn acl_get_qualifier as an argument. </p>
<p> The argument <i>entry_d</i> and any other ACL entry descriptors that refer to entries within the ACL containing the entry referred to by <i>entry_d</i> continue to refer to those entries. The order of all existing entries in the ACL containing the entry referred to by <i>entry_d</i> remains unchanged.</p>
<h2>RETURN VALUE</h2>
<p> On success, the function returns a pointer to the tag qualifier that was retrieved into ACL working storage. On error, a value of <code>(void *)NULL</code> is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_get_qualifier function returns <code>(void *)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>entry_d</i> is not a valid descriptor for an ACL entry. </p>
<p> The value of the tag type in the ACL entry referenced by the argument <i>entry_d</i> is neither ACL_USER nor ACL_GROUP.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The value to be returned requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_create_entry3, acl_free3, acl_get_entry3, acl_get_permset3, acl_get_tag_type3, acl_set_permset3, acl_set_qualifier3, acl_set_tag_type3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
