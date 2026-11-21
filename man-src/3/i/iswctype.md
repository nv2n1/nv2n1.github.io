---

title: "iswctype(3)"
name: "iswctype"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iswctype/"
description: "iswctype – wide-character classification"
---

<pre><code>
#include &lt;wctype.h&gt;
int iswctype(wint_t wc, wctype_t desc);
</code></pre>
<p> If <i>wc</i> is a wide character having the character property designated by <i>desc</i> (or in other words: belongs to the character class designated by <i>desc</i>), the <code>iswctype</code>() function returns nonzero. Otherwise, it returns zero. If <i>wc</i> is <code>WEOF</code>, zero is returned. </p>
<p> <i>desc</i> must be a character property descriptor returned by the <code><a href="/docs/linux/man/3-wctype/">wctype</a></code>(3) function.</p>
<h2>RETURN VALUE</h2>
<p> The <code>iswctype</code>() function returns nonzero if the <i>wc</i> has the designated property. Otherwise, it returns 0.</p>
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
<td> <code>iswctype</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.</p>
<h2>NOTES</h2>
<p> The behavior of <code>iswctype</code>() depends on the <code>LC_CTYPE</code> category of the current locale.</p>
<h2>SEE ALSO</h2>
<p> <code>iswalnum</code>(3), <code>iswalpha</code>(3), <code>iswblank</code>(3), <code>iswcntrl</code>(3), <code>iswdigit</code>(3), <code>iswgraph</code>(3), <code>iswlower</code>(3), <code>iswprint</code>(3), <code>iswpunct</code>(3), <code>iswspace</code>(3), <code>iswupper</code>(3), <code>iswxdigit</code>(3), <code><a href="/docs/linux/man/3-wctype/">wctype</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
