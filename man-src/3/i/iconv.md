---
title: "iconv(3)"
name: "iconv"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iconv/"
description: "iconv – perform character set conversion"
---

<h2 class="name">NAME</h2>
<p> iconv &#8211; perform character set conversion </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;iconv.h&gt;
size_t iconv(iconv_t cd,
             char **inbuf, size_t *inbytesleft,
             char **outbuf, size_t *outbytesleft);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>iconv</code>() function converts a sequence of characters in one character encoding to a sequence of characters in another character encoding. The <i>cd</i> argument is a conversion descriptor, previously created by a call to <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3); the conversion descriptor defines the character encodings that <code>iconv</code>() uses for the conversion. The <i>inbuf</i> argument is the address of a variable that points to the first character of the input sequence; <i>inbytesleft</i> indicates the number of bytes in that buffer. The <i>outbuf</i> argument is the address of a variable that points to the first byte available in the output buffer; <i>outbytesleft</i> indicates the number of bytes available in the output buffer. </p>
<p> The main case is when <i>inbuf</i> is not NULL and <i>*inbuf</i> is not NULL. In this case, the <code>iconv</code>() function converts the multibyte sequence starting at <i>*inbuf</i> to a multibyte sequence starting at <i>*outbuf</i>. At most <i>*inbytesleft</i> bytes, starting at <i>*inbuf</i>, will be read. At most <i>*outbytesleft</i> bytes, starting at <i>*outbuf</i>, will be written. </p>
<p> The <code>iconv</code>() function converts one multibyte character at a time, and for each character conversion it increments <i>*inbuf</i> and decrements <i>*inbytesleft</i> by the number of converted input bytes, it increments <i>*outbuf</i> and decrements <i>*outbytesleft</i> by the number of converted output bytes, and it updates the conversion state contained in <i>cd</i>. If the character encoding of the input is stateful, the <code>iconv</code>() function can also convert a sequence of input bytes to an update to the conversion state without producing any output bytes; such input is called a <i>shift sequence</i>. The conversion can stop for four reasons:</p>
<dl>
<dt>1.</p>
<dd> An invalid multibyte sequence is encountered in the input. In this case, it sets <i>errno</i> to <code>EILSEQ</code> and returns <i>(size_t)&nbsp;-1</i>. <i>*inbuf</i> is left pointing to the beginning of the invalid multibyte sequence.</p>
<dt>2.</p>
<dd> The input byte sequence has been entirely converted, that is, <i>*inbytesleft</i> has gone down to 0. In this case, <code>iconv</code>() returns the number of nonreversible conversions performed during this call.</p>
<dt>3.</p>
<dd> An incomplete multibyte sequence is encountered in the input, and the input byte sequence terminates after it. In this case, it sets <i>errno</i> to <code>EINVAL</code> and returns <i>(size_t)&nbsp;-1</i>. <i>*inbuf</i> is left pointing to the beginning of the incomplete multibyte sequence.</p>
<dt>4.</p>
<dd> The output buffer has no more room for the next converted character. In this case, it sets <i>errno</i> to <code>E2BIG</code> and returns <i>(size_t)&nbsp;-1</i>.</dl>
<p> A different case is when <i>inbuf</i> is NULL or <i>*inbuf</i> is NULL, but <i>outbuf</i> is not NULL and <i>*outbuf</i> is not NULL. In this case, the <code>iconv</code>() function attempts to set <i>cd</i>&#8216;s conversion state to the initial state and store a corresponding shift sequence at <i>*outbuf</i>. At most <i>*outbytesleft</i> bytes, starting at <i>*outbuf</i>, will be written. If the output buffer has no more room for this reset sequence, it sets <i>errno</i> to <code>E2BIG</code> and returns <i>(size_t)&nbsp;-1</i>. Otherwise, it increments <i>*outbuf</i> and decrements <i>*outbytesleft</i> by the number of bytes written. </p>
<p> A third case is when <i>inbuf</i> is NULL or <i>*inbuf</i> is NULL, and <i>outbuf</i> is NULL or <i>*outbuf</i> is NULL. In this case, the <code>iconv</code>() function sets <i>cd</i>&#8216;s conversion state to the initial state.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iconv</code>() function returns the number of characters converted in a nonreversible way during this call; reversible conversions are not counted. In case of error, it sets <i>errno</i> and returns <i>(size_t)&nbsp;-1</i>.</p>
<h2>ERRORS</h2>
<p> The following errors can occur, among others:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> There is not sufficient room at <i>*outbuf</i>.</p>
<dt><code>EILSEQ</code></p>
<dd> An invalid multibyte sequence has been encountered in the input.</p>
<dt><code>EINVAL</code></p>
<dd> An incomplete multibyte sequence has been encountered in the input.</dl>
<h2>VERSIONS</h2>
<p> This function is available in glibc since version 2.1.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>iconv</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:cd
</td>
</tr>
</table>
<p> The <code>iconv</code>() function is MT-Safe, as long as callers arrange for mutual exclusion on the <i>cd</i> argument.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> In each series of calls to <code>iconv</code>(), the last should be one with <i>inbuf</i> or <i>*inbuf</i> equal to NULL, in order to flush out any partially converted input. </p>
<p> Although <i>inbuf</i> and <i>outbuf</i> are typed as <i>char&nbsp;**</i>, this does not mean that the objects they point can be interpreted as C strings or as arrays of characters: the interpretation of character byte sequences is handled internally by the conversion functions. In some encodings, a zero byte may be a valid part of a multibyte character. </p>
<p> The caller of <code>iconv</code>() must ensure that the pointers passed to the function are suitable for accessing characters in the appropriate character set. This includes ensuring correct alignment on platforms that have tight restrictions on alignment.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iconv_close/">iconv_close</a></code>(3), <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3), <code><a href="/docs/linux/man/8-iconvconfig/">iconvconfig</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
