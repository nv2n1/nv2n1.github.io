---
title: "sys_siglist(3)"
name: "sys_siglist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sys_siglist/"
description: "strsignal, sigdescr_np, sigdescr_np, sys_siglist – return string describing signal"
---

<p>strsignal, sigdescr_np, sigdescr_np, sys_siglist &#8211; return string describing signal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strsignal(int sig);
char *sigdescr_np(int sig);
char *sigabbrev_np(int sig);

extern const char *const sys_siglist[];</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sigabbrev_np</code>(), <code>sigdescr_np</code>():</p>
<dl>
<dd>
<dl>
<dt>_GNU_SOURCE</p>
<dd></dl>
</dl>
<p> <code>strsignal</code>():</p>
<dl>
<dd>
<dl>
<dt>From glibc 2.10 to 2.31:</p>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd>_GNU_SOURCE</dl>
</dl>
<p> <i>sys_siglist</i>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>The <code>strsignal</code>() function returns a string describing the signal number passed in the argument <i>sig</i>. The string can be used only until the next call to <code>strsignal</code>(). The string returned by <code>strsignal</code>() is localized according to the <code>LC_MESSAGES</code> category in the current locale. </p>
<p> The <code>sigdescr_np</code>() function returns a string describing the signal number passed in the argument <i>sig</i>. Unlike <code>strsignal</code>() this string is not influenced by the current locale. </p>
<p> The <code>sigabbrev_np</code>() function returns the abbreviated name of the signal, <i>sig</i>. For example, given the value <code>SIGINT</code>, it returns the string &quot;INT&quot;. </p>
<p> The (deprecated) array <i>sys_siglist</i> holds the signal description strings indexed by signal number. The <code>strsignal</code>() or the <code>sigdescr_np</code>() function should be used instead of this array; see also VERSIONS.</p>
<h2>Return Value</h2>
<p>The <code>strsignal</code>() function returns the appropriate description string, or an unknown signal message if the signal number is invalid. On some systems (but not on Linux), NULL may instead be returned for an invalid signal number. </p>
<p> The <code>sigdescr_np</code>() and <code>sigdabbrev_np</code>() functions return the appropriate description string. The returned string is statically allocated and valid for the lifetime of the program. These functions return NULL for an invalid signal number.</p>
<h2>Versions</h2>
<p><code>sigdescr_np</code>() and <code>sigdabbrev_np</code>() first appeared in glibc 2.32. </p>
<p> Starting with version 2.32, the <i>sys_siglist</i> symbol is no longer exported by glibc.</p>
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
<td> <code>strsignal</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:strsignal locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>sigdescr_np</code>(), <code>sigabbrev_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>strsignal</code>(): POSIX.1-2008. Present on Solaris and the BSDs. </p>
<p> <code>sigdescr_np</code>() and <code>sigdabbrev_np</code>() are GNU extensions. </p>
<p> <i>sys_siglist</i> is nonstandard, but present on many other systems.</p>
<h2>Notes</h2>
<p><code>sigdescr_np</code>() and <code>sigdabbrev_np</code>() are thread-safe and async-signal-safe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-psignal/">psignal</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
