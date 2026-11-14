---
title: "punycode_decode(3)"
name: "punycode_decode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-punycode_decode/"
description: "punycode_decode – API function"
---

<p>punycode_decode &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;punycode.h&gt;
int punycode_decode(size_t input_length, const char[] input, size_t *output_length, punycode_uint[] output, unsigned char[] case_flags);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>size_t input_length</p>
<dd>The number of ASCII code points in the <i>input</i> array.</p>
<dt>const char [] input</p>
<dd>An array of ASCII code points (0..7F).</p>
<dt>size_t * output_length</p>
<dd>The caller passes in the maximum number of code points that it can receive into the <i>output</i> array (which is also the maximum number of flags that it can receive into the <i>case_flags</i> array, if <i>case_flags</i> is not a <code>NULL</code> pointer). On successful return it will contain the number of code points actually output (which is also the number of flags actually output, if case_flags is not a null pointer). The decoder will never need to output more code points than the number of ASCII code points in the input, because of the way the encoding is defined. The number of code points output cannot exceed the maximum possible value of a punycode_uint, even if the supplied <i>output_length</i> is greater than that.</p>
<dt>punycode_uint [] output</p>
<dd>An array of code points like the input argument of <code>punycode_encode()</code> (see above).</p>
<dt>unsigned char [] case_flags</p>
<dd>A <code>NULL</code> pointer (if the flags are not needed by the caller) or an array of boolean values parallel to the <i>output</i> array. Nonzero (true, flagged) suggests that the corresponding Unicode character be forced to uppercase by the caller (if possible), and zero (false, unflagged) suggests that it be forced to lowercase (if possible). ASCII code points (0..7F) are output already in the proper case, but their flags will be set appropriately so that applying the flags would be harmless.</dl>
<h2>Description</h2>
<p>Converts Punycode to a sequence of code points (presumed to be Unicode code points).</p>
<h2>Return Value</h2>
<p>The return value can be any of the <code>Punycode_status</code> values defined above. If not <code>PUNYCODE_SUCCESS</code>, then <i>output_length</i>, <i>output</i>, and <i>case_flags</i> might contain garbage.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;bug-libidn [at] gnu.org&gt;. GNU Libidn home page: <a rel="nofollow" href="http://www.gnu.org/software/libidn/">http://www.gnu.org/software/libidn/</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2013 Simon Josefsson.<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>See Also</h2>
<p>The full documentation for <code>libidn</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libidn</code> programs are properly installed at your site, the command</p>
<dl>
<dd><code>info libidn</code></dl>
<p> should give you access to the complete manual. </p>
