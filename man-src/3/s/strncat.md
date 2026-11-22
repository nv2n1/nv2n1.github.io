---
title: "strncat(3)"
name: "strncat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strncat/"
description: "strcat, strncat – concatenate two strings"
---

<p>strcat, strncat &#8211; concatenate two strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strcat(char *dest, const char *src);
char *strncat(char *dest, const char *src, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>strcat</code>() function appends the <i>src</i> string to the <i>dest</i> string, overwriting the terminating null byte (&#8216;\0&#8217;) at the end of <i>dest</i>, and then adds a terminating null byte. The strings may not overlap, and the <i>dest</i> string must have enough space for the result. If <i>dest</i> is not large enough, program behavior is unpredictable; <i>buffer overruns are a favorite avenue for attacking secure programs</i>. </p>
<p> The <code>strncat</code>() function is similar, except that </p>
<dl>
<dt>*</dt>
<dd> <p> it will use at most <i>n</i> bytes from <i>src</i>; and </p>
 </dd>
<dt>*</dt>
<dd> <p> <i>src</i> does not need to be null-terminated if it contains <i>n</i> or more bytes. </p>
 </dd></dl>
<p> As with <code>strcat</code>(), the resulting string in <i>dest</i> is always null-terminated. </p>
<p> If <i>src</i> contains <i>n</i> or more bytes, <code>strncat</code>() writes <i>n+1</i> bytes to <i>dest</i> (<i>n</i> from <i>src</i> plus the terminating null byte). Therefore, the size of <i>dest</i> must be at least <i>strlen(dest)+n+1</i>. </p>
<p> A simple implementation of <code>strncat</code>() might be: </p>
<p> char * strncat(char *dest, const char *src, size_t n) { <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t dest_len&nbsp;=&nbsp;strlen(dest); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t i; </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(i&nbsp;=&nbsp;0&nbsp;;&nbsp;i&nbsp;&lt;&nbsp;n&nbsp;&amp;&amp;&nbsp;src[i]&nbsp;!=&nbsp;&#8216;\0&#8217;&nbsp;;&nbsp;i++) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dest[dest_len&nbsp;+&nbsp;i]&nbsp;=&nbsp;src[i]; <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dest[dest_len&nbsp;+&nbsp;i]&nbsp;=&nbsp;&#8216;\0&#8217;; </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return dest; }  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strcat</code>() and <code>strncat</code>() functions return a pointer to the resulting string <i>dest</i>.  </p>
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
<td> <code>strcat</code>(), <code>strncat</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.  </p>
<h2>NOTES</h2>
<p> Some systems (the BSDs, Solaris, and others) provide the following function: </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t strlcat(char&nbsp;*dest, const char&nbsp;*src, size_t size); </p>
<p> This function appends the null-terminated string <i>src</i> to the string <i>dest</i>, copying at most <i>size-strlen(dest)-1</i> from <i>src</i>, and adds a terminating null byte to the result, <i>unless</i> <i>size</i> is less than <i>strlen(dest)</i>. This function fixes the buffer overrun problem of <code>strcat</code>(), but the caller must still handle the possibility of data loss if <i>size</i> is too small. The function returns the length of the string <code>strlcat</code>() tried to create; if the return value is greater than or equal to <i>size</i>, data loss occurred. If data loss matters, the caller <i>must</i> either check the arguments before the call, or test the function return value. <code>strlcat</code>() is not present in glibc and is not standardized by POSIX, but is available on Linux via the <i>libbsd</i> library.  </p>
<h2>EXAMPLES</h2>
<p> Because <code>strcat</code>() and <code>strncat</code>() must find the null byte that terminates the string <i>dest</i> using a search that starts at the beginning of the string, the execution time of these functions scales according to the length of the string <i>dest</i>. This can be demonstrated by running the program below. (If the goal is to concatenate many strings to one target, then manually copying the bytes from each source string while maintaining a pointer to the end of the target string will provide better performance.)  </p>
<h3>Program source</h3>
<p> #include &lt;stdint.h&gt; #include &lt;string.h&gt; #include &lt;time.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(int argc, char *argv[]) { #define LIM 4000000 <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char p[LIM&nbsp;+&nbsp;1];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;+1 for terminating null byte&nbsp;*/ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t base; </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base&nbsp;=&nbsp;time(NULL); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p[0]&nbsp;=&nbsp;&#8216;\0&#8217;; </p>
<p> <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;LIM;&nbsp;j++)&nbsp;{ <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;((j&nbsp;%&nbsp;10000)&nbsp;==&nbsp;0) <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d&nbsp;%jd\n&quot;, j,&nbsp;(intmax_t)&nbsp;(time(NULL)&nbsp;- base)); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strcat(p,&nbsp;&quot;a&quot;); <br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bcopy/">bcopy</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-wcscat/">wcscat</a></code>(3), <code><a href="/docs/linux/man/3-wcsncat/">wcsncat</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
