---
title: "acl_get_tag_type(3)"
name: "acl_get_tag_type"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_get_tag_type/"
description: "acl_get_tag_type – get the tag type of an ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_get_tag_type</code> &#8211; get the tag type of an ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_get_tag_type acl_entry_t entry_d acl_tag_t *tag_type_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_get_tag_type function assigns to the value pointed to by <i>tag_type_p</i> the tag type for the ACL entry indicated by the argument <i>entry_d</i> </p>
<p> The argument <i>entry_d</i> and any other ACL entry descriptors that refer to entries in the same ACL continue to refer to those entries. The order of all existing entries in the ACL remain unchanged.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_get_tag_type</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_get_tag_type function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>entry_d</i> is not a valid descriptor for an ACL entry.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_create_entry3, acl_get_entry3, acl_get_permset3, acl_get_qualifier3, acl_set_permset3, acl_set_qualifier3, acl_set_tag_type3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
