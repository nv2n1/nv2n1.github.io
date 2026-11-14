---
title: "toupper(3)"
name: "toupper"
section: "3"
letter: "t"
url: "/docs/linux/man/3-toupper/"
description: "toupper, tolower, toupper_l, tolower_l – convert uppercase or lowercase"
---

<p>toupper, tolower, toupper_l, tolower_l &#8211; convert uppercase or lowercase</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ctype.h&gt;

int toupper(int c);
int tolower(int c);

int toupper_l(int c, locale_t locale);
int tolower_l(int c, locale_t locale);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>toupper_l</code>(), <code>tolower_l</code>():</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;700</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p>These functions convert lowercase letters to uppercase, and vice versa. </p>
<p> If <i>c</i> is a lowercase letter, <code>toupper</code>() returns its uppercase equivalent, if an uppercase representation exists in the current locale. Otherwise, it returns <i>c</i>. The <code>toupper_l</code>() function performs the same task, but uses the locale referred to by the locale handle <i>locale</i>. </p>
<p> If <i>c</i> is an uppercase letter, <code>tolower</code>() returns its lowercase equivalent, if a lowercase representation exists in the current locale. Otherwise, it returns <i>c</i>. The <code>tolower_l</code>() function performs the same task, but uses the locale referred to by the locale handle <i>locale</i>. </p>
<p> If <i>c</i> is neither an <i>unsigned char</i> value nor <code>EOF</code>, the behavior of these functions is undefined. </p>
<p> The behavior of <code>toupper_l</code>() and <code>tolower_l</code>() is undefined if <i>locale</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> (see <code><a href="/docs/linux/man/3-duplocale/">duplocale</a></code>(3)) or is not a valid locale object handle.</p>
<h2>Return Value</h2>
<p>The value returned is that of the converted letter, or <i>c</i> if the conversion was not possible.</p>
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
<td> <code>toupper</code>(), <code>tolower</code>(),<br />
 <code>toupper_l</code>(), <code>tolower_l</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>toupper</code>(), <code>tolower</code>(): C89, C99, 4.3BSD, POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>toupper_l</code>(), <code>tolower_l</code>(): POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The standards require that the argument <i>c</i> for these functions is either <code>EOF</code> or a value that is representable in the type <i>unsigned char</i>. If the argument <i>c</i> is of type <i>char</i>, it must be cast to <i>unsigned char</i>, as in the following example: </p>
<pre><code>char c;
... res = toupper((unsigned char)c);</code></pre>
<p> This is necessary because <i>char</i> may be the equivalent <i>signed char</i>, in which case a byte where the top bit is set would be sign extended when converting to <i>int</i>, yielding a value that is outside the range of <i>unsigned char</i>. The details of what constitutes an uppercase or lowercase letter depend on the locale. For example, the default <code>C</code> locale does not know about umlauts, so no conversion is done for them. In some non-English locales, there are lowercase letters with no corresponding uppercase equivalent; the German sharp s is one example.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-isalpha/">isalpha</a></code>(3), <code><a href="/docs/linux/man/3-newlocale/">newlocale</a></code>(3), <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3), <code><a href="/docs/linux/man/3-towlower/">towlower</a></code>(3), <code><a href="/docs/linux/man/3-towupper/">towupper</a></code>(3), <code><a href="/docs/linux/man/3-uselocale/">uselocale</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
