---
title: "mbsnrtowcs(3)"
name: "mbsnrtowcs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbsnrtowcs/"
description: "mbsnrtowcs – convert a multibyte string to a wide-character string"
---
<h2 class="name">NAME</h2>
<p> mbsnrtowcs - convert a multibyte string to a wide-character string </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;wchar.h&gt; 
 size_t mbsnrtowcs(wchar_t *  dest  , const char **  src  , 
                   size_t  nms  , size_t  len  , mbstate_t *  ps  ); 
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mbsnrtowcs</code>(): </p>
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
<p> The <code>mbsnrtowcs</code>() function is like the <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3) function, except that the number of bytes to be converted, starting at <i>*src</i>, is limited to at most <i>nms</i> bytes. </p>
<p> If <i>dest</i> is not NULL, the <code>mbsnrtowcs</code>() function converts at most <i>nms</i> bytes from the multibyte string <i>*src</i> to a wide-character string starting at <i>dest</i>. At most <i>len</i> wide characters are written to <i>dest</i>. The shift state <i>*ps</i> is updated. The conversion is effectively performed by repeatedly calling <i>mbrtowc(dest, *src, n, ps)</i> where <i>n</i> is some positive number, as long as this call succeeds, and then incrementing <i>dest</i> by one and <i>*src</i> by the number of bytes consumed. The conversion can stop for three reasons: </p>
<dl>
<dt>1.</dt>
<dd> <p> An invalid multibyte sequence has been encountered. In this case, <i>*src</i> is left pointing to the invalid multibyte sequence, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>EILSEQ</code>. </p>
 </dd>
<dt>2.</dt>
<dd> <p> The <i>nms</i> limit forces a stop, or <i>len</i> non-L&#8217;\0&#8217; wide characters have been stored at <i>dest</i>. In this case, <i>*src</i> is left pointing to the next multibyte sequence to be converted, and the number of wide characters written to <i>dest</i> is returned. </p>
 </dd>
<dt>3.</dt>
<dd> <p> The multibyte string has been completely converted, including the terminating null wide character (&#8216;\0&#8217;) (which has the side effect of bringing back <i>*ps</i> to the initial state). In this case, <i>*src</i> is set to NULL, and the number of wide characters written to <i>dest</i>, excluding the terminating null wide character, is returned. </p>
 </dd></dl>
<p> According to POSIX.1, if the input buffer ends with an incomplete character, it is unspecified whether conversion stops at the end of the previous character (if any), or at the end of the input buffer. The glibc implementation adopts the former behavior. </p>
<p> If <i>dest</i> is NULL, <i>len</i> is ignored, and the conversion proceeds as above, except that the converted wide characters are not written out to memory, and that no destination length limit exists. </p>
<p> In both of the above cases, if <i>ps</i> is NULL, a static anonymous state known only to the <code>mbsnrtowcs</code>() function is used instead. </p>
<p> The programmer must ensure that there is room for at least <i>len</i> wide characters at <i>dest</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>mbsnrtowcs</code>() function returns the number of wide characters that make up the converted part of the wide-character string, not including the terminating null wide character. If an invalid multibyte sequence was encountered, <i>(size_t)&nbsp;-1</i> is returned, and <i>errno</i> set to <code>EILSEQ</code>.  </p>
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
<td> <code>mbsnrtowcs</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:mbsnrtowcs/!ps
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>mbsnrtowcs</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> Passing NULL as <i>ps</i> is not multithread safe.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3), <code><a href="/docs/linux/man/3-mbsinit/">mbsinit</a></code>(3), <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3)  </p>
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
