---

title: "mbrtowc(3)"
name: "mbrtowc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbrtowc/"
description: "mbrtowc – convert a multibyte sequence to a wide character"
---

<p> mbrtowc &#8211; convert a multibyte sequence to a wide character </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;wchar.h&gt;
size_t mbrtowc(wchar_t *pwc, const char *s, size_t n, mbstate_t *ps);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The main case for this function is when <i>s</i> is not NULL and <i>pwc</i> is not NULL. In this case, the <code>mbrtowc</code>() function inspects at most <i>n</i> bytes of the multibyte string starting at <i>s</i>, extracts the next complete multibyte character, converts it to a wide character and stores it at <i>*pwc</i>. It updates the shift state <i>*ps</i>. If the converted wide character is not L&#8217;\0&#8217; (the null wide character), it returns the number of bytes that were consumed from <i>s</i>. If the converted wide character is L&#8217;\0&#8217;, it resets the shift state <i>*ps</i> to the initial state and returns 0. </p>
<p> If the <i>n</i> bytes starting at <i>s</i> do not contain a complete multibyte character, <code>mbrtowc</code>() returns <i>(size_t)&nbsp;-2</i>. This can happen even if <i>n</i> &gt;= <i>MB_CUR_MAX</i>, if the multibyte string contains redundant shift sequences. </p>
<p> If the multibyte string starting at <i>s</i> contains an invalid multibyte sequence before the next complete character, <code>mbrtowc</code>() returns <i>(size_t)&nbsp;-1</i> and sets <i>errno</i> to <code>EILSEQ</code>. In this case, the effects on <i>*ps</i> are undefined. </p>
<p> A different case is when <i>s</i> is not NULL but <i>pwc</i> is NULL. In this case, the <code>mbrtowc</code>() function behaves as above, except that it does not store the converted wide character in memory. </p>
<p> A third case is when <i>s</i> is NULL. In this case, <i>pwc</i> and <i>n</i> are ignored. If the conversion state represented by <i>*ps</i> denotes an incomplete multibyte character conversion, the <code>mbrtowc</code>() function returns <i>(size_t)&nbsp;-1</i>, sets <i>errno</i> to <code>EILSEQ</code>, and leaves <i>*ps</i> in an undefined state. Otherwise, the <code>mbrtowc</code>() function puts <i>*ps</i> in the initial state and returns 0. </p>
<p> In all of the above cases, if <i>ps</i> is NULL, a static anonymous state known only to the <code>mbrtowc</code>() function is used instead. Otherwise, <i>*ps</i> must be a valid <i>mbstate_t</i> object. An <i>mbstate_t</i> object <i>a</i> can be initialized to the initial state by zeroing it, for example using </p>
<p> memset(&amp;a, 0, sizeof(a));  </p>
<h2>RETURN VALUE</h2>
<p> The <code>mbrtowc</code>() function returns the number of bytes parsed from the multibyte sequence starting at <i>s</i>, if a non-L&#8217;\0&#8217; wide character was recognized. It returns 0, if a L&#8217;\0&#8217; wide character was recognized. It returns <i>(size_t)&nbsp;-1</i> and sets <i>errno</i> to <code>EILSEQ</code>, if an invalid multibyte sequence was encountered. It returns <i>(size_t)&nbsp;-2</i> if it couldn&#8217;t parse a complete multibyte character, meaning that <i>n</i> should be increased.  </p>
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
<td> <code>mbrtowc</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:mbrtowc/!ps
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>mbrtowc</code>() depends on the <code>LC_CTYPE</code> category of the current locale.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mbsinit/">mbsinit</a></code>(3), <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
