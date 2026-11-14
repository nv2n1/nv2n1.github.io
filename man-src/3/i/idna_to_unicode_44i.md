---
title: "idna_to_unicode_44i(3)"
name: "idna_to_unicode_44i"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idna_to_unicode_44i/"
description: "idna_to_unicode_44i – API function"
---

<h2>NAME</h2>
<p> idna_to_unicode_44i &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;idna.h&gt;</code> </p>
<p> <code>int idna_to_unicode_44i(const uint32_t * </code><i>in</i><code>, size_t </code><i>inlen</i><code>, uint32_t * </code><i>out</i><code>, size_t * </code><i>outlen</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const uint32_t * in</p>
<dd> input array with unicode code points.</p>
<dt>size_t inlen</p>
<dd> length of input array with unicode code points.</p>
<dt>uint32_t * out</p>
<dd> output array with unicode code points.</p>
<dt>size_t * outlen</p>
<dd> on input, maximum size of output array with unicode code points, on exit, actual size of output array with unicode code points.</p>
<dt>int flags</p>
<dd> an <code>Idna_flags</code> value, e.g., <code>IDNA_ALLOW_UNASSIGNED</code> or <code>IDNA_USE_STD3_ASCII_RULES</code>.</dl>
<h2>DESCRIPTION</h2>
<p> The ToUnicode operation takes a sequence of Unicode code points that make up one domain label and returns a sequence of Unicode code points. If the input sequence is a label in ACE form, then the result is an equivalent internationalized label that is not in ACE form, otherwise the original sequence is returned unaltered. </p>
<p> ToUnicode never fails. If any step fails, then the original input sequence is returned immediately in that step. </p>
<p> The Punycode decoder can never output more code points than it inputs, but Nameprep can, and therefore ToUnicode can. Note that the number of octets needed to represent a sequence of code points depends on the particular character encoding used. </p>
<p> The inputs to ToUnicode are a sequence of code points, the AllowUnassigned flag, and the UseSTD3ASCIIRules flag. The output of ToUnicode is always a sequence of Unicode code points.</p>
<h2>RETURN VALUE</h2>
<p> Returns <code>Idna_rc</code> error condition, but it must only be used for debugging purposes. The output buffer is always guaranteed to contain the correct data according to the specification (sans malloc induced errors). NB! This means that you normally ignore the return code from this function, as checking it means breaking the standard.</p>
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
