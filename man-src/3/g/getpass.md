---
title: "getpass(3)"
name: "getpass"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpass/"
description: "getpass – get a password"
---

<h2 class="name">NAME</h2>
<p> getpass &#8211; get a password </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>char *getpass(const char *</code><i>prompt</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getpass</code>():</p>
<dl>
<dl>
<dt>Since glibc 2.2.2:</dt>
<dd>
<pre><code>
_XOPEN_SOURCE &amp;&amp; !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L) || /* Glibc since 2.19: */ _DEFAULT_SOURCE || /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE
</code></pre>
</dd><dt>Before glibc 2.2.2:</dt>
<dd> none</dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> This function is obsolete. Do not use it. If you want to read input without terminal echoing enabled, see the description of the <i>ECHO</i> flag in <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3). </p>
<p> The <code>getpass</code>() function opens <i>/dev/tty</i> (the controlling terminal of the process), outputs the string <i>prompt</i>, turns off echoing, reads one line (the &quot;password&quot;), restores the terminal state and closes <i>/dev/tty</i> again.</p>
<h2>RETURN VALUE</h2>
<p> The function <code>getpass</code>() returns a pointer to a static buffer containing (the first <code>PASS_MAX</code> bytes of) the password without the trailing newline, terminated by a null byte (&#8216;\0&#8217;). This buffer may be overwritten by a following call. On error, the terminal state is restored, <i>errno</i> is set appropriately, and NULL is returned.  </p>
<h2>ERRORS</h2>
<p> The function may fail if </p>
<dl>
<dt><code>ENXIO</code></dt>
<dd> <p> The process does not have a controlling terminal. </p>
 </dd></dl>
<h2>FILES</h2>
<p> <i>/dev/tty</i>  </p>
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
<td> <code>getpass</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe term
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Present in SUSv2, but marked LEGACY. Removed in POSIX.1-2001.  </p>
<h2>NOTES</h2>
<p> In the GNU C library implementation, if <i>/dev/tty</i> cannot be opened, the prompt is written to <i>stderr</i> and the password is read from <i>stdin</i>. There is no limit on the length of the password. Line editing is not disabled. </p>
<p> According to SUSv2, the value of <code>PASS_MAX</code> must be defined in <i>&lt;limits.h&gt;</i> in case it is smaller than 8, and can in any case be obtained using <i>sysconf(_SC_PASS_MAX)</i>. However, POSIX.2 withdraws the constants <code>PASS_MAX</code> and <code>_SC_PASS_MAX</code>, and the function <code>getpass</code>(). The glibc version accepts <code>_SC_PASS_MAX</code> and returns <code>BUFSIZ</code> (e.g., 8192).  </p>
<h2>BUGS</h2>
<p> The calling process should zero the password as soon as possible to avoid leaving the cleartext password visible in the process&#8217;s address space.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
