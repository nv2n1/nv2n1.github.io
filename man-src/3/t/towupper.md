---
title: "towupper(3)"
name: "towupper"
section: "3"
letter: "t"
url: "/docs/linux/man/3-towupper/"
description: "towupper, towupper_l – convert a wide character to uppercase"
---

<p>towupper, towupper_l &#8211; convert a wide character to uppercase</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wctype.h&gt;

wint_t towupper(wint_t wc);

wint_t towupper_l(wint_t wc, locale_t locale);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>towupper_l</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;700</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>The <code>towupper</code>() function is the wide-character equivalent of the <code><a href="/docs/linux/man/3-toupper/">toupper</a></code>(3) function. If <i>wc</i> is a lowercase wide character, and there exists an uppercase equivalent in the current locale, it returns the uppercase equivalent of <i>wc</i>. In all other cases, <i>wc</i> is returned unchanged. </p>
<p> The <code>towupper_l</code>() function performs the same task, but performs the conversion based on the character type information in the locale specified by <i>locale</i>. The behavior of <code>towupper_l</code>() is undefined if <i>locale</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> (see <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)) or is not a valid locale object handle. </p>
<p> The argument <i>wc</i> must be representable as a <i>wchar_t</i> and be a valid character in the locale or be the value <code>WEOF</code>.</p>
<h2>Return Value</h2>
<p>If <i>wc</i> was convertible to uppercase, <code>towupper</code>() returns its uppercase equivalent; otherwise it returns <i>wc</i>.</p>
<h2>Versions</h2>
<p>The <code>towupper_l</code>() function first appeared in glibc 2.3.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>towupper</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>towupper_l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>towupper</code>(): C99, POSIX.1-2001 (XSI); present as an XSI extension in POSIX.1-2008, but marked obsolete. </p>
<p> <code>towupper_l</code>(): POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The behavior of these functions depends on the <code>LC_CTYPE</code> category of the locale. </p>
<p> These functions are not very appropriate for dealing with Unicode characters, because Unicode knows about three cases: upper, lower and title case.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-iswupper/">iswupper</a></code>(3), <code><a href="/docs/linux/man/3-towctrans/">towctrans</a></code>(3), <code><a href="/docs/linux/man/3-towlower/">towlower</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
