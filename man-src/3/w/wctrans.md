---
title: "wctrans(3)"
name: "wctrans"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wctrans/"
description: "wctrans – wide-character translation mapping"
---

<p>wctrans &#8211; wide-character translation mapping</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wctype.h&gt;

wctrans_t wctrans(const char *name);</code></pre>
<h2>Description</h2>
<p>The <i>wctrans_t</i> type represents a mapping which can map a wide character to another wide character. Its nature is implementation-dependent, but the special value <i>(wctrans_t)&nbsp;0</i> denotes an invalid mapping. Nonzero <i>wctrans_t</i> values can be passed to the <code><a href="/docs/linux/man/3-towctrans/">towctrans</a></code>(3) function to actually perform the wide-character mapping. </p>
<p> The <code>wctrans</code>() function returns a mapping, given by its name. The set of valid names depends on the <code>LC_CTYPE</code> category of the current locale, but the following names are valid in all locales. </p>
<pre> &quot;tolower&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-tolower/">tolower</a></code>(3) mapping
 &quot;toupper&quot; - realizes the <code><a href="//www.systutorials.com/docs/linux/man/3-toupper/">toupper</a></code>(3) mapping</pre>
<h2>Return Value</h2>
<p>The <code>wctrans</code>() function returns a mapping descriptor if the <i>name</i> is valid. Otherwise, it returns <i>(wctrans_t)&nbsp;0</i>.</p>
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
<td> <code>wctrans</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>Notes</h2>
<p>The behavior of <code>wctrans</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-towctrans/">towctrans</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
