---
title: "acl_from_mode(3)"
name: "acl_from_mode"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_from_mode/"
description: "acl_from_mode – create an ACL from file permission bits"
---

<h2 class="name">NAME</h2>
<p> <code>acl_from_mode</code> &#8211; create an ACL from file permission bits </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft acl_t Fn acl_from_mode mode_t mode</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_from_mode function creates a minimal ACL that contains the three entries with tag types ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER, with permissions corresponding to the owner, group, and other permission bits of its argument <i>mode</i></p>
<h2>RETURN VALUE</h2>
<p> On success, this function returns a pointer to the working storage. On error, a value of <code>(acl_t)NULL</code> is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> If any of the following conditions occur, the Fn acl_from_mode function returns a value of <code>(acl_t)NULL</code> and sets <i>errno</i> to the corresponding value:</p>
<dl>
<dt><code>Bq </code>Er ENOMEM</p>
<dd> The ACL working storage requires more memory than is allowed by the hardware or system-imposed memory management constraints.</dl>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> acl_equiv_mode3, acl_get_file3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
