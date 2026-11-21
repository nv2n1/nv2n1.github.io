---
title: "putchar(3)"
name: "putchar"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putchar/"
description: "fputc, fputs, putc, putchar, puts – output of characters and strings"
---

<p>fputc, fputs, putc, putchar, puts &#8211; output of characters and strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;
int fputc(int c, FILE *stream);
int fputs(const char *s, FILE *stream);
int putc(int c, FILE *stream);
int putchar(int c);
int puts(const char *s);</code></pre>
<h2>Description</h2>
<p><code>fputc</code>() writes the character <i>c</i>, cast to an <i>unsigned char</i>, to <i>stream</i>. </p>
<p> <code>fputs</code>() writes the string <i>s</i> to <i>stream</i>, without its terminating null byte (&#8216;\0&#8217;). </p>
<p> <code>putc</code>() is equivalent to <code>fputc</code>() except that it may be implemented as a macro which evaluates <i>stream</i> more than once. </p>
<p> <code>putchar(</code><i>c</i><code>)</code> is equivalent to <code>putc(</code><i>c</i><code>, </code><i>stdout</i><code>)</code><i></i>. </p>
<p> <code>puts</code>() writes the string <i>s</i> and a trailing newline to <i>stdout</i>. </p>
<p> Calls to the functions described here can be mixed with each other and with calls to other output functions from the <i>stdio</i> library for the same output stream. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).  </p>
<h2>RETURN VALUE</h2>
<p> <code>fputc</code>(), <code>putc</code>(), and <code>putchar</code>() return the character written as an <i>unsigned char</i> cast to an <i>int</i> or <code>EOF</code> on error. </p>
<p> <code>puts</code>() and <code>fputs</code>() return a nonnegative number on success, or <code>EOF</code> on error.  </p>
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
<td> <code>fputc</code>(), <code>fputs</code>(), <code>putc</code>(), <code>putchar</code>(), <code>puts</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99.  </p>
<h2>BUGS</h2>
<p> It is not advisable to mix calls to output functions from the <i>stdio</i> library with low-level calls to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) for the file descriptor associated with the same output stream; the results will be undefined and very probably not what you want.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3), <code><a href="/docs/linux/man/3-fgets/">fgets</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-fputwc/">fputwc</a></code>(3), <code><a href="/docs/linux/man/3-fputws/">fputws</a></code>(3), <code><a href="/docs/linux/man/3-fseek/">fseek</a></code>(3), <code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3), <code><a href="/docs/linux/man/3-putwchar/">putwchar</a></code>(3), <code><a href="/docs/linux/man/3-scanf/">scanf</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
