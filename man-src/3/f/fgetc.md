---

title: "fgetc(3)"
name: "fgetc"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetc/"
description: "fgetc, fgets, getc, getchar, ungetc – input of characters and strings"
---

<p> fgetc, fgets, getc, getchar, ungetc &#8211; input of characters and strings </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
int fgetc(FILE *stream);
char *fgets(char *s, int size, FILE *stream);
int getc(FILE *stream);
int getchar(void);
int ungetc(int c, FILE *stream);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>fgetc</code>() reads the next character from <i>stream</i> and returns it as an <i>unsigned char</i> cast to an <i>int</i>, or <code>EOF</code> on end of file or error. </p>
<p> <code>getc</code>() is equivalent to <code>fgetc</code>() except that it may be implemented as a macro which evaluates <i>stream</i> more than once. </p>
<p> <code>getchar</code>() is equivalent to <code>getc(</code><i>stdin</i><code>)</code><i></i>. </p>
<p> <code>fgets</code>() reads in at most one less than <i>size</i> characters from <i>stream</i> and stores them into the buffer pointed to by <i>s</i>. Reading stops after an <code>EOF</code> or a newline. If a newline is read, it is stored into the buffer. A terminating null byte (&#8216;\0&#8217;) is stored after the last character in the buffer. </p>
<p> <code>ungetc</code>() pushes <i>c</i> back to <i>stream</i>, cast to <i>unsigned char</i>, where it is available for subsequent read operations. Pushed-back characters will be returned in reverse order; only one pushback is guaranteed. </p>
<p> Calls to the functions described here can be mixed with each other and with calls to other input functions from the <i>stdio</i> library for the same input stream. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).  </p>
<h2>RETURN VALUE</h2>
<p> <code>fgetc</code>(), <code>getc</code>(), and <code>getchar</code>() return the character read as an <i>unsigned char</i> cast to an <i>int</i> or <code>EOF</code> on end of file or error. </p>
<p> <code>fgets</code>() returns <i>s</i> on success, and NULL on error or when end of file occurs while no characters have been read. </p>
<p> <code>ungetc</code>() returns <i>c</i> on success, or <code>EOF</code> on error.  </p>
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
<td> <code>fgetc</code>(), <code>fgets</code>(), <code>getc</code>(),  <code>getchar</code>(), <code>ungetc</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99. </p>
<p> It is not advisable to mix calls to input functions from the <i>stdio</i> library with low-level calls to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) for the file descriptor associated with the input stream; the results will be undefined and very probably not what you want.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3), <code><a href="/docs/linux/man/3-fgetwc/">fgetwc</a></code>(3), <code><a href="/docs/linux/man/3-fgetws/">fgetws</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fread/">fread</a></code>(3), <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3), <code><a href="/docs/linux/man/3-getline/">getline</a></code>(3), <code><a href="/docs/linux/man/3-gets/">gets</a></code>(3), <code><a href="/docs/linux/man/3-getwchar/">getwchar</a></code>(3), <code><a href="/docs/linux/man/3-puts/">puts</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3), <code><a href="/docs/linux/man/3-ungetwc/">ungetwc</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
