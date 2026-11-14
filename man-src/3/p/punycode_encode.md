---
title: "punycode_encode(3)"
name: "punycode_encode"
section: "3"
letter: "p"
url: "/docs/linux/man/3-punycode_encode/"
description: "punycode_encode – API function"
---

<p>punycode_encode &#8211; API function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;punycode.h&gt;
int punycode_encode(size_t input_length, const punycode_uint[] input, const unsigned char[] case_flags, size_t *output_length, char[] output);</code></pre>
<h2>Arguments</h2>
<dl>
<dt>size_t input_length</p>
<dd>The number of code points in the <i>input</i> array and the number of flags in the <i>case_flags</i> array.</p>
<dt>const punycode_uint [] input</p>
<dd>An array of code points. They are presumed to be Unicode code points, but that is not strictly REQUIRED. The array contains code points, not code units. UTF-16 uses code units D800 through DFFF to refer to code points 10000..10FFFF. The code points D800..DFFF do not occur in any valid Unicode string. The code points that can occur in Unicode strings (0..D7FF and E000..10FFFF) are also called Unicode scalar values.</p>
<dt>const unsigned char [] case_flags</p>
<dd>A <code>NULL</code> pointer or an array of boolean values parallel to the <i>input</i> array. Nonzero (true, flagged) suggests that the corresponding Unicode character be forced to uppercase after being decoded (if possible), and zero (false, unflagged) suggests that it be forced to lowercase (if possible). ASCII code points (0..7F) are encoded literally, except that ASCII letters are forced to uppercase or lowercase according to the corresponding case flags. If <i>case_flags</i> is a <code>NULL</code> pointer then ASCII letters are left as they are, and other code points are treated as unflagged.</p>
<dt>size_t * output_length</p>
<dd>The caller passes in the maximum number of ASCII code points that it can receive. On successful return it will contain the number of ASCII code points actually output.</p>
<dt>char [] output</p>
<dd>An array of ASCII code points. It is *not* null-terminated; it will contain zeros if and only if the <i>input</i> contains zeros. (Of course the caller can leave room for a terminator and add one if needed.)</dl>
<h2>Description</h2>
<p>Converts a sequence of code points (presumed to be Unicode code points) to Punycode.</p>
<h2>Return Value</h2>
<p>The return value can be any of the <code>Punycode_status</code> values defined above except <code>PUNYCODE_BAD_INPUT</code>. If not <code>PUNYCODE_SUCCESS</code>, then <i>output_size</i> and <i>output</i> might contain garbage.</p>
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
