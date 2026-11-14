---
title: "acl_error(3)"
name: "acl_error"
section: "3"
letter: "a"
url: "/docs/linux/man/3-acl_error/"
description: "acl_error – convert an ACL error code to a text message"
---

<h2 class="name">NAME</h2>
<p> <code>acl_error</code> &#8211; convert an ACL error code to a text message </p>
<h2>LIBRARY</h2>
<p> Linux Access Control Lists library (libacl, -lacl).</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In acl/libacl.h Ft const char * Fn acl_error int code</p>
<h2>DESCRIPTION</h2>
<p> The Fn acl_error function converts an ACL error code such as returned by the Fn acl_check function to a text message describing the error condition. In the &#8220;POSIX&#8221; locale, Fn acl_check returns the following descriptions for the error codes.</p>
<dl>
<dt><code>ACL_MULTI_ERROR</code></p>
<dd> &#8220;Multiple entries&#8221;</p>
<dt><code>ACL_DUPLICATE_ERROR</code></p>
<dd> &#8220;Duplicate entries&#8221;</p>
<dt><code>ACL_MISS_ERROR</code></p>
<dd> &#8220;Missing or wrong entry&#8221;</p>
<dt><code>ACL_ENTRY_ERROR</code></p>
<dd> &#8220;Invalid entry type&#8221;</dl>
<h2>RETURN VALUE</h2>
<p> The Fn acl_error function returns a text message if the error code is recognized, and a value of <code>(const char *)NULL</code> otherwise.</p>
<h2>STANDARDS</h2>
<p> This is a non-portable, Linux specific extension to the ACL manipulation functions defined in IEEE Std 1003.1e draft 17 (&#8220;POSIX.1e&#8221;, abandoned).</p>
<h2>SEE ALSO</h2>
<p> acl_check3, acl_valid3, <a href="/docs/linux/man/5-acl/">acl</a>(5)</p>
<h2>AUTHOR</h2>
<p> Written by An Andreas Gruenbacher Aq a.gruenbacher [at] bestbits.at . </p>
<h2>Index</h2>
