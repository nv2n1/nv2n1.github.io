---

title: "gets(3)"
name: "gets"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gets/"
description: "gets – get a string from standard input (DEPRECATED)"
---

<pre><code>
#include &lt;stdio.h&gt;
char *gets(char *s);
</code></pre>
<p> <i>Never use this function</i>. </p>
<p> <code>gets</code>() reads a line from <i>stdin</i> into the buffer pointed to by <i>s</i> until either a terminating newline or <code>EOF</code>, which it replaces with a null byte (&#8216;\0&#8217;). No check for buffer overrun is performed (see BUGS below).  </p>
<h2>RETURN VALUE</h2>
<p> <code>gets</code>() returns <i>s</i> on success, and NULL on error or when end of file occurs while no characters have been read. However, given the lack of buffer overrun checking, there can be no guarantees that the function will even return.  </p>
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
<td> <code>gets</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> C89, C99, POSIX.1-2001. </p>
<p> LSB deprecates <code>gets</code>(). POSIX.1-2008 marks <code>gets</code>() obsolescent. ISO C11 removes the specification of <code>gets</code>() from the C language, and since version 2.16, glibc header files don&#8217;t expose the function declaration if the <code>_ISOC11_SOURCE</code> feature test macro is defined.  </p>
<h2>BUGS</h2>
<p> Never use <code>gets</code>(). Because it is impossible to tell without knowing the data in advance how many characters <code>gets</code>() will read, and because <code>gets</code>() will continue to store characters past the end of the buffer, it is extremely dangerous to use. It has been used to break computer security. Use <code>fgets</code>() instead. </p>
<p> For more information, see CWE-242 (aka &quot;Use of Inherently Dangerous Function&quot;) at <a rel="nofollow" href="http://cwe.mitre.org/data/definitions/242.html">http://cwe.mitre.org/data/definitions/242.html</a>  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3), <code><a href="/docs/linux/man/3-fgetc/">fgetc</a></code>(3), <code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3), <code><a href="/docs/linux/man/3-fgetwc/">fgetwc</a></code>(3), <code><a href="/docs/linux/man/3-fgetws/">fgetws</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3), <code><a href="/docs/linux/man/3-getline/">getline</a></code>(3), <code><a href="/docs/linux/man/3-getwchar/">getwchar</a></code>(3), <code><a href="/docs/linux/man/3-puts/">puts</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3), <code><a href="/docs/linux/man/3-ungetwc/">ungetwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
