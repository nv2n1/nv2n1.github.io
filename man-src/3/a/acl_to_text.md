---
title: "acl_to_text(3)"
name: "acl_to_text"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_to_text/"
description: "acl_to_text – convert an ACL to text"
---

<h2 class="name">NAME</h2>
<p> <code>acl_to_text</code> &#8211; convert an ACL to text </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft char * Fn acl_to_text acl_t acl ssize_t *len_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_to_text function translates the ACL pointed to by the argument <i>acl</i> into a <code>NULL</code> terminated character string. If the pointer <i>len_p</i> is not <code>NULL</code> then the function returns the length of the string (not including the <code>NULL</code> terminator) in the location pointed to by <i>len_p</i> The format of the text string returned by Fn acl_to_text is the long text form defined in <a href="/docs/linux/man/5-acl/">acl</a>(5). The ACL referred to by <i>acl</i> is not changed. </p>
<p> This function allocates any memory necessary to contain the string and returns a pointer to the string. The caller should free any releasable memory, when the new string is no longer required, by calling acl_free3 with the <i>(void*)char</i> returned by Fn acl_to_text as an argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns a pointer to the long text form of the ACL. On error, a value of <code>(char *)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_to_text function returns a value of <code>(char *)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>acl</i> is not a valid pointer to an ACL. </p>
<p> The ACL referenced by <i>acl</i> contains one or more improperly formed ACL entries, or for some other reason cannot be translated into a text form of an ACL.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The character string to be returned requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_free3, Xw acl_from_text 3 , acl_to_any_text3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
