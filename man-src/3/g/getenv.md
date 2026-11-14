---
title: "getenv(3)"
name: "getenv"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getenv/"
description: "getenv, secure_getenv – get an environment variable"
---

<h2 class="name">NAME</h2>
<p> getenv, secure_getenv &#8211; get an environment variable </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
char *getenv(const char *name);
char *secure_getenv(const char *name);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>secure_getenv</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>getenv</code>() function searches the environment list to find the environment variable <i>name</i>, and returns a pointer to the corresponding <i>value</i> string. </p>
<p> The GNU-specific <code>secure_getenv</code>() function is just like <code>getenv</code>() except that it returns NULL in cases where &quot;secure execution&quot; is required. Secure execution is required if one of the following conditions was true when the program run by the calling process was loaded:</p>
<dl>
<dt>*</p>
<dd> the process&#8217;s effective user ID did not match its real user ID or the process&#8217;s effective group ID did not match its real group ID (typically this is the result of executing a set-user-ID or set-group-ID program);</p>
<dt>*</p>
<dd> the effective capability bit was set on the executable file; or</p>
<dt>*</p>
<dd> the process has a nonempty permitted capability set.</dl>
<p> Secure execution may also be required if triggered by some Linux security modules. </p>
<p> The <code>secure_getenv</code>() function is intended for use in general-purpose libraries to avoid vulnerabilities that could occur if set-user-ID or set-group-ID programs accidentally trusted the environment.</p>
<h2>RETURN VALUE</h2>
<p> The <code>getenv</code>() function returns a pointer to the value in the environment, or NULL if there is no match.</p>
<h2>VERSIONS</h2>
<p> <code>secure_getenv</code>() first appeared in glibc 2.17.</p>
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
<td> <code>getenv</code>(), <code>secure_getenv</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>getenv</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD. </p>
<p> <code>secure_getenv</code>() is a GNU extension.</p>
<h2>NOTES</h2>
<p> The strings in the environment list are of the form <i>name=value</i>. </p>
<p> As typically implemented, <code>getenv</code>() returns a pointer to a string within the environment list. The caller must take care not to modify this string, since that would change the environment of the process. </p>
<p> The implementation of <code>getenv</code>() is not required to be reentrant. The string pointed to by the return value of <code>getenv</code>() may be statically allocated, and can be modified by a subsequent call to <code>getenv</code>(), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), or <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3). </p>
<p> The &quot;secure execution&quot; mode of <code>secure_getenv</code>() is controlled by the <code>AT_SECURE</code> flag contained in the auxiliary vector passed from the kernel to user space.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-clearenv/">clearenv</a></code>(3), <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
