---
title: "wctype(3)"
name: "wctype"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wctype/"
description: "wctype – wide-character classification"
---

<p>wctype &#8211; wide-character classification</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wctype.h&gt;

wctype_t wctype(const char *name);</code></pre>
<h2>Description</h2>
<p>The <i>wctype_t</i> type represents a property which a wide character may or may not have. In other words, it represents a class of wide characters. This type&#8217;s nature is implementation-dependent, but the special value <i>(wctype_t) 0</i> denotes an invalid property. Nonzero <i>wctype_t</i> values can be passed to the <code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3) function to actually test whether a given wide character has the property. </p>
<p> The <code>wctype</code>() function returns a property, given by its name. The set of valid names depends on the <code>LC_CTYPE</code> category of the current locale, but the following names are valid in all locales. </p>
<pre> &quot;alnum&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isalnum/">isalnum</a></code>(3) classification function
 &quot;alpha&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isalpha/">isalpha</a></code>(3) classification function
 &quot;blank&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isblank/">isblank</a></code>(3) classification function
 &quot;cntrl&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-iscntrl/">iscntrl</a></code>(3) classification function
 &quot;digit&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isdigit/">isdigit</a></code>(3) classification function
 &quot;graph&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isgraph/">isgraph</a></code>(3) classification function
 &quot;lower&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-islower/">islower</a></code>(3) classification function
 &quot;print&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isprint/">isprint</a></code>(3) classification function
 &quot;punct&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-ispunct/">ispunct</a></code>(3) classification function
 &quot;space&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isspace/">isspace</a></code>(3) classification function
 &quot;upper&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isupper/">isupper</a></code>(3) classification function
 &quot;xdigit&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-isxdigit/">isxdigit</a></code>(3) classification function</pre>
<h2>Return Value</h2>
<p>The <code>wctype</code>() function returns a property descriptor if the <i>name</i> is valid. Otherwise, it returns <i>(wctype_t) 0</i>.</p>
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
<td> <code>wctype</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>wctype</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-iswctype/">iswctype</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
