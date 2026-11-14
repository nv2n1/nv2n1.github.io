---
title: "fmtcheck(3)"
name: "fmtcheck"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmtcheck/"
description: "fmtcheck – sanitizes user-supplied"
---

<h2 class="name">NAME</h2>
<p> <code>fmtcheck</code> &#8211; sanitizes user-supplied </p>
<p><a href="/docs/linux/man/3-printf/">printf</a>(3)Ns-style format string</p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In bsd/stdio.h Ft const char * Fn fmtcheck const char *fmt_suspect const char *fmt_default</p>
<h2>DESCRIPTION</h2>
<p> The Fn fmtcheck scans Fa fmt_suspect and Fa fmt_default to determine if Fa fmt_suspect will consume the same argument types as Fa fmt_default and to ensure that Fa fmt_suspect is a valid format string. </p>
<p> The <a href="/docs/linux/man/3-printf/">printf</a>(3) family of functions cannot verify the types of arguments that they are passed at run-time. In some cases, like <a href="/docs/linux/man/3-catgets/">catgets</a>(3), it is useful or necessary to use a user-supplied format string with no guarantee that the format string matches the specified arguments. </p>
<p> The Fn fmtcheck was designed to be used in these cases, as in: </p>
<blockquote>
<pre>
printf(fmtcheck(user_format, standard_format), arg1, arg2);
</pre>
</blockquote>
<p> In the check, field widths, fillers, precisions, etc. are ignored (unless the field width or precision is an asterisk `*&#8217; instead of a digit string). Also, any text other than the format specifiers is completely ignored.</p>
<h2>RETURN VALUES</h2>
<p> If Fa fmt_suspect is a valid format and consumes the same argument types as Fa fmt_default , then the Fn fmtcheck will return Fa fmt_suspect . Otherwise, it will return Fa fmt_default .</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p> Note that the formats may be quite different as long as they accept the same arguments. For example, Qq Li %p %o %30s %#llx %-10.*e %n is compatible with Qq Li This number %lu %d%% and string %s has %qd numbers and %.*g floats (%n) . However, Qq Li %o is not equivalent to Qq Li %lx because the first requires an integer and the second requires a long.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-printf/">printf</a>(3)</p>
<h2>BUGS</h2>
<p> The Fn fmtcheck function does not understand all of the conversions that <a href="/docs/linux/man/3-printf/">printf</a>(3) does. </p>
<h2>Index</h2>
