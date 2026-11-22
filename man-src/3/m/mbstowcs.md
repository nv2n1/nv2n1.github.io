---

title: "mbstowcs(3)"
name: "mbstowcs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mbstowcs/"
description: "mbstowcs – convert a multibyte string to a wide-character string"
---

<p> mbstowcs - convert a multibyte string to a wide-character string </p>
<h2>SYNOPSIS</h2>
<pre><code>
 #include &lt;stdlib.h&gt; 
 size_t mbstowcs(wchar_t *  dest  , const char *  src  , size_t  n  ); 
</code></pre>
<h2>DESCRIPTION</h2>
<p> If <i>dest</i> is not NULL, the <code>mbstowcs</code>() function converts the multibyte string <i>src</i> to a wide-character string starting at <i>dest</i>. At most <i>n</i> wide characters are written to <i>dest</i>. The sequence of characters in the string <i>src</i> shall begin in the initial shift state. The conversion can stop for three reasons: </p>
<dl>
<dt>1.</dt>
<dd> <p> An invalid multibyte sequence has been encountered. In this case, <i>(size_t)&nbsp;-1</i> is returned. </p>
 </dd>
<dt>2.</dt>
<dd> <p> <i>n</i> non-L&#8217;\0&#8217; wide characters have been stored at <i>dest</i>. In this case, the number of wide characters written to <i>dest</i> is returned, but the shift state at this point is lost. </p>
 </dd>
<dt>3.</dt>
<dd> <p> The multibyte string has been completely converted, including the terminating null character (&#8216;\0&#8217;). In this case, the number of wide characters written to <i>dest</i>, excluding the terminating null wide character, is returned. </p>
 </dd></dl>
<p> The programmer must ensure that there is room for at least <i>n</i> wide characters at <i>dest</i>. </p>
<p> If <i>dest</i> is NULL, <i>n</i> is ignored, and the conversion proceeds as above, except that the converted wide characters are not written out to memory, and that no length limit exists. </p>
<p> In order to avoid the case 2 above, the programmer should make sure <i>n</i> is greater than or equal to <i>mbstowcs(NULL,src,0)+1</i>.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>mbstowcs</code>() function returns the number of wide characters that make up the converted part of the wide-character string, not including the terminating null wide character. If an invalid multibyte sequence was encountered, <i>(size_t)&nbsp;-1</i> is returned.  </p>
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
<td> <code>mbstowcs</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C99.  </p>
<h2>NOTES</h2>
<p> The behavior of <code>mbstowcs</code>() depends on the <code>LC_CTYPE</code> category of the current locale. </p>
<p> The function <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3) provides a better interface to the same functionality.  </p>
<h2>EXAMPLES</h2>
<p> The program below illustrates the use of <code>mbstowcs</code>(), as well as some of the wide character classification functions. An example run is the following: </p>
<p> $ ./t_mbstowcs de_DE.UTF-8 Grüße! Length of source string (excluding terminator): <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8 bytes <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6 multibyte characters </p>
<p> Wide character string is: Grüße! (6 characters) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;G alpha upper <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r alpha lower <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ü&nbsp;alpha lower <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ß&nbsp;alpha lower <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e alpha lower <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!&nbsp;!alpha  </p>
<h3>Program source</h3>
<p> #include &lt;wctype.h&gt; #include &lt;locale.h&gt; #include &lt;wchar.h&gt; #include &lt;stdio.h&gt; #include &lt;string.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t mbslen;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of multibyte characters in source&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wchar_t&nbsp;*wcs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to converted wide character string&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;locale&gt;&nbsp;&lt;string&gt;\n&quot;, argv[0]); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Apply the specified locale&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(setlocale(LC_ALL, argv[1])&nbsp;==&nbsp;NULL)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;setlocale&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Calculate the length required to hold argv[2]&nbsp;converted to <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a wide character string&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mbslen&nbsp;=&nbsp;mbstowcs(NULL, argv[2], 0); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mbslen&nbsp;==&nbsp;(size_t)&nbsp;-1)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;mbstowcs&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Describe the source string to the user&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Length of source string&nbsp;(excluding terminator):\n&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%zu bytes\n&quot;, strlen(argv[2])); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%zu multibyte characters\n\n&quot;, mbslen); </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Allocate wide character string of the desired size.&nbsp;<wbr>&nbsp;Add 1 <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to allow for terminating null wide character&nbsp;(L&#8217;\0&#8217;).&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wcs&nbsp;=&nbsp;calloc(mbslen&nbsp;+&nbsp;1, sizeof(*wcs)); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(wcs&nbsp;==&nbsp;NULL)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;calloc&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Convert the multibyte character string in argv[2]&nbsp;to a <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wide character string&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mbstowcs(wcs, argv[2], mbslen&nbsp;+&nbsp;1)&nbsp;==&nbsp;(size_t)&nbsp;-1)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;mbstowcs&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Wide character string is:&nbsp;%ls&nbsp;(%zu characters)\n&quot;, <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wcs, mbslen); </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Now do some inspection of the classes of the characters in <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the wide character string&nbsp;*/ </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(wchar_t&nbsp;*wp&nbsp;=&nbsp;wcs;&nbsp;*wp&nbsp;!=&nbsp;0;&nbsp;wp++)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%lc&nbsp;&quot;,&nbsp;(wint_t)&nbsp;*wp); </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(!iswalpha(*wp)) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;!&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;alpha&nbsp;&quot;); </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(iswalpha(*wp))&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(iswupper(*wp)) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;upper&nbsp;&quot;); </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(iswlower(*wp)) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;lower&nbsp;&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;putchar(&#8216;\n&#8217;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mblen/">mblen</a></code>(3), <code><a href="/docs/linux/man/3-mbsrtowcs/">mbsrtowcs</a></code>(3), <code><a href="/docs/linux/man/3-mbtowc/">mbtowc</a></code>(3), <code><a href="/docs/linux/man/3-wcstombs/">wcstombs</a></code>(3), <code><a href="/docs/linux/man/3-wctomb/">wctomb</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
