---
title: "isdigit_l(3)"
name: "isdigit_l"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isdigit_l/"
description: "isalnum, isalpha, isascii, isblank, iscntrl, isdigit, isgraph, islower, isprint, ispunct, isspace, isupper, isxdigit, isalnum_l, isalpha_l, isascii_l, isblank_l, iscntrl_l, isdigit_l, isgraph_l, is..."
---

<h2 class="name">NAME</h2>
<p> isalnum, isalpha, isascii, isblank, iscntrl, isdigit, isgraph, islower, isprint, ispunct, isspace, isupper, isxdigit, isalnum_l, isalpha_l, isascii_l, isblank_l, iscntrl_l, isdigit_l, isgraph_l, islower_l, isprint_l, ispunct_l, isspace_l, isupper_l, isxdigit_l &#8211; character classification functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ctype.h&gt;
int isalnum(int c);
int isalpha(int c);
int iscntrl(int c);
int isdigit(int c);
int isgraph(int c);
int islower(int c);
int isprint(int c);
int ispunct(int c);
int isspace(int c);
int isupper(int c);
int isxdigit(int c);
int isascii(int c);
int isblank(int c);
int isalnum_l(int c, locale_t locale);
int isalpha_l(int c, locale_t locale);
int isblank_l(int c, locale_t locale);
int iscntrl_l(int c, locale_t locale);
int isdigit_l(int c, locale_t locale);
int isgraph_l(int c, locale_t locale);
int islower_l(int c, locale_t locale);
int isprint_l(int c, locale_t locale);
int ispunct_l(int c, locale_t locale);
int isspace_l(int c, locale_t locale);
int isupper_l(int c, locale_t locale);
int isxdigit_l(int c, locale_t locale);
int isascii_l(int c, locale_t locale);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>isascii</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE</dl>
<p> <code>isblank</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<p> <code>isalnum_l</code>(), <code>isalpha_l</code>(), <code>isblank_l</code>(), <code>iscntrl_l</code>(), <code>isdigit_l</code>(), <code>isgraph_l</code>(), <code>islower_l</code>(), <code>isprint_l</code>(), <code>ispunct_l</code>(), <code>isspace_l</code>(), <code>isupper_l</code>(), <code>isxdigit_l</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;700</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<p> <code>isascii_l</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;700 &amp;&amp; (_SVID_SOURCE || _BSD_SOURCE)</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> These functions check whether <i>c</i>, which must have the value of an <i>unsigned char</i> or <code>EOF</code>, falls into a certain character class according to the specified locale. The functions without the &quot;_l&quot; suffix perform the check based on the current locale. </p>
<p> The functions with the &quot;_l&quot; suffix perform the check based on the locale specified by the locale object <i>locale</i>. The behavior of these functions is undefined if <i>locale</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> (see <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)) or is not a valid locale object handle. </p>
<p> The list below explains the operation of the functions without the &quot;_l&quot; suffix; the functions with the &quot;_l&quot; suffix differ only in using the locale object <i>locale</i> instead of the current locale.</p>
<dl>
<dt><code>isalnum</code>()</p>
<dd> checks for an alphanumeric character; it is equivalent to <code>(isalpha(</code><i>c</i><code>) || isdigit(</code><i>c</i><code>))</code><i></i>.</p>
<dt><code>isalpha</code>()</p>
<dd> checks for an alphabetic character; in the standard <code>&quot;C&quot;</code> locale, it is equivalent to <code>(isupper(</code><i>c</i><code>) || islower(</code><i>c</i><code>))</code><i></i>. In some locales, there may be additional characters for which <code>isalpha</code>() is true&#8212;letters which are neither uppercase nor lowercase.</p>
<dt><code>isascii</code>()</p>
<dd> checks whether <i>c</i> is a 7-bit <i>unsigned char</i> value that fits into the ASCII character set.</p>
<dt><code>isblank</code>()</p>
<dd> checks for a blank character; that is, a space or a tab.</p>
<dt><code>iscntrl</code>()</p>
<dd> checks for a control character.</p>
<dt><code>isdigit</code>()</p>
<dd> checks for a digit (0 through 9).</p>
<dt><code>isgraph</code>()</p>
<dd> checks for any printable character except space.</p>
<dt><code>islower</code>()</p>
<dd> checks for a lowercase character.</p>
<dt><code>isprint</code>()</p>
<dd> checks for any printable character including space.</p>
<dt><code>ispunct</code>()</p>
<dd> checks for any printable character which is not a space or an alphanumeric character.</p>
<dt><code>isspace</code>()</p>
<dd> checks for white-space characters. In the <code>C</code> and <code>POSIX</code> locales, these are: space, form-feed (<code>&#8216;&#8217;</code>), newline (<code>&#8216;
&#8217;</code>), carriage return (<code>&#8216;&#8217;</code>), horizontal tab (<code>&#8216;	&#8217;</code>), and vertical tab (<code>&#8216;&#8217;</code>).</p>
<dt><code>isupper</code>()</p>
<dd> checks for an uppercase letter.</p>
<dt><code>isxdigit</code>()</p>
<dd> checks for hexadecimal digits, that is, one of<br />
 <code>0 1 2 3 4 5 6 7 8 9 a b c d e f A B C D E F</code>.</dl>
<h2>RETURN VALUE</h2>
<p> The values returned are nonzero if the character <i>c</i> falls into the tested class, and zero if not.</p>
<h2>VERSIONS</h2>
<p> <code>isalnum_l</code>(), <code>isalpha_l</code>(), <code>isblank_l</code>(), <code>iscntrl_l</code>(), <code>isdigit_l</code>(), <code>isgraph_l</code>(), <code>islower_l</code>(), <code>isprint_l</code>(), <code>ispunct_l</code>(), <code>isspace_l</code>(), <code>isupper_l</code>(), <code>isxdigit_l</code>(), and <code>isascii_l</code>() are available since glibc 2.3.</p>
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
<td> <code>isalnum</code>(), <code>isalpha</code>(), <code>isascii</code>(), <code>isblank</code>(), <code>iscntrl</code>(), <code>isdigit</code>(), <code>isgraph</code>(), <code>islower</code>(), <code>isprint</code>(), <code>ispunct</code>(), <code>isspace</code>(), <code>isupper</code>(), <code>isxdigit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C89 specifies <code>isalnum</code>(), <code>isalpha</code>(), <code>iscntrl</code>(), <code>isdigit</code>(), <code>isgraph</code>(), <code>islower</code>(), <code>isprint</code>(), <code>ispunct</code>(), <code>isspace</code>(), <code>isupper</code>(), and <code>isxdigit</code>(), but not <code>isascii</code>() and <code>isblank</code>(). POSIX.1-2001 also specifies those functions, and also <code>isascii</code>() (as an XSI extension) and <code>isblank</code>(). C99 specifies all of the preceding functions, except <code>isascii</code>(). </p>
<p> POSIX.1-2008 marks <code>isascii</code>() as obsolete, noting that it cannot be used portably in a localized application. </p>
<p> POSIX.1-2008 specifies <code>isalnum_l</code>(), <code>isalpha_l</code>(), <code>isblank_l</code>(), <code>iscntrl_l</code>(), <code>isdigit_l</code>(), <code>isgraph_l</code>(), <code>islower_l</code>(), <code>isprint_l</code>(), <code>ispunct_l</code>(), <code>isspace_l</code>(), <code>isupper_l</code>(), and <code>isxdigit_l</code>(). </p>
<p> <code>isascii_l</code>() is a GNU extension.</p>
<h2>NOTES</h2>
<p> The standards require that the argument <i>c</i> for these functions is either <code>EOF</code> or a value that is representable in the type <i>unsigned char</i>. If the argument <i>c</i> is of type <i>char</i>, it must be cast to <i>unsigned char</i>, as in the following example: </p>
<p> char c; &#8230; res = toupper((unsigned char) c); </p>
<p> This is necessary because <i>char</i> may be the equivalent of <i>signed char</i>, in which case a byte where the top bit is set would be sign extended when converting to <i>int</i>, yielding a value that is outside the range of <i>unsigned char</i>. </p>
<p> The details of what characters belong to which class depend on the locale. For example, <code>isupper</code>() will not recognize an A-umlaut (&Auml;) as an uppercase letter in the default <code>C</code> locale.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iswalnum/">iswalnum</a></code>(3), <code><a href="/docs/linux/man/3-iswalpha/">iswalpha</a></code>(3), <code><a href="/docs/linux/man/3-iswblank/">iswblank</a></code>(3), <code><a href="/docs/linux/man/3-iswcntrl/">iswcntrl</a></code>(3), <code><a href="/docs/linux/man/3-iswdigit/">iswdigit</a></code>(3), <code><a href="/docs/linux/man/3-iswgraph/">iswgraph</a></code>(3), <code><a href="/docs/linux/man/3-iswlower/">iswlower</a></code>(3), <code><a href="/docs/linux/man/3-iswprint/">iswprint</a></code>(3), <code><a href="/docs/linux/man/3-iswpunct/">iswpunct</a></code>(3), <code><a href="/docs/linux/man/3-iswspace/">iswspace</a></code>(3), <code><a href="/docs/linux/man/3-iswupper/">iswupper</a></code>(3), <code><a href="/docs/linux/man/3-iswxdigit/">iswxdigit</a></code>(3), <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-toascii/">toascii</a></code>(3), <code><a href="/docs/linux/man/3-tolower/">tolower</a></code>(3), <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3), <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), <code><a href="/docs/linux/man/7-ascii/">ascii</a></code>(7), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
