---
title: "strerrordesc_np(3)"
name: "strerrordesc_np"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strerrordesc_np/"
description: "strerror, strerrorname_np, strerrordesc_np, strerror_r, strerror_l – return string describing error number"
---

<p>strerror, strerrorname_np, strerrordesc_np, strerror_r, strerror_l &#8211; return string describing error number</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *strerror(int errnum);
const char *strerrorname_np(int errnum);
const char *strerrordesc_np(int errnum);
int strerror_r(int errnum, char *buf, size_t buflen);
/* XSI-compliant */
char *strerror_r(int errnum, char *buf, size_t buflen);
/* GNU-specific */
char *strerror_l(int errnum, locale_t locale);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strerrorname_np</code>(), <code>strerrordesc_np</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_GNU_SOURCE <code>strerror_r</code>():</p>
<dl>
<dd>The XSI-compliant version is provided if:<br />
 (_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L) &amp;&amp; ! &nbsp;_GNU_SOURCE<br />
 Otherwise, the GNU-specific version is provided.</dd></dl>
<h2>Description</h2>
<p>The <code>strerror</code>() function returns a pointer to a string that describes the error code passed in the argument <i>errnum</i>, possibly using the <code>LC_MESSAGES</code> part of the current locale to select the appropriate language. (For example, if <i>errnum</i> is <code>EINVAL</code>, the returned description will be &quot;Invalid argument&quot;.) This string must not be modified by the application, but may be modified by a subsequent call to <code>strerror</code>() or <code>strerror_l</code>(). No other library function, including <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), will modify this string. </p>
<p> Like <code>strerror</code>(), the <code>strerrordesc_np</code>() function returns a pointer to a string that describes the error code passed in the argument <i>errnum</i>, with the difference that the returned string is not translated according to the current locale. </p>
<p> The <code>strerrorname_np</code>() function returns a pointer to a string containing the name of the error code passed in the argument <i>errnum</i>. For example, given <code>EPERM</code> as an argument, this function returns a pointer to the string &quot;EPERM&quot;.</p>
<h3>strerror_r()</h3>
<p>The <code>strerror_r</code>() function is similar to <code>strerror</code>(), but is thread safe. This function is available in two versions: an XSI-compliant version specified in POSIX.1-2001 (available since glibc 2.3.4, but not POSIX-compliant until glibc 2.13), and a GNU-specific version (available since glibc 2.0). The XSI-compliant version is provided with the feature test macros settings shown in the SYNOPSIS; otherwise the GNU-specific version is provided. If no feature test macros are explicitly defined, then (since glibc 2.4) <code>_POSIX_C_SOURCE</code> is defined by default with the value 200112L, so that the XSI-compliant version of <code>strerror_r</code>() is provided by default. </p>
<p> The XSI-compliant <code>strerror_r</code>() is preferred for portable applications. It returns the error string in the user-supplied buffer <i>buf</i> of length <i>buflen</i>. </p>
<p> The GNU-specific <code>strerror_r</code>() returns a pointer to a string containing the error message. This may be either a pointer to a string that the function stores in <i>buf</i>, or a pointer to some (immutable) static string (in which case <i>buf</i> is unused). If the function stores a string in <i>buf</i>, then at most <i>buflen</i> bytes are stored (the string may be truncated if <i>buflen</i> is too small and <i>errnum</i> is unknown). The string always includes a terminating null byte (&#8216;\0&#8217;).  </p>
<h3>strerror_l()</h3>
<p> <code>strerror_l</code>() is like <code>strerror</code>(), but maps <i>errnum</i> to a locale-dependent error message in the locale specified by <i>locale</i>. The behavior of <code>strerror_l</code>() is undefined if <i>locale</i> is the special locale object <code>LC_GLOBAL_LOCALE</code> or is not a valid locale object handle.  </p>
<h2>RETURN VALUE</h2>
<p> The <code>strerror</code>(), <code>strerror_l</code>(), and the GNU-specific <code>strerror_r</code>() functions return the appropriate error description string, or an &quot;Unknown error nnn&quot; message if the error number is unknown. </p>
<p> On success, <code>strerrorname_np</code>() and <code>strerrordesc_np</code>() return the appropriate error description string. If <i>errnum</i> is an invalid error number, these functions return NULL. </p>
<p> The XSI-compliant <code>strerror_r</code>() function returns 0 on success. On error, a (positive) error number is returned (since glibc 2.13), or -1 is returned and <i>errno</i> is set to indicate the error (glibc versions before 2.13). </p>
<p> POSIX.1-2001 and POSIX.1-2008 require that a successful call to <code>strerror</code>() or <code>strerror_l</code>() shall leave <i>errno</i> unchanged, and note that, since no function return value is reserved to indicate an error, an application that wishes to check for errors should initialize <i>errno</i> to zero before the call, and then check <i>errno</i> after the call.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></dt>
<dd> <p> The value of <i>errnum</i> is not a valid error number. </p>
 </dd>
<dt><code>ERANGE</code></dt>
<dd> <p> Insufficient storage was supplied to contain the error description string. </p>
 </dd></dl>
<h2>VERSIONS</h2>
<p> The <code>strerror_l</code>() function first appeared in glibc 2.6.  </p>
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
<td> <code>strerror</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:strerror
</td>
</tr>
<tr VALIGN=top>
<td> <code>strerrorname_np</code>(), <code>strerrordesc_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>strerror_r</code>(),  <code>strerror_l</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>strerror</code>() is specified by POSIX.1-2001, POSIX.1-2008, C89, and C99. <code>strerror_r</code>() is specified by POSIX.1-2001 and POSIX.1-2008. </p>
<p> <code>strerror_l</code>() is specified in POSIX.1-2008. </p>
<p> The GNU-specific functions <code>strerror_r</code>(), <code>strerrorname_np</code>(), and <code>strerrordesc_np</code>() are nonstandard extensions. </p>
<p> POSIX.1-2001 permits <code>strerror</code>() to set <i>errno</i> if the call encounters an error, but does not specify what value should be returned as the function result in the event of an error. On some systems, <code>strerror</code>() returns NULL if the error number is unknown. On other systems, <code>strerror</code>() returns a string something like &quot;Error nnn occurred&quot; and sets <i>errno</i> to <code>EINVAL</code> if the error number is unknown. C99 and POSIX.1-2008 require the return value to be non-NULL.  </p>
<h2>NOTES</h2>
<p> The GNU C Library uses a buffer of 1024 characters for <code>strerror</code>(). This buffer size therefore should be sufficient to avoid an <code>ERANGE</code> error when calling <code>strerror_r</code>(). </p>
<p> <code>strerrorname_np</code>() and <code>strerrordesc_np</code>() are thread-safe and async-signal-safe.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-err/">err</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-error/">error</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-strsignal/">strsignal</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
