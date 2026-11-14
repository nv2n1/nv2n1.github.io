---
title: "acl_delete_entry(3)"
name: "acl_delete_entry"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_delete_entry/"
description: "acl_delete_entry – delete an ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_delete_entry</code> &#8211; delete an ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_delete_entry acl_t acl acl_entry_t entry_d</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_delete_entry function removes the ACL entry indicated by the <i>entry_d</i> descriptor from the ACL pointed to by <i>acl</i> Any existing ACL entry descriptors that refer to entries in <i>acl</i> other than that referred to by <i>entry_d</i> continue to refer to the same entries. The argument <i>entry_d</i> and any other ACL entry descriptors that refer to the same ACL entry are undefined after this function completes. Any existing ACL pointers that refer to the ACL referred to by <i>acl</i> continue to refer to the ACL.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_delete_entry</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_delete_entry function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl_p</i> is not a valid pointer to an ACL. </p>
<p> The argument <i>entry_d</i> is not a valid pointer to an ACL entry.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_copy_entry3, acl_create_entry3, acl_get_entry3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
