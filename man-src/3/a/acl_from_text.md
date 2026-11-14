---
title: "acl_from_text(3)"
name: "acl_from_text"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_from_text/"
description: "acl_from_text – create an ACL from text"
---

<h2 class="name">NAME</h2>
<p> <code>acl_from_text</code> &#8211; create an ACL from text </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft acl_t Fn acl_from_text const char *buf_p</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_from_text function converts the text form of the ACL referred to by <i>buf_p</i> into the internal form of an ACL and returns a pointer to the working storage that contains the ACL. The Fn acl_from_text function accepts as input the long text form and short text form of an ACL as described in <a href="/docs/linux/man/5-acl/">acl</a>(5). </p>
<p> This function may cause memory to be allocated. The caller should free any releasable memory, when the new ACL is no longer required, by calling acl_free3 with the <i>(void*)acl_t</i> returned by Fn acl_from_text as an argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns a pointer to the working storage. On error, a value of <code>(acl_t)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_from_text function returns a value of <code>(acl_t)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument <i>buf_p</i> cannot be translated into an ACL.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The <i>acl_t</i> to be returned requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_free3, acl_get_entry3, Xw acl_to_text 3 , <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
