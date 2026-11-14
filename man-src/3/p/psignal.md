---
title: "psignal(3)"
name: "psignal"
section: "3"
letter: "p"
url: "/docs/linux/man/3-psignal/"
description: "psignal, psiginfo – print signal description"
---

<p>psignal, psiginfo &#8211; print signal description</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

void psignal(int sig, const char *s);
void psiginfo(const siginfo_t *pinfo, const char *s);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>psignal</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE<br />
 <code>psiginfo</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<h2>Description</h2>
<p>The <code>psignal</code>() function displays a message on <i>stderr</i> consisting of the string <i>s</i>, a colon, a space, a string describing the signal number <i>sig</i>, and a trailing newline. If the string <i>s</i> is NULL or empty, the colon and space are omitted. If <i>sig</i> is invalid, the message displayed will indicate an unknown signal. </p>
<p> The <code>psiginfo</code>() function is like <code>psignal</code>(), except that it displays information about the signal described by <i>pinfo</i>, which should point to a valid <i>siginfo_t</i> structure. As well as the signal description, <code>psiginfo</code>() displays information about the origin of the signal, and other information relevant to the signal (e.g., the relevant memory address for hardware-generated signals, the child process ID for <code>SIGCHLD</code>, and the user ID and process ID of the sender, for signals set using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) or <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3)).</p>
<h2>Return Value</h2>
<p>The <code>psignal</code>() and <code>psiginfo</code>() functions return no value.</p>
<h2>Versions</h2>
<p>The <code>psiginfo</code>() function was added to glibc in version 2.10.</p>
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
<td> <code>psignal</code>(), <code>psiginfo</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2008, 4.3BSD.</p>
<h2>Bugs</h2>
<p>In glibc versions up to 2.12, <code>psiginfo</code>() had the following bugs:</p>
<dl>
<dt>*</p>
<dd>In some circumstances, a trailing newline is not printed.</p>
<dt>*</p>
<dd>Additional details are not displayed for real-time signals.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-strsignal/">strsignal</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
