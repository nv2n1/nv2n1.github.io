---
title: "vwprintf(3)"
name: "vwprintf"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vwprintf/"
description: "wprintf, fwprintf, swprintf, vwprintf, vfwprintf, vswprintf – formatted wide-character output conversion"
---
<p>wprintf, fwprintf, swprintf, vwprintf, vfwprintf, vswprintf &#8211; formatted wide-character output conversion </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;stdio.h&gt; 
 #include &lt;wchar.h&gt; 
 int wprintf(const wchar_t *  format  , ...); 
 int fwprintf(FILE *  stream  , const wchar_t *  format  , ...); 
 int swprintf(wchar_t *  wcs  , size_t  maxlen  , 
              const wchar_t *  format  , ...); 
 int vwprintf(const wchar_t *  format  , va_list  args  ); 
 int vfwprintf(FILE *  stream  , const wchar_t *  format  , va_list  args  ); 
 int vswprintf(wchar_t *  wcs  , size_t  maxlen  , 
               const wchar_t *  format  , va_list  args  ); 
</code></pre>
<p>Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p>All functions shown above: </p>
<dl>
<dd> <p> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _ISOC99_SOURCE || <br />
 _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L </p>
 </dd></dl>
<h2>DESCRIPTION</h2>
<p> The <code>wprintf</code>() family of functions is the wide-character equivalent of the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) family of functions. It performs formatted output of wide characters. </p>
<p>The <code>wprintf</code>() and <code>vwprintf</code>() functions perform wide-character output to <i>stdout</i>. <i>stdout</i> must not be byte oriented; see <code><a href="/docs/linux/man/3-fwide/">fwide</a></code>(3) for more information. </p>
<p>The <code>fwprintf</code>() and <code>vfwprintf</code>() functions perform wide-character output to <i>stream</i>. <i>stream</i> must not be byte oriented; see <code><a href="/docs/linux/man/3-fwide/">fwide</a></code>(3) for more information. </p>
<p>The <code>swprintf</code>() and <code>vswprintf</code>() functions perform wide-character output to an array of wide characters. The programmer must ensure that there is room for at least <i>maxlen</i> wide characters at <i>wcs</i>. </p>
<p>These functions are like the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-vfprintf/">vfprintf</a></code>(3), <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3) functions except for the following differences: </p>
<dl>
<dt><code>&bull;</code></dt>
<dd> <p> The <i>format</i> string is a wide-character string. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> The output consists of wide characters, not bytes. </p>
 </dd>
<dt><code>&bull;</code></dt>
<dd> <p> <code>swprintf</code>() and <code>vswprintf</code>() take a <i>maxlen</i> argument, <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3) do not. (<code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsnprintf/">vsnprintf</a></code>(3) take a <i>maxlen</i> argument, but these functions do not return -1 upon buffer overflow on Linux.) </p>
 </dd></dl>
<p>The treatment of the conversion characters <code>c</code> and <code>s</code> is different: </p>
<dl>
<dt><code>c</code></dt>
<dd> <p> If no <code>l</code> modifier is present, the <i>int</i> argument is converted to a wide character by a call to the <code><a href="/docs/linux/man/3-btowc/">btowc</a></code>(3) function, and the resulting wide character is written. If an <code>l</code> modifier is present, the <i>wint_t</i> (wide character) argument is written. </p>
 </dd>
<dt><code>s</code></dt>
<dd> <p> If no <code>l</code> modifier is present: the <i>const char&nbsp;*</i> argument is expected to be a pointer to an array of character type (pointer to a string) containing a multibyte character sequence beginning in the initial shift state. Characters from the array are converted to wide characters (each by a call to the <code><a href="/docs/linux/man/3-mbrtowc/">mbrtowc</a></code>(3) function with a conversion state starting in the initial state before the first byte). The resulting wide characters are written up to (but not including) the terminating null wide character (L&#8217;\0&#8217;). If a precision is specified, no more wide characters than the number specified are written. Note that the precision determines the number of <i>wide characters</i> written, not the number of <i>bytes</i> or <i>screen positions</i>. The array must contain a terminating null byte (&#8216;\0&#8217;), unless a precision is given and it is so small that the number of converted wide characters reaches it before the end of the array is reached. If an <code>l</code> modifier is present: the <i>const wchar_t&nbsp;*</i> argument is expected to be a pointer to an array of wide characters. Wide characters from the array are written up to (but not including) a terminating null wide character. If a precision is specified, no more than the number specified are written. The array must contain a terminating null wide character, unless a precision is given and it is smaller than or equal to the number of wide characters in the array. </p>
 </dd></dl>
<h2>RETURN VALUE</h2>
<p> The functions return the number of wide characters written, excluding the terminating null wide character in case of the functions <code>swprintf</code>() and <code>vswprintf</code>(). They return -1 when an error occurs.  </p>
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
<td> <code>wprintf</code>(), <code>fwprintf</code>(),  <code>swprintf</code>(), <code>vwprintf</code>(),  <code>vfwprintf</code>(), <code>vswprintf</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>wprintf</code>() et al. depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p>If the <i>format</i> string contains non-ASCII wide characters, the program will work correctly only if the <code>LC_CTYPE</code> category of the current locale at run time is the same as the <code>LC_CTYPE</code> category of the current locale at compile time. This is because the <i>wchar_t</i> representation is platform- and locale-dependent. (The glibc represents wide characters using their Unicode (ISO-10646) code point, but other platforms don&#8217;t do this. Also, the use of C99 universal character names of the form \unnnn does not solve this problem.) Therefore, in internationalized programs, the <i>format</i> string should consist of ASCII wide characters only, or should be constructed at run time in an internationalized way (e.g., using <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3) or <code><a href="/docs/linux/man/3-iconv/">iconv</a></code>(3), followed by <code><a href="/docs/linux/man/3-mbstowcs/">mbstowcs</a></code>(3)).  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-fputwc/">fputwc</a></code>(3), <code><a href="/docs/linux/man/3-fwide/">fwide</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-snprintf/">snprintf</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
