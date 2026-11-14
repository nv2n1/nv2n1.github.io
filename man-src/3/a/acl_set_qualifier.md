---
title: "acl_set_qualifier(3)"
name: "acl_set_qualifier"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_set_qualifier/"
description: "acl_set_qualifier – set the qualifier of an ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_set_qualifier</code> &#8211; set the qualifier of an ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_set_qualifier acl_entry_t entry_d const void *qualifier_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_set_qualifier function sets the qualifier of the ACL entry indicated by the argument <i>entry_d</i> to the value referred to by the argument <i>qualifier_p</i> If the value of the tag type in the ACL entry referred to by <i>entry_d</i> is ACL_USER, then the value referred to by <i>qualifier_p</i> shall be of type <i>uid_t</i> If the value of the tag type in the ACL entry referred to by <i>entry_d</i> is ACL_GROUP, then the value referred to by <i>qualifier_p</i> shall be of type <i>gid_t</i> If the value of the tag type in the ACL entry referred to by <i>entry_d</i> is a tag type for which a qualifier is not supported, Fn acl_set_qualifier returns an error. </p>
<p> Any ACL entry descriptors that refer to the entry referred to by <i>entry_d</i> continue to refer to that entry. This function may cause memory to be allocated. The caller should free any releasable memory, when the ACL is no longer required, by calling Fn acl_free with a pointer to the ACL as argument.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_set_qualifier</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_set_qualifier function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>entry_d</i> is not a valid descriptor for an ACL entry. </p>
<p> The value of the tag type in the ACL entry referenced by the argument <i>entry_d</i> is neither ACL_USER nor ACL_GROUP. </p>
<p> The value pointed to by the argument <i>qualifier_p</i> is not valid.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The Fn acl_set_qualifier function is unable to allocate the memory required for the ACL qualifier.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_create_entry3, acl_free3, acl_get_permset3, acl_get_qualifier3, acl_get_tag_type3, acl_set_entry3, acl_set_permset3, acl_set_tag_type3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
