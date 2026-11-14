---
title: "putenv(3)"
name: "putenv"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putenv/"
description: "putenv – change or add an environment variable"
---

<p>putenv &#8211; change or add an environment variable</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int putenv(char *string);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>putenv</code>(): _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>putenv</code>() function adds or changes the value of environment variables. The argument <i>string</i> is of the form <i>name</i>=<i>value</i>. If <i>name</i> does not already exist in the environment, then <i>string</i> is added to the environment. If <i>name</i> does exist, then the value of <i>name</i> in the environment is changed to <i>value</i>. The string pointed to by <i>string</i> becomes part of the environment, so altering the string changes the environment.</p>
<h2>Return Value</h2>
<p>The <code>putenv</code>() function returns zero on success, or nonzero if an error occurs. In the event of an error, <i>errno</i> is set to indicate the cause.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>Insufficient space to allocate new environment.</dl>
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
<td> <code>putenv</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe const:env
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>Notes</h2>
<p>The <code>putenv</code>() function is not required to be reentrant, and the one in glibc 2.0 is not, but the glibc 2.1 version is. </p>
<p> Since version 2.1.2, the glibc implementation conforms to SUSv2: the pointer <i>string</i> given to <code>putenv</code>() is used. In particular, this string becomes part of the environment; changing it later will change the environment. (Thus, it is an error to call <code>putenv</code>() with an automatic variable as the argument, then return from the calling function while <i>string</i> is still part of the environment.) However, glibc versions 2.0 to 2.1.1 differ: a copy of the string is used. On the one hand this causes a memory leak, and on the other hand it violates SUSv2. </p>
<p> The 4.4BSD version, like glibc 2.0, uses a copy. </p>
<p> SUSv2 removes the <i>const</i> from the prototype, and so does glibc 2.1.3. </p>
<p> The GNU C library implementation provides a nonstandard extension. If <i>string</i> does not include an equal sign: </p>
<p> putenv(&quot;NAME&quot;); </p>
<p> then the named variable is removed from the caller&#8217;s environment.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-clearenv/">clearenv</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
