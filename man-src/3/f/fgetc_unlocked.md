---
title: "fgetc_unlocked(3)"
name: "fgetc_unlocked"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fgetc_unlocked/"
description: "getc_unlocked, getchar_unlocked, putc_unlocked, putchar_unlocked – nonlocking stdio functions"
---

<h2 class="name">NAME</h2>
<p> getc_unlocked, getchar_unlocked, putc_unlocked, putchar_unlocked &#8211; nonlocking stdio functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
int getc_unlocked(FILE *stream);
int getchar_unlocked(void);
int putc_unlocked(int c, FILE *stream);
int putchar_unlocked(int c);
void clearerr_unlocked(FILE *stream);
int feof_unlocked(FILE *stream);
int ferror_unlocked(FILE *stream);
int fileno_unlocked(FILE *stream);
int fflush_unlocked(FILE *stream);
int fgetc_unlocked(FILE *stream);
int fputc_unlocked(int c, FILE *stream);
size_t fread_unlocked(void *ptr, size_t size, size_t n,
                      FILE *stream);
size_t fwrite_unlocked(const void *ptr, size_t size, size_t n,
                       FILE *stream);
char *fgets_unlocked(char *s, int n, FILE *stream);
int fputs_unlocked(const char *s, FILE *stream);
#include &lt;wchar.h&gt;
wint_t getwc_unlocked(FILE *stream);
wint_t getwchar_unlocked(void);
wint_t fgetwc_unlocked(FILE *stream);
wint_t fputwc_unlocked(wchar_t wc, FILE *stream);
wint_t putwc_unlocked(wchar_t wc, FILE *stream);
wint_t putwchar_unlocked(wchar_t wc);
wchar_t *fgetws_unlocked(wchar_t *ws, int n, FILE *stream);
int fputws_unlocked(const wchar_t *ws, FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getc_unlocked</code>(), <code>getchar_unlocked</code>(), <code>putc_unlocked</code>(), <code>putchar_unlocked</code>():</p>
<dl>
<dt>
<dd> /* Since glibc 2.24: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.23:&nbsp;*/&nbsp;_POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<p> <code>clearerr_unlocked</code>(), <code>feof_unlocked</code>(), <code>ferror_unlocked</code>(), <code>fileno_unlocked</code>(), <code>fflush_unlocked</code>(), <code>fgetc_unlocked</code>(), <code>fputc_unlocked</code>(), <code>fread_unlocked</code>(), <code>fwrite_unlocked</code>():</p>
<dl>
<dt>
<dd> /* Glibc since 2.19: */ _DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<p> <code>fgets_unlocked</code>(), <code>fputs_unlocked</code>(), <code>getwc_unlocked</code>(), <code>getwchar_unlocked</code>(), <code>fgetwc_unlocked</code>(), <code>fputwc_unlocked</code>(), <code>putwchar_unlocked</code>(), <code>fgetws_unlocked</code>(), <code>fputws_unlocked</code>():</p>
<dl>
<dt>
<dd> _GNU_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> Each of these functions has the same behavior as its counterpart without the &quot;_unlocked&quot; suffix, except that they do not use locking (they do not set locks themselves, and do not test for the presence of locks set by others) and hence are thread-unsafe. See <code><a href="/docs/linux/man/3-flockfile/">flockfile</a></code>(3).</p>
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
<td> <code>getc_unlocked</code>(), <code>putc_unlocked</code>(), <code>clearerr_unlocked</code>(), <code>fflush_unlocked</code>(), <code>fgetc_unlocked</code>(), <code>fputc_unlocked</code>(), <code>fread_unlocked</code>(), <code>fwrite_unlocked</code>(), <code>fgets_unlocked</code>(), <code>fputs_unlocked</code>(), <code>getwc_unlocked</code>(), <code>fgetwc_unlocked</code>(), <code>fputwc_unlocked</code>(), <code>putwc_unlocked</code>(), <code>fgetws_unlocked</code>(), <code>fputws_unlocked</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:stream
</td>
</tr>
<tr VALIGN=top>
<td> <code>getchar_unlocked</code>(), <code>getwchar_unlocked</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:stdin
</td>
</tr>
<tr VALIGN=top>
<td> <code>putchar_unlocked</code>(), <code>putwchar_unlocked</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:stdout
</td>
</tr>
<tr VALIGN=top>
<td> <code>feof_unlocked</code>(), <code>ferror_unlocked</code>(), <code>fileno_unlocked</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The four functions <code>getc_unlocked</code>(), <code>getchar_unlocked</code>(), <code>putc_unlocked</code>(), <code>putchar_unlocked</code>() are in POSIX.1-2001 and POSIX.1-2008. </p>
<p> The nonstandard <code>*_unlocked</code>() variants occur on a few UNIX systems, and are available in recent glibc. They should probably not be used.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-flockfile/">flockfile</a></code>(3), <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
