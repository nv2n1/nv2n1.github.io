---
title: "wcsnrtombs(3)"
name: "wcsnrtombs"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wcsnrtombs/"
description: "wcsnrtombs – convert a wide-character string to a multibyte string"
---
<p>wcsnrtombs &#8211; convert a wide-character string to a multibyte string </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;wchar.h&gt; 
 size_t wcsnrtombs(char *  dest  , const wchar_t **  src  , size_t  nwc  , 
                   size_t  len  , mbstate_t *  ps  ); 
</code></pre>
<p>Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>wcsnrtombs</code>(): </p>
<dl>
<dd>  </dd>
<dl>
<dt>Since glibc 2.10:</dt>
<dd> <p> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L </p>
 </dd>
<dt>Before glibc 2.10:</dt>
<dd> <p> _GNU_SOURCE </p>
 </dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>wcsnrtombs</code>() function is like the <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3) function, except that the number of wide characters to be converted, starting at <i>*src</i>, is limited to <i>nwc</i>. </p>
<p>If <i>dest</i> is not NULL, the <code>wcsnrtombs</code>() function converts at most <i>nwc</i> wide characters from the wide-character string <i>*src</i> to a multibyte string starting at <i>dest</i>. At most <i>len</i> bytes are written to <i>dest</i>. The shift state <i>*ps</i> is updated. The conversion is effectively performed by repeatedly calling <i>wcrtomb(dest, *src, ps)</i>, as long as this call succeeds, and then incrementing <i>dest</i> by the number of bytes written and <i>*src</i> by one. The conversion can stop for three reasons: </p>
<dl>
<dt>1.</dt>
<dd> <p> A wide character has been encountered that can not be represented as a multibyte sequence (according to the current locale). In this case, <i>*src</i> is left pointing to the invalid wide character, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>EILSEQ</code>. </p>
 </dd>
<dt>2.</dt>
<dd> <p> <i>nwc</i> wide characters have been converted without encountering a null wide character (L&#8217;\0&#8217;), or the length limit forces a stop. In this case, <i>*src</i> is left pointing to the next wide character to be converted, and the number of bytes written to <i>dest</i> is returned. </p>
 </dd>
<dt>3.</dt>
<dd> <p> The wide-character string has been completely converted, including the terminating null wide character (which has the side effect of bringing back <i>*ps</i> to the initial state). In this case, <i>*src</i> is set to NULL, and the number of bytes written to <i>dest</i>, excluding the terminating null byte (&#8216;\0&#8217;), is returned. </p>
 </dd></dl>
<p>If <i>dest</i> is NULL, <i>len</i> is ignored, and the conversion proceeds as above, except that the converted bytes are not written out to memory, and that no destination length limit exists. </p>
<p>In both of the above cases, if <i>ps</i> is NULL, a static anonymous state known only to the <code>wcsnrtombs</code>() function is used instead. </p>
<p>The programmer must ensure that there is room for at least <i>len</i> bytes at <i>dest</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>wcsnrtombs</code>() function returns the number of bytes that make up the converted part of multibyte sequence, not including the terminating null byte. If a wide character was encountered which could not be converted, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> set to <code>EILSEQ</code>.  </p>
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
<td> <code>wcsnrtombs</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:wcsnrtombs/!ps
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>wcsnrtombs</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p>Passing NULL as <i>ps</i> is not multithread safe.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/3-mbsinit/">mbsinit</a></code>(3), <code><a href="/docs/linux/man/3-wcsrtombs/">wcsrtombs</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">RETURN VALUE</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">ATTRIBUTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">CONFORMING TO</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">NOTES</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">COLOPHON</a></dt>
<dd>  </dd></dl>
