---
title: "wcstombs(3)"
name: "wcstombs"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcstombs/"
description: "wcstombs – convert a wide-character string to a multibyte string"
---
<p>wcstombs &#8211; convert a wide-character string to a multibyte string </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;stdlib.h&gt; 
 size_t wcstombs(char *  dest  , const wchar_t *  src  , size_t  n  ); 
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <i>dest</i> is not NULL, the <code>wcstombs</code>() function converts the wide-character string <i>src</i> to a multibyte string starting at <i>dest</i>. At most <i>n</i> bytes are written to <i>dest</i>. The sequence of characters placed in <i>dest</i> begins in the initial shift state. The conversion can stop for three reasons: </p>
<dl>
<dt>1.</dt>
<dd> <p> A wide character has been encountered that can not be represented as a multibyte sequence (according to the current locale). In this case, <i>(size_t)&nbsp;-1</i> is returned. </p>
 </dd>
<dt>2.</dt>
<dd> <p> The length limit forces a stop. In this case, the number of bytes written to <i>dest</i> is returned, but the shift state at this point is lost. </p>
 </dd>
<dt>3.</dt>
<dd> <p> The wide-character string has been completely converted, including the terminating null wide character (L&#8217;\0&#8217;). In this case, the conversion ends in the initial shift state. The number of bytes written to <i>dest</i>, excluding the terminating null byte (&#8216;\0&#8217;), is returned. </p>
 </dd></dl>
<p>The programmer must ensure that there is room for at least <i>n</i> bytes at <i>dest</i>. </p>
<p>If <i>dest</i> is NULL, <i>n</i> is ignored, and the conversion proceeds as above, except that the converted bytes are not written out to memory, and no length limit exists. </p>
<p>In order to avoid the case 2 above, the programmer should make sure <i>n</i> is greater than or equal to <i>wcstombs(NULL,src,0)+1</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcstombs</code>() function returns the number of bytes that make up the converted part of a multibyte sequence, not including the terminating null byte. If a wide character was encountered which could not be converted, <i>(size_t)&nbsp;-1</i> is returned.  </p>
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
<td> <code>wcstombs</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>wcstombs</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p>The function <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3) provides a better interface to the same functionality.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3), <code><a href="/docs/linux/man/3-mbstowcs/">mbstowcs</a></code>(3), <code><a href="/docs/linux/man/3-mbtowc/">mbtowc</a></code>(3), <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3), <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
