---
title: "bstring(3)"
name: "bstring"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bstring/"
description: "bcmp, bcopy, bzero, memccpy, memchr, memcmp, memcpy, memfrob, memmem, memmove, memset – byte string operations"
---

<h2 class="name">NAME</h2>
<p> bcmp, bcopy, bzero, memccpy, memchr, memcmp, memcpy, memfrob, memmem, memmove, memset &#8211; byte string operations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;string.h&gt;
int bcmp(const void *s1, const void *s2, size_t n);
void bcopy(const void *src, void *dest, size_t n);
void bzero(void *s, size_t n);
void *memccpy(void *dest, const void *src, int c, size_t n);
void *memchr(const void *s, int c, size_t n);
int memcmp(const void *s1, const void *s2, size_t n);
void *memcpy(void *dest, const void *src, size_t n);
void *memfrob(void *s, size_t n);
void *memmem(const void *haystack, size_t haystacklen,
             const void *needle, size_t needlelen);
void *memmove(void *dest, const void *src, size_t n);
void *memset(void *s, int c, size_t n);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The byte string functions perform operations on strings (byte arrays) that are not necessarily null-terminated. See the individual man pages for descriptions of each function.</p>
<h2>NOTES</h2>
<p> The functions <code>bcmp</code>(), <code>bcopy</code>(), and <code>bzero</code>() are obsolete. Use <code>memcmp</code>(), <code>memcpy</code>(), and <code>memset</code>() instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bcmp/">bcmp</a></code>(3), <code><a href="/docs/linux/man/3-bcopy/">bcopy</a></code>(3), <code><a href="/docs/linux/man/3-bzero/">bzero</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memchr/">memchr</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memfrob/">memfrob</a></code>(3), <code><a href="/docs/linux/man/3-memmem/">memmem</a></code>(3), <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3), <code><a href="/docs/linux/man/3-memset/">memset</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
