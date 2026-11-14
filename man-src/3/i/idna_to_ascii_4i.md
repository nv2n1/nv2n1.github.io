---
title: "idna_to_ascii_4i(3)"
name: "idna_to_ascii_4i"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idna_to_ascii_4i/"
description: "idna_to_ascii_4i – API function"
---

<h2>NAME</h2>
<p> idna_to_ascii_4i &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;idna.h&gt;</code> </p>
<p> <code>int idna_to_ascii_4i(const uint32_t * </code><i>in</i><code>, size_t </code><i>inlen</i><code>, char * </code><i>out</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const uint32_t * in</p>
<dd> input array with unicode code points.</p>
<dt>size_t inlen</p>
<dd> length of input array with unicode code points.</p>
<dt>char * out</p>
<dd> output zero terminated string that must have room for at least 63 characters plus the terminating zero.</p>
<dt>int flags</p>
<dd> an <code>Idna_flags</code> value, e.g., <code>IDNA_ALLOW_UNASSIGNED</code> or <code>IDNA_USE_STD3_ASCII_RULES</code>.</dl>
<h2>DESCRIPTION</h2>
<p> The ToASCII operation takes a sequence of Unicode code points that make up one domain label and transforms it into a sequence of code points in the ASCII range (0..7F). If ToASCII succeeds, the original sequence and the resulting sequence are equivalent labels. </p>
<p> It is important to note that the ToASCII operation can fail. ToASCII fails if any step of it fails. If any step of the ToASCII operation fails on any label in a domain name, that domain name MUST NOT be used as an internationalized domain name. The method for deadling with this failure is application-specific. </p>
<p> The inputs to ToASCII are a sequence of code points, the AllowUnassigned flag, and the UseSTD3ASCIIRules flag. The output of ToASCII is either a sequence of ASCII code points or a failure condition. </p>
<p> ToASCII never alters a sequence of code points that are all in the ASCII range to begin with (although it could fail). Applying the ToASCII operation multiple times has exactly the same effect as applying it just once.</p>
<h2>RETURN VALUE</h2>
<p> Returns 0 on success, or an <code>Idna_rc</code> error code.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-libidn [at] gnu.org&gt;. GNU Libidn home page: <a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2013 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libidn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libidn</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libidn</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
