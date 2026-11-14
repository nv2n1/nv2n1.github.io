---
title: "ipsec_ttoul(3)"
name: "ipsec_ttoul"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_ttoul/"
description: "ipsec_ttoul, ipsec_ultot – convert unsigned-long numbers to and from text"
---

<h2 class="name">NAME</h2>
<p> ipsec_ttoul, ipsec_ultot &#8211; convert unsigned-long numbers to and from text </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;freeswan.h&gt;
</code></pre>
<dl>
<dt> <code>const char *ttoul(const char&nbsp;<wbr>*&nbsp;<wbr></code><i>src</i><code>, size_t&nbsp;<wbr></code><i>srclen</i><code>, int&nbsp;<wbr></code><i>base</i><code>, unsigned long&nbsp;<wbr>*&nbsp;<wbr></code><i>n</i><code>);</code> </p>
<dt> <code>size_t ultot(unsigned long&nbsp;<wbr></code><i>n</i><code>, int&nbsp;<wbr></code><i>format</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>dst</i><code>, size_t&nbsp;<wbr></code><i>dstlen</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <i>Ttoul</i></p>
<dd>converts a text-string number into a binary <code>unsigned long</code> value. <i>Ultot</i> does the reverse conversion, back to a text version. </p>
<p> Numbers are specified in text as decimal (e.g. 123), octal with a leading zero (e.g. 012, which has value 10), or hexadecimal with a leading <code>0x</code> (e.g. <code>0x1f</code>, which has value 31) in either upper or lower case. </p>
<p> The <i>srclen</i> parameter of <code>ttoul</code> specifies the length of the string pointed to by <i>src</i>; it is an error for there to be anything else (e.g., a terminating NUL) within that length. As a convenience for cases where an entire NUL-terminated string is to be converted, a <i>srclen</i> value of 0 is taken to mean <code>strlen(src)</code>. </p>
<p> The <i>base</i> parameter of <code>ttoul</code> can be 8, 10, or 16, in which case the number supplied is assumed to be of that form (and in the case of 16, to lack any <code>0x</code> prefix). It can also be 0, in which case the number is examined for a leading zero or a leading <code>0x</code> to determine its base. </p>
<p> The <i>dstlen</i> parameter of <code>ultot</code> specifies the size of the <i>dst</i> parameter; under no circumstances are more than <i>dstlen</i> bytes written to <i>dst</i>. A result which will not fit is truncated. <i>Dstlen</i> can be zero, in which case <i>dst</i> need not be valid and no result is written, but the return value is unaffected; in all other cases, the (possibly truncated) result is NUL-terminated. The <i>freeswan.h</i> header file defines a constant, <code>ULTOT_BUF</code>, which is the size of a buffer just large enough for worst-case results. </p>
<p> The <i>format</i> parameter of <code>ultot</code> must be one of: </p>
<p> <code>&#8216;o&#8217;</code></p>
<dl>
<dt>
<dd> octal conversion with leading 0</dl>
<p> <code>&nbsp;<wbr>8</code></p>
<dl>
<dt>
<dd> octal conversion with no leading 0</dl>
<p> <code>&#8216;d&#8217;</code></p>
<dl>
<dt>
<dd> decimal conversion</dl>
<p> 10</p>
<dl>
<dt>
<dd> same as <code>d</code></dl>
<p> <code>&#8216;x&#8217;</code></p>
<dl>
<dt>
<dd> hexadecimal conversion, including leading <code>0x</code></dl>
<p> 16</p>
<dl>
<dt>
<dd> hexadecimal conversion with no leading <code>0x</code></dl>
<p> 17</p>
<dl>
<dt>
<dd> like 16 except padded on left with 0s to eight digits (full width of a 32-bit number)</dl>
<p> <i>Ttoul</i> returns NULL for success and a pointer to a string-literal error message for failure; see DIAGNOSTICS. <i>Ultot</i> returns 0 for a failure, and otherwise returns the size of buffer which would be needed to accommodate the full conversion result, including terminating NUL (it is the caller&#8217;s responsibility to check this against the size of the provided buffer to determine whether truncation has occurred).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-atol/">atol</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3)</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors in <code>ttoul</code> are: empty input; unknown <i>base</i>; non-digit character found; number too large for an <code>unsigned long</code>. </p>
<p> Fatal errors in <code>ultot</code> are: unknown <i>format</i>.</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> Conversion of 0 with format <code>o</code> yields 00. </p>
<p> <i>Ultot</i> format 17 is a bit of a kludge. </p>
<p> The restriction of error reports to literal strings (so that callers don&#8217;t need to worry about freeing them or copying them) does limit the precision of error reporting. </p>
<p> The error-reporting convention lends itself to slightly obscure code, because many readers will not think of NULL as signifying success. A good way to make it clearer is to write something like: </p>
<dl>
<dt>
<dd>
<pre><code>
const char *error;
error = ttoul(/* ... */);
if (error != NULL) {
/* something went wrong */
</code></pre>
</dl>
<h2>Index</h2>
