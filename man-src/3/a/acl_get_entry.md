---
title: "acl_get_entry(3)"
name: "acl_get_entry"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_get_entry/"
description: "acl_get_entry – get an ACL entry"
---

<h2 class="name">NAME</h2>
<p> <code>acl_get_entry</code> &#8211; get an ACL entry </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft int Fn acl_get_entry acl_t acl int entry_id acl_entry_t *entry_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_get_entry function obtains a descriptor for an ACL entry as specified by <i>entry_id</i> within the ACL indicated by the argument <i>acl</i> If the value of <i>entry_id</i> is ACL_FIRST_ENTRY, then the function returns in <i>entry_p</i> a descriptor for the first ACL entry within <i>acl</i> If the value of <i>entry_id </i> is ACL_NEXT_ENTRY, then the function returns in <i>entry_p </i> a descriptor for the next ACL entry within <i>acl</i> </p>
<p> If a call is made to Fn acl_get_entry with <i>entry_id</i> set to ACL_NEXT_ENTRY when there has not been either an initial successful call to Fn acl_get_entry , or a previous successful call to Fn acl_get_entry following a call to Fn acl_calc_mask , Fn acl_copy_int , Fn acl_create_entry , Fn acl_delete_entry , Fn acl_dup , Fn acl_from_text , Fn acl_get_fd , Fn acl_get_file , Fn acl_set_fd , Fn acl_set_file , or Fn acl_valid , then the effect is unspecified. </p>
<p> Calls to Fn acl_get_entry do not modify any ACL entries. Subsequent operations using the returned ACL entry descriptor operate on the ACL entry within the ACL in working storage. The order of all existing entries in the ACL remains unchanged. Any existing ACL entry descriptors that refer to entries within the ACL continue to refer to those entries. Any existing ACL pointers that refer to the ACL referred to by <i>acl</i> continue to refer to the ACL.</p>
<h2>RETURN VALUE</h2>
<p> If the function successfully obtains an ACL entry, the function returns a value of <code>1</code> If the ACL has no ACL entries, the function returns the value <code>0</code> If the value of <i>entry_id</i> is ACL_NEXT_ENTRY and the last ACL entry in the ACL has already been returned by a previous call to Fn acl_get_entry , the function returns the value <code>0</code> until a successful call with an <i>entry_id</i> of ACL_FIRST_ENTRY is made. Otherwise, the value <code>-1</code> is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_get_entry function returns <code>-1</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl_p</i> is not a valid pointer to an ACL. </p>
<p> The argument <i>entry_id</i> is neither ACL_NEXT_ENTRY nor ACL_FIRST_ENTRY.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_calc_mask3, acl_create_entry3, acl_copy_entry3, acl_delete_entry3, acl_get_file3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
