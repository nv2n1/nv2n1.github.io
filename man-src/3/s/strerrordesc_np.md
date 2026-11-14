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
 Otherwise, the GNU-specific version is provided.</dl>
<h2>Description</h2>
<p>The <code>strerror</code>() function returns a pointer to a string that describes the error code passed in the argument <i>errnum</i>, possibly using the <code>LC_MESSAGES</code> part of the current locale to select the appropriate language. (For example, if <i>errnum</i> is <code>EINVAL</code>, the returned description will be &quot;Invalid argument&quot;.) This string must not be modified by the application, but may be modified by a subsequent call to <code>strerror</code>() or <code>strerror_l</code>(). No other library function, including <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), will modify this string. </p>
<p> Like <code>strerror</code>(), the <code>strerrordesc_np</code>() function returns a pointer to a string that describes the error code passed in the argument <i>errnum</i>, with the difference that the returned string is not translated according to the current locale. </p>
<p> The <code>strerrorname_np</code>() function returns a pointer to a string containing the name of the error code passed in the argument <i>errnum</i>. For example, given <code>EPERM</code> as an argument, this function returns a pointer to the string &quot;EPERM&quot;.</p>
<h3>strerror_r()</h3>
<p>The <code>strerror_r</code>() function is similar to <code>strerror</code>(), but is thread safe. This function is available in two versions: an XSI-compliant version specified in POSIX.1-2001 (available since glibc 2.3.4, but not POSIX-compliant until glibc 2.13), and a GNU-specific version (available since glibc 2.0). The XSI-compliant version is provided with the feature test macros settings shown in the SYNOPSIS; otherwise the GNU-specific version is provided. If no feature test macros are explicitly defined, then (since glibc 2.4) <code>_POSIX_C_SOURCE</code> is defined by default with the value 200112L, so that the XSI-compliant version of <code>strerror_r</code>() is provided by default. </p>
<p> The XSI-compliant <code>strerror_r</code>() is preferred for portable applications. It returns the error string in the user-supplied buffer <i>buf</i> of length <i>buflen</i>. </p>
<p> The GNU-specific <code>strerror_r</code>() returns a pointer to a string containing the error message. This may be either a pointer to a string that the function stores in <i>buf</i>, or a pointer to some (immutable) static string (in which case <i>buf</i> is unused). If the function stores a string in <i>buf</i>, then at most <i>buflen</i> bytes are stored (the string may be truncated if <i>buflen</i> is too small and <i>errnum</i> is unknown). The string always includes a terminating null byte (&#8216;
