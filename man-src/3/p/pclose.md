---
title: "pclose(3)"
name: "pclose"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pclose/"
description: "popen, pclose – pipe stream to or from a process"
---

<p>popen, pclose &#8211; pipe stream to or from a process</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

FILE *popen(const char *command, const char *type);

int pclose(FILE *stream);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>popen</code>(), <code>pclose</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>The <code>popen</code>() function opens a process by creating a pipe, forking, and invoking the shell. Since a pipe is by definition unidirectional, the <i>type</i> argument may specify only reading or writing, not both; the resulting stream is correspondingly read-only or write-only. </p>
<p> The <i>command</i> argument is a pointer to a null-terminated string containing a shell command line. This command is passed to <i>/bin/sh</i> using the <code>-c</code> flag; interpretation, if any, is performed by the shell. </p>
<p> The <i>type</i> argument is a pointer to a null-terminated string which must contain either the letter &#8216;r&#8217; for reading or the letter &#8216;w&#8217; for writing. Since glibc 2.9, this argument can additionally include the letter &#8216;e&#8217;, which causes the close-on-exec flag (<code>FD_CLOEXEC</code>) to be set on the underlying file descriptor; see the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful. </p>
<p> The return value from <code>popen</code>() is a normal standard I/O stream in all respects save that it must be closed with <code>pclose</code>() rather than <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3). Writing to such a stream writes to the standard input of the command; the command&#8217;s standard output is the same as that of the process that called <code>popen</code>(), unless this is altered by the command itself. Conversely, reading from the stream reads the command&#8217;s standard output, and the command&#8217;s standard input is the same as that of the process that called <code>popen</code>(). </p>
<p> Note that output <code>popen</code>() streams are block buffered by default. </p>
<p> The <code>pclose</code>() function waits for the associated process to terminate and returns the exit status of the command as returned by <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2).</p>
<h2>Return Value</h2>
<p><code>popen</code>(): on success, returns a pointer to an open stream that can be used to read or write to the pipe; if the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) calls fail, or if the function cannot allocate memory, NULL is returned. </p>
<p> <code>pclose</code>(): on success, returns the exit status of the command; if <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2) returns an error, or some other error is detected, -1 is returned. </p>
<p> Both functions set <i>errno</i> to an appropriate value in the case of an error.</p>
<h2>Errors</h2>
<p>The <code>popen</code>() function does not set <i>errno</i> if memory allocation fails. If the underlying <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) or <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) fails, <i>errno</i> is set appropriately. If the <i>type</i> argument is invalid, and this condition is detected, <i>errno</i> is set to <code>EINVAL</code>. </p>
<p> If <code>pclose</code>() cannot obtain the child status, <i>errno</i> is set to <code>ECHILD</code>.</p>
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
<td> <code>popen</code>(), <code>pclose</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008. </p>
<p> The &#8216;e&#8217; value for <i>type</i> is a Linux extension.</p>
<h2>Notes</h2>
<p><code>Note</code>: carefully read Caveats in <code><a href="/docs/linux/man/3-system/">system</a></code>(3).</p>
<h2>Bugs</h2>
<p>Since the standard input of a command opened for reading shares its seek offset with the process that called <code>popen</code>(), if the original process has done a buffered read, the command&#8217;s input position may not be as expected. Similarly, the output from a command opened for writing may become intermingled with that of the original process. The latter can be avoided by calling <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3) before <code>popen</code>(). </p>
<p> Failure to execute the shell is indistinguishable from the shell&#8217;s failure to execute command, or an immediate exit of the command. The only hint is an exit status of 127.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3), <code><a href="/docs/linux/man/3-system/">system</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
