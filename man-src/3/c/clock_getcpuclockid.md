---
title: "clock_getcpuclockid(3)"
name: "clock_getcpuclockid"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clock_getcpuclockid/"
description: "clock_getcpuclockid – obtain ID of a process CPU-time clock"
---

<h2 class="name">NAME</h2>
<p> clock_getcpuclockid &#8211; obtain ID of a process CPU-time clock </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<pre><code>
int clock_getcpuclockid(pid_t pid, clockid_t *clockid);
</code></pre>
<p> Link with <i>-lrt</i> (only for glibc versions before 2.17). </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>clock_getcpuclockid</code>():</p>
<dl>
<dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> The <code>clock_getcpuclockid</code>() function obtains the ID of the CPU-time clock of the process whose ID is <i>pid</i>, and returns it in the location pointed to by <i>clockid</i>. If <i>pid</i> is zero, then the clock ID of the CPU-time clock of the calling process is returned.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>clock_getcpuclockid</code>() returns 0; on error, it returns one of the positive error numbers listed in ERRORS.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOSYS</code></p>
<dd> The kernel does not support obtaining the per-process CPU-time clock of another process, and <i>pid</i> does not specify the calling process.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have permission to access the CPU-time clock of the process specified by <i>pid</i>. (Specified in POSIX.1-2001; does not occur on Linux unless the kernel does not support obtaining the per-process CPU-time clock of another process.)</p>
<dt><code>ESRCH</code></p>
<dd> There is no process with the ID <i>pid</i>.</dl>
<h2>VERSIONS</h2>
<p> The <code>clock_getcpuclockid</code>() function is available in glibc since version 2.2.</p>
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
<td> <code>clock_getcpuclockid</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> Calling <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) with the clock ID obtained by a call to <code>clock_getcpuclockid</code>() with a <i>pid</i> of 0, is the same as using the clock ID <code>CLOCK_PROCESS_CPUTIME_ID</code>.</p>
<h2>EXAMPLES</h2>
<p> The example program below obtains the CPU-time clock ID of the process whose ID is given on the command line, and then uses <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) to obtain the time on that clock. An example run is the following: </p>
<p> $<code> ./a.out 1</code> # Show CPU clock of init process CPU-time clock for PID 1 is 2.213466748 seconds</p>
<h3>Program source</h3>
<p> #define _XOPEN_SOURCE 600 #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;time.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clockid_t clockid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec ts; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s&nbsp;&lt;process-ID&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_getcpuclockid(atoi(argv[1]),&nbsp;&amp;clockid)&nbsp;!=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;clock_getcpuclockid&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(clock_gettime(clockid,&nbsp;&amp;ts)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;clock_gettime&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;CPU-time clock for PID&nbsp;%s is&nbsp;%jd.%09ld seconds
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[1],&nbsp;(intmax_t)&nbsp;ts.tv_sec, ts.tv_nsec);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/3-pthread_getcpuclockid/">pthread_getcpuclockid</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
