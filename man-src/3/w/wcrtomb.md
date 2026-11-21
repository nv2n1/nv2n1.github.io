---
title: "wcrtomb(3)"
name: "wcrtomb"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcrtomb/"
description: "wcrtomb – convert a wide character to a multibyte sequence"
---

<p>wcrtomb &#8211; convert a wide character to a multibyte sequence</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;wchar.h&gt;
size_t wcrtomb(char *s, wchar_t wc, mbstate_t *ps);</code></pre>
<h2>Description</h2>
<p>The main case for this function is when <i>s</i> is not NULL and <i>wc</i> is not a null wide character (L&#8217;\0&#8217;). In this case, the <code>wcrtomb</code>() function converts the wide character <i>wc</i> to its multibyte representation and stores it at the beginning of the character array pointed to by <i>s</i>. It updates the shift state <i>*ps</i>, and returns the length of said multibyte representation, that is, the number of bytes written at <i>s</i>. </p>
<p> A different case is when <i>s</i> is not NULL, but <i>wc</i> is a null wide character (L&#8217;\0&#8217;). In this case, the <code>wcrtomb</code>() function stores at the character array pointed to by <i>s</i> the shift sequence needed to bring <i>*ps</i> back to the initial state, followed by a &#8216;\0&#8217; byte. It updates the shift state <i>*ps</i> (i.e., brings it into the initial state), and returns the length of the shift sequence plus one, that is, the number of bytes written at <i>s</i>. </p>
<p> A third case is when <i>s</i> is NULL. In this case, <i>wc</i> is ignored, and the function effectively returns </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wcrtomb(buf, L&#8217;\0&#8217;, ps) </p>
<p> where <i>buf</i> is an internal anonymous buffer. </p>
<p> In all of the above cases, if <i>ps</i> is NULL, a static anonymous state known only to the <code>wcrtomb</code>() function is used instead.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcrtomb</code>() function returns the number of bytes that have been or would have been written to the byte array at <i>s</i>. If <i>wc</i> can not be represented as a multibyte sequence (according to the current locale), <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> set to <code>EILSEQ</code>.  </p>
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
<td> <code>wcrtomb</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:wcrtomb/!ps
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>wcrtomb</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> Passing NULL as <i>ps</i> is not multithread safe.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mbsinit/">mbsinit</a></code>(3), <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
