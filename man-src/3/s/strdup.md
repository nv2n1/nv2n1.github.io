---
title: "strdup(3)"
name: "strdup"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strdup/"
description: "strdup, strndup, strdupa, strndupa – duplicate a string"
---

<p>strdup, strndup, strdupa, strndupa &#8211; duplicate a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strdup(const char *s);
char *strndup(const char *s, size_t n);
char *strdupa(const char *s);
char *strndupa(const char *s, size_t n);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strdup</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dd></dl>
<p> <code>strndup</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<p> <code>strdupa</code>(), <code>strndupa</code>(): _GNU_SOURCE</p>
<h2>Description</h2>
<p>The <code>strdup</code>() function returns a pointer to a new string which is a duplicate of the string <i>s</i>. Memory for the new string is obtained with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and can be freed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> The <code>strndup</code>() function is similar, but copies at most <i>n</i> bytes. If <i>s</i> is longer than <i>n</i>, only <i>n</i> bytes are copied, and a terminating null byte (&#8216;\0&#8217;) is added. </p>
<p> <code>strdupa</code>() and <code>strndupa</code>() are similar, but use <code><a href="/docs/linux/man/3-alloca/">alloca</a></code>(3) to allocate the buffer. They are available only when using the GNU GCC suite, and suffer from the same limitations described in <code><a href="/docs/linux/man/3-alloca/">alloca</a></code>(3).  </p>
<h2>RETURN VALUE</h2>
<p> On success, the <code>strdup</code>() function returns a pointer to the duplicated string. It returns NULL if insufficient memory was available, with <i>errno</i> set to indicate the cause of the error.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></dt>
<dd> <p> Insufficient memory available to allocate duplicate string. </p>
 </dd></dl>
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
<td> <code>strdup</code>(), <code>strndup</code>(), <code>strdupa</code>(),  <code>strndupa</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>strdup</code>() conforms to SVr4, 4.3BSD, POSIX.1-2001. <code>strndup</code>() conforms to POSIX.1-2008. <code>strdupa</code>() and <code>strndupa</code>() are GNU extensions.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-alloca/">alloca</a></code>(3), <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-wcsdup/">wcsdup</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
