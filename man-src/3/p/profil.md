---
title: "profil(3)"
name: "profil"
section: "3"
letter: "p"
url: "/docs/linux/man/3-profil/"
description: "profil – execution time profile"
---

<p>profil &#8211; execution time profile</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

int profil(unsigned short *buf, size_t bufsiz,
           size_t offset, unsigned int scale);

Feature Test Macro Requirements for glibc (see
feature_test_macros(7)):</code></pre>
<p> <code>profil</code>(): </p>
<pre> Since glibc 2.21:
 _DEFAULT_SOURCE
 In glibc 2.19 and 2.20:
 _DEFAULT_SOURCE || (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE&nbsp;&lt;&nbsp;500)
 Up to and including glibc 2.19:
 _BSD_SOURCE || (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE&nbsp;&lt;&nbsp;500)</pre>
<h2>Description</h2>
<p>This routine provides a means to find out in what areas your program spends most of its time. The argument <i>buf</i> points to <i>bufsiz</i> bytes of core. Every virtual 10 milliseconds, the user&#8217;s program counter (PC) is examined: <i>offset</i> is subtracted and the result is multiplied by <i>scale</i> and divided by 65536. If the resulting value is less than <i>bufsiz</i>, then the corresponding entry in <i>buf</i> is incremented. If <i>buf</i> is NULL, profiling is disabled.</p>
<h2>Return Value</h2>
<p>Zero is always returned.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>profil</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>Similar to a call in SVr4 (but not POSIX.1).</p>
<h2>Bugs</h2>
<p><code>profil</code>() cannot be used on a program that also uses <code>ITIMER_PROF</code> interval timers (see <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2)). </p>
<p> True kernel profiling provides more accurate results.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gprof/">gprof</a></code>(1), <code><a href="/docs/linux/man/1-sprof/">sprof</a></code>(1), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
