---
title: "idna_strerror(3)"
name: "idna_strerror"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idna_strerror/"
description: "idna_strerror – API function"
---

<h2>NAME</h2>
<p> idna_strerror &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;idna.h&gt;</code> </p>
<p> <code>const char * idna_strerror(Idna_rc </code><i>rc</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>Idna_rc rc</p>
<dd> an <code>Idna_rc</code> return code.</dl>
<h2>DESCRIPTION</h2>
<p> Convert a return code integer to a text string. This string can be used to output a diagnostic message to the user.</p>
<h2>IDNA_SUCCESS</h2>
<p> Successful operation. This value is guaranteed to always be zero, the remaining ones are only guaranteed to hold non-zero values, for logical comparison purposes.</p>
<h2>IDNA_STRINGPREP_ERROR</h2>
<p> Error during string preparation.</p>
<h2>IDNA_PUNYCODE_ERROR</h2>
<p> Error during punycode operation.</p>
<h2>IDNA_CONTAINS_NON_LDH</h2>
<p> For IDNA_USE_STD3_ASCII_RULES, indicate that the string contains non-LDH ASCII characters.</p>
<h2>IDNA_CONTAINS_MINUS</h2>
<p> For IDNA_USE_STD3_ASCII_RULES, indicate that the string contains a leading or trailing hyphen-minus (U+002D).</p>
<h2>IDNA_INVALID_LENGTH</h2>
<p> The final output string is not within the (inclusive) range 1 to 63 characters.</p>
<h2>IDNA_NO_ACE_PREFIX</h2>
<p> The string does not contain the ACE prefix (for ToUnicode).</p>
<h2>IDNA_ROUNDTRIP_VERIFY_ERROR</h2>
<p> The ToASCII operation on output string does not equal the input.</p>
<h2>IDNA_CONTAINS_ACE_PREFIX</h2>
<p> The input contains the ACE prefix (for ToASCII).</p>
<h2>IDNA_ICONV_ERROR</h2>
<p> Could not convert string in locale encoding.</p>
<h2>IDNA_MALLOC_ERROR</h2>
<p> Could not allocate buffer (this is typically a fatal error).</p>
<h2>IDNA_DLOPEN_ERROR</h2>
<p> Could not dlopen the libcidn DSO (only used internally in libc).</p>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to a statically allocated string containing a description of the error with the return code <i>rc</i>.</p>
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
