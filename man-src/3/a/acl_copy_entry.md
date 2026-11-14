---
title: "acl_copy_entry(3)"
name: "acl_copy_entry"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_copy_entry/"
description: "acl_copy_entry – copy an ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_copy_entry</code> &#8211; copy an ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_copy_entry acl_entry_t dest_d acl_entry_t src_d</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_copy_entry function copies the contents of the ACL entry indicated by the <i>src_d</i> descriptor to the existing ACL entry indicated by the <i>dest_d</i> descriptor. The <i>src_d</i> and <i>dest_d</i> descriptors may refer to entries in different ACLs.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_copy_entry</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_copy_entry function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>src_d</i> or <i>dest_d</i> is not a valid descriptor for an ACL entry. </p>
<p> The arguments <i>src_d</i> and <i>dest_d</i> reference the same ACL entry.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_get_entry3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
