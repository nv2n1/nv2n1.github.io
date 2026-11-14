---
title: "ipsec_ttodata(3)"
name: "ipsec_ttodata"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_ttodata/"
description: "ipsec_ttodata, ipsec_datatot – convert binary data bytes from and to text formats"
---

<h2 class="name">NAME</h2>
<p> ipsec_ttodata, ipsec_datatot &#8211; convert binary data bytes from and to text formats </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;freeswan.h&gt;
</code></pre>
<dl>
<dt> <code>const char *ttodata(const char&nbsp;<wbr>*&nbsp;<wbr></code><i>src</i><code>, size_t&nbsp;<wbr></code><i>srclen</i><code>, int&nbsp;<wbr></code><i>base</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>dst</i><code>, size_t&nbsp;<wbr></code><i>dstlen</i><code>, size_t&nbsp;<wbr>*&nbsp;<wbr></code><i>lenp</i><code>);</code> </p>
<dt> <code>const char *ttodatav(const char&nbsp;<wbr>*&nbsp;<wbr></code><i>src</i><code>, size_t&nbsp;<wbr></code><i>srclen</i><code>, int&nbsp;<wbr></code><i>base</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>dst</i><code>, size_t&nbsp;<wbr></code><i>dstlen</i><code>, size_t&nbsp;<wbr>*&nbsp;<wbr></code><i>lenp</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>errp</i><code>, size_t&nbsp;<wbr></code><i>errlen</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code> </p>
<dt> <code>size_t datatot(const char&nbsp;<wbr>*&nbsp;<wbr></code><i>src</i><code>, size_t&nbsp;<wbr></code><i>srclen</i><code>, int&nbsp;<wbr></code><i>format</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>dst</i><code>, size_t&nbsp;<wbr></code><i>dstlen</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <i>Ttodata</i>, <code>ttodatav</code>, and <code>datatot</code></p>
<dd>convert arbitrary binary data (e.g. encryption or authentication keys) from and to more-or-less human-readable text formats. </p>
<p> Currently supported formats are hexadecimal, base64, and characters. </p>
<p> A hexadecimal text value begins with a <code>0x</code> (or <code>0X</code>) prefix and continues with two-digit groups of hexadecimal digits (0-9, and a-f or A-F), each group encoding the value of one binary byte, high-order digit first. A single <code>_</code> (underscore) between consecutive groups is ignored, permitting punctuation to improve readability; doing this every eight digits seems about right. </p>
<p> A base64 text value begins with a <code>0s</code> (or <code>0S</code>) prefix and continues with four-digit groups of base64 digits (A-Z, a-z, 0-9, +, and /), each group encoding the value of three binary bytes as described in section 6.8 of RFC 2045. If <i>flags</i> has the <code>TTODATAV_IGNORESPACE</code> bit on, blanks are ignore (after the prefix). Note that the last one or two digits of a base64 group can be <code>=</code> to indicate that fewer than three binary bytes are encoded. </p>
<p> A character text value begins with a <code>0t</code> (or <code>0T</code>) prefix and continues with text characters, each being the value of one binary byte. </p>
<p> All these functions basically copy data from <i>src</i> (whose size is specified by <i>srclen</i>) to <i>dst</i> (whose size is specified by <i>dstlen</i>), doing the conversion en route. If the result will not fit in <i>dst</i>, it is truncated; under no circumstances are more than <i>dstlen</i> bytes of result written to <i>dst</i>. <i>Dstlen</i> can be zero, in which case <i>dst</i> need not be valid and no result bytes are written at all. </p>
<p> The <i>base</i> parameter of <code>ttodata</code> and <code>ttodatav</code> specifies what format the input is in; normally it should be 0 to signify that this gets figured out from the prefix. Values of 16, 64, and 256 respectively signify hexadecimal, base64, and character-text formats without prefixes. </p>
<p> The <i>format</i> parameter of <code>datatot</code>, a single character used as a type code, specifies which text format is wanted. The value 0 (not ASCII <code>&#8216;0&#8217;</code>, but a zero value) specifies a reasonable default. Other currently-supported values are: </p>
<p> <code>&#8216;x&#8217;</code></p>
<dl>
<dt>
<dd> continuous lower-case hexadecimal with a <code>0x</code> prefix</dl>
<p> <code>&#8216;h&#8217;</code></p>
<dl>
<dt>
<dd> lower-case hexadecimal with a <code>0x</code> prefix and a <code>_</code> every eight digits</dl>
<p> <code>&#8216;:&#8217;</code></p>
<dl>
<dt>
<dd> lower-case hexadecimal with no prefix and a <code>:</code> (colon) every two digits</dl>
<p> 16</p>
<dl>
<dt>
<dd> lower-case hexadecimal with no prefix or <code>_</code></dl>
<p> <code>&#8216;s&#8217;</code></p>
<dl>
<dt>
<dd> continuous base64 with a <code>0s</code> prefix</dl>
<p> 64</p>
<dl>
<dt>
<dd> continuous base64 with no prefix</dl>
<p> The default format is currently <code>&#8216;h&#8217;</code>. </p>
<p> <i>Ttodata</i> returns NULL for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. On success, if and only if <i>lenp</i> is non-NULL, <code>*lenp</code> is set to the number of bytes required to contain the full untruncated result. It is the caller&#8217;s responsibility to check this against <i>dstlen</i> to determine whether he has obtained a complete result. The <code>*lenp</code> value is correct even if <i>dstlen</i> is zero, which offers a way to determine how much space would be needed before having to allocate any. </p>
<p> <i>Ttodatav</i> is just like <code>ttodata</code> except that in certain cases, if <i>errp</i> is non-NULL, the buffer pointed to by <i>errp</i> (whose length is given by <i>errlen</i>) is used to hold a more detailed error message. The return value is NULL for success, and is either <i>errp</i> or a pointer to a string literal for failure. If the size of the error-message buffer is inadequate for the desired message, <code>ttodatav</code> will fall back on returning a pointer to a literal string instead. The <i>freeswan.h</i> header file defines a constant <code>TTODATAV_BUF</code> which is the size of a buffer large enough for worst-case results. </p>
<p> The normal return value of <code>datatot</code> is the number of bytes required to contain the full untruncated result. It is the caller&#8217;s responsibility to check this against <i>dstlen</i> to determine whether he has obtained a complete result. The return value is correct even if <i>dstlen</i> is zero, which offers a way to determine how much space would be needed before having to allocate any. A return value of 0 signals a fatal error of some kind (see DIAGNOSTICS). </p>
<p> A zero value for <i>srclen</i> in <code>ttodata</code> (but not <code>datatot</code>!) is synonymous with <code>strlen(src)</code>. A non-zero <i>srclen</i> in <code>ttodata</code> must not include the terminating NUL. </p>
<p> Unless <i>dstlen</i> is zero, the result supplied by <code>datatot</code> is always NUL-terminated, and its needed-size return value includes space for the terminating NUL. </p>
<p> Several obsolete variants of these functions (<i>atodata</i>, <i>datatoa</i>, <i>atobytes</i>, and <i>bytestoa</i>) are temporarily also supported.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/3-ipsec_atoaddr/">ipsec_atoaddr</a></code>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <code>ttodata</code> and <code>ttodatav</code> are: unknown characters in the input; unknown or missing prefix; unknown base; incomplete digit group; non-zero padding in a base64 less-than-three-bytes digit group; zero-length input. </p>
<p> Fatal errors in <code>datatot</code> are: unknown format code; zero-length input.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> <i>Datatot</i> should have a format code to produce character-text output. </p>
<p> The <code>0s</code> and <code>0t</code> prefixes are the author&#8217;s inventions and are not a standard of any kind. They have been chosen to avoid collisions with existing practice (some C implementations use <code>0b</code> for binary) and possible confusion with unprefixed hexadecimal. </p>
<h2>Index</h2>
