---
title: "acl_init(3)"
name: "acl_init"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_init/"
description: "acl_init – initialize ACL working storage"
---

<h2 class="name">NAME</h2>
<p> <code>acl_init</code> &#8211; initialize ACL working storage </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In sys/acl.h Ft acl_t Fn acl_init int count</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_init function allocates and initializes the working storage for an ACL of at least <i>count</i> ACL entries. The ACL created initially contains no ACL entries. A pointer to the working storage is returned. </p>
<p> This function may cause memory to be allocated. The caller should free any releasable memory, when the new ACL is no longer required, by calling acl_free3 with the <i>(void*)acl_t</i> returned by Fn acl_init as an argument.</p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns a pointer to the working storage. On error, a value of <code>(acl_t)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_init function returns a value of <code>(acl_t)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The value of count is less than zero.</p>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The <i>acl_t</i> to be returned requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned)</p>
<h2>SEE ALSO</h2>
<p> acl_get_file3, acl_free3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Derived from the FreeBSD manual pages written by An Robert N M Watson Aq rwatson [at] FreeBSD.org , and adapted for Linux by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
