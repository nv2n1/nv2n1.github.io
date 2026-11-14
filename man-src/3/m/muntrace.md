---
title: "muntrace(3)"
name: "muntrace"
section: "3"
letter: "m"
url: "/docs/linux/man/3-muntrace/"
description: "mtrace, muntrace – malloc tracing"
---

<p>mtrace, muntrace &#8211; malloc tracing </p>
<h2>Synopsis</h2>
<p><code>#include &lt;mcheck.h&gt;</code> </p>
<p> <code>void mtrace(void);</code> </p>
<p> <code>void muntrace(void);</code></p>
<h2>Description</h2>
<p>The <code>mtrace</code>() function installs hook functions for the memory-allocation functions (<code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) <code><a href="/docs/linux/man/3-memalign/">memalign</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3)). These hook functions record tracing information about memory allocation and deallocation. The tracing information can be used to discover memory leaks and attempts to free nonallocated memory in a program. </p>
<p> The <code>muntrace</code>() function disables the hook functions installed by <code>mtrace</code>(), so that tracing information is no longer recorded for the memory-allocation functions. If no hook functions were successfully installed by <code>mtrace</code>(), <code>muntrace</code>() does nothing. </p>
<p> When <code>mtrace</code>() is called, it checks the value of the environment variable <code>MALLOC_TRACE</code>, which should contain the pathname of a file in which the tracing information is to be recorded. If the pathname is successfully opened, it is truncated to zero length. </p>
<p> If <code>MALLOC_TRACE</code> is not set, or the pathname it specifies is invalid or not writable, then no hook functions are installed, and <code>mtrace</code>() has no effect. In set-user-ID and set-group-ID programs, <code>MALLOC_TRACE</code> is ignored, and <code>mtrace</code>() has no effect.</p>
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
<td> <code>mtrace</code>(), <code>muntrace</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are GNU extensions.</p>
<h2>Notes</h2>
<p>In normal usage, <code>mtrace</code>() is called once at the start of execution of a program, and <code>muntrace</code>() is never called. </p>
<p> The tracing output produced after a call to <code>mtrace</code>() is textual, but not designed to be human readable. The GNU C library provides a Perl script, <code><a href="/docs/linux/man/1-mtrace/">mtrace</a></code>(1), that interprets the trace log and produces human-readable output. For best results, the traced program should be compiled with debugging enabled, so that line-number information is recorded in the executable. </p>
<p> The tracing performed by <code>mtrace</code>() incurs a performance penalty (if <code>MALLOC_TRACE</code> points to a valid, writable pathname).</p>
<h2>Bugs</h2>
<p>The line-number information produced by <code><a href="/docs/linux/man/1-mtrace/">mtrace</a></code>(1) is not always precise: the line number references may refer to the previous or following (nonblank) line of the source code.</p>
<h2>Examples</h2>
<p>The shell session below demonstrates the use of the <code>mtrace</code>() function and the <code><a href="/docs/linux/man/1-mtrace/">mtrace</a></code>(1) command in a program that has memory leaks at two different locations. The demonstration uses the following program: </p>
<p> $ <code>cat t_mtrace.c</code> #include &lt;mcheck.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mtrace(); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;2;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;malloc(100);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Never freed&#8211;a memory leak&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calloc(16, 16);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Never freed&#8211;a memory leak&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p> When we run the program as follows, we see that <code>mtrace</code>() diagnosed memory leaks at two different locations in the program: </p>
<p> $ <code>cc -g t_mtrace.c -o t_mtrace</code> $ <code>export MALLOC_TRACE=/tmp/t</code> $ <code>./t_mtrace</code> $ <code>mtrace ./t_mtrace $MALLOC_TRACE</code> Memory not freed: &#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Address&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Caller 0x084c9378 0x64 at /home/cecilia/t_mtrace.c:12 0x084c93e0 0x64 at /home/cecilia/t_mtrace.c:12 0x084c9448 0x100 at /home/cecilia/t_mtrace.c:16 </p>
<p> The first two messages about unfreed memory correspond to the two <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) calls inside the <i>for</i> loop. The final message corresponds to the call to <code><a href="/docs/linux/man/3-calloc/">calloc</a></code>(3) (which in turn calls <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mtrace/">mtrace</a></code>(1), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-malloc_hook/">malloc_hook</a></code>(3), <code><a href="/docs/linux/man/3-mcheck/">mcheck</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
