---
title: "idna_to_unicode_4z4z(3)"
name: "idna_to_unicode_4z4z"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idna_to_unicode_4z4z/"
description: "idna_to_unicode_4z4z – API function"
---

<h2>NAME</h2>
<p> idna_to_unicode_4z4z &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;idna.h&gt;</code> </p>
<p> <code>int idna_to_unicode_4z4z(const uint32_t * </code><i>input</i><code>, uint32_t ** </code><i>output</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const uint32_t * input</p>
<dd> zero-terminated Unicode string.</p>
<dt>uint32_t ** output</p>
<dd> pointer to newly allocated output Unicode string.</p>
<dt>int flags</p>
<dd> an <code>Idna_flags</code> value, e.g., <code>IDNA_ALLOW_UNASSIGNED</code> or <code>IDNA_USE_STD3_ASCII_RULES</code>.</dl>
<h2>DESCRIPTION</h2>
<p> Convert possibly ACE encoded domain name in UCS-4 format into a UCS-4 string. The domain name may contain several labels, separated by dots. The output buffer must be deallocated by the caller.</p>
<h2>RETURN VALUE</h2>
<p> Returns <code>IDNA_SUCCESS</code> on success, or error code.</p>
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
