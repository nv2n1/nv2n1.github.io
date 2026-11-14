---
title: "error_at_line(3)"
name: "error_at_line"
section: "3"
letter: "e"
url: "/docs/linux/man/3-error_at_line/"
description: "error, error_at_line, error_message_count, error_one_per_line, error_print_progname – glibc error reporting functions"
---

<h2 class="name">NAME</h2>
<p> error, error_at_line, error_message_count, error_one_per_line, error_print_progname &#8211; glibc error reporting functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;error.h&gt;
void error(int status, int errnum, const char *format, ...);
void error_at_line(int status, int errnum, const char *filename,
                   unsigned int linenum, const char *format, ...);
extern unsigned int error_message_count;
extern int error_one_per_line;
extern void (*error_print_progname)(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>error</code>() is a general error-reporting function. It flushes <i>stdout</i>, and then outputs to <i>stderr</i> the program name, a colon and a space, the message specified by the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)-style format string <i>format</i>, and, if <i>errnum</i> is nonzero, a second colon and a space followed by the string given by <i>strerror(errnum)</i>. Any arguments required for <i>format</i> should follow <i>format</i> in the argument list. The output is terminated by a newline character. </p>
<p> The program name printed by <code>error</code>() is the value of the global variable <code><a href="/docs/linux/man/3-program_invocation_name/">program_invocation_name</a></code>(3). <i>program_invocation_name</i> initially has the same value as <i>main</i>()&#8217;s <i>argv[0]</i>. The value of this variable can be modified to change the output of <code>error</code>(). </p>
<p> If <i>status</i> has a nonzero value, then <code>error</code>() calls <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) to terminate the program using the given value as the exit status. </p>
<p> The <code>error_at_line</code>() function is exactly the same as <code>error</code>(), except for the addition of the arguments <i>filename</i> and <i>linenum</i>. The output produced is as for <code>error</code>(), except that after the program name are written: a colon, the value of <i>filename</i>, a colon, and the value of <i>linenum</i>. The preprocessor values <code>__LINE__</code> and <code>__FILE__</code> may be useful when calling <code>error_at_line</code>(), but other values can also be used. For example, these arguments could refer to a location in an input file. </p>
<p> If the global variable <i>error_one_per_line</i> is set nonzero, a sequence of <code>error_at_line</code>() calls with the same value of <i>filename</i> and <i>linenum</i> will result in only one message (the first) being output. </p>
<p> The global variable <i>error_message_count</i> counts the number of messages that have been output by <code>error</code>() and <code>error_at_line</code>(). </p>
<p> If the global variable <i>error_print_progname</i> is assigned the address of a function (i.e., is not NULL), then that function is called instead of prefixing the message with the program name and colon. The function should print a suitable string to <i>stderr</i>.</p>
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
<td> <code>error</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>error_at_line</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race: error_at_line/error_one_per_line locale
</td>
</tr>
</table>
<p> The internal <i>error_one_per_line</i> variable is accessed (without any form of synchronization, but since it&#8217;s an <i>int</i> used once, it should be safe enough) and, if <i>error_one_per_line</i> is set nonzero, the internal static variables (not exposed to users) used to hold the last printed filename and line number are accessed and modified without synchronization; the update is not atomic and it occurs before disabling cancellation, so it can be interrupted only after one of the two variables is modified. After that, <code>error_at_line</code>() is very much like <code>error</code>().</p>
<h2>CONFORMING TO</h2>
<p> These functions and variables are GNU extensions, and should not be used in programs intended to be portable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-err/">err</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-program_invocation_name/">program_invocation_name</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
