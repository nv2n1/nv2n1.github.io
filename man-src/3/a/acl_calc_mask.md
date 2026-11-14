---
title: "acl_calc_mask(3)"
name: "acl_calc_mask"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_calc_mask/"
description: "acl_calc_mask – calculate the file group class mask"
---

<h2 class="name">NAME</h2>
<p> <code>acl_calc_mask</code> &#8211; calculate the file group class mask </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_calc_mask acl_t *acl_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_calc_mask function calculates and sets the permissions associated with the ACL_MASK ACL entry of the ACL referred to by <i>acl_p</i> The value of the new permissions is the union of the permissions granted by all entries of tag type ACL_GROUP, ACL_GROUP_OBJ, or ACL_USER. If the ACL referred to by <i>acl_p</i> already contains an ACL_MASK entry, its permissions are overwritten; if it does not contain an ACL_MASK entry, one is added. </p>
<p> If the ACL referred to by <i>acl_p</i> does not contain enough space for the new ACL entry, then additional working storage may be allocated. If the working storage cannot be increased in the current location, then it may be relocated and the previous working storage is released and a pointer to the new working storage is returned via <i>acl_p</i> </p>
<p> The order of existing entries in the ACL is undefined after this function. </p>
<p> Any existing ACL entry descriptors that refer to entries in the ACL continue to refer to those entries. Any existing ACL pointers that refer to the ACL referred to by <i>acl_p</i> continue to refer to the ACL.</p>
<h2>RETURN VALUE</h2>
<p> Rv -std acl_calc_mask</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_calc_mask function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The Fn acl_calc_mask function is unable to allocate the memory required for an ACL_MASK ACL entry.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_check3, acl_get_entry3, acl_valid3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
