---
title: "setenv(3)"
name: "setenv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setenv/"
description: "setenv – change or add an environment variable"
---

<p>setenv &#8211; change or add an environment variable</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int setenv(const char *name, const char *value, int overwrite);

int unsetenv(const char *name);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>setenv</code>(), <code>unsetenv</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>Description</h2>
<p>The <code>setenv</code>() function adds the variable <i>name</i> to the environment with the value <i>value</i>, if <i>name</i> does not already exist. If <i>name</i> does exist in the environment, then its value is changed to <i>value</i> if <i>overwrite</i> is nonzero; if <i>overwrite</i> is zero, then the value of <i>name</i> is not changed (and <code>setenv</code>() returns a success status). This function makes copies of the strings pointed to by <i>name</i> and <i>value</i> (by contrast with <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3)). </p>
<p> The <code>unsetenv</code>() function deletes the variable <i>name</i> from the environment. If <i>name</i> does not exist in the environment, then the function succeeds, and the environment is unchanged.</p>
<h2>Return Value</h2>
<p><code>setenv</code>() and <code>unsetenv</code>() functions return zero on success, or -1 on error, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>name</i> is NULL, points to a string of length 0, or contains an &#8216;=&#8217; character.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory to add a new variable to the environment.</dl>
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
<td> <code>setenv</code>(), <code>unsetenv</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe const:env
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, 4.3BSD.</p>
<h2>Notes</h2>
<p>POSIX.1 does not require <code>setenv</code>() or <code>unsetenv</code>() to be reentrant. </p>
<p> Prior to glibc 2.2.2, <code>unsetenv</code>() was prototyped as returning <i>void</i>; more recent glibc versions follow the POSIX.1-compliant prototype shown in the SYNOPSIS.</p>
<h2>Bugs</h2>
<p>POSIX.1 specifies that if <i>name</i> contains an &#8216;=&#8217; character, then <code>setenv</code>() should fail with the error <code>EINVAL</code>; however, versions of glibc before 2.3.4 allowed an &#8216;=&#8217; sign in <i>name</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-clearenv/">clearenv</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
