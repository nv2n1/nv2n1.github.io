---
title: "crypt_preferred_method(3)"
name: "crypt_preferred_method"
section: "3"
letter: "c"
url: "/docs/linux/man/3-crypt_preferred_method/"
description: "crypt_preferred_method – get the prefix of the preferred hash method"
---

<p>libxcrypt</p>
<h2 class="name">NAME</h2>
<p> <code>crypt_preferred_method</code> &#8211; get the prefix of the preferred hash method </p>
<h2>LIBRARY</h2>
<p> Lb libcrypt</p>
<h2>SYNOPSIS</h2>
<p> In crypt.h Ft const char* Fo crypt_preferred_method Fa void Fc</p>
<h2>DESCRIPTION</h2>
<p> <code>crypt_preferred_method</code> is a convenience function to get the prefix of the preferred hash method. If a preferred method is available, it is the same as the one also used by the <code>crypt_gensalt functions</code> if their given <i>prefix</i> parameter is NULL.</p>
<h2>RETURN VALUES</h2>
<p> The string returned equals the prefix of the preferred hash method. If no preferred hash method is available it is NULL. It <i>is</i> safe to pass the string returned by <code>crypt_preferred_method</code> directly to <code>crypt_gensalt</code> without prior string-sanitizing nor NULL-pointer checks.</p>
<h2>FEATURE TEST MACROS</h2>
<p> In crypt.h will define the macro <code>CRYPT_PREFERRED_METHOD_AVAILABLE</code> if <code>crypt_preferred_method</code> is available in the current version of libxcrypt.</p>
<h2>PORTABILITY NOTES</h2>
<p> The function <code>crypt_preferred_method</code> is not part of any standard. It was added to libxcrypt in version 4.4.0.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <a href="/docs/linux/man/7-attributes/">attributes</a>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>crypt_preferred_method</code> </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>SEE ALSO</h2>
<p> crypt_gensalt3 </p>
<h2>Index</h2>
