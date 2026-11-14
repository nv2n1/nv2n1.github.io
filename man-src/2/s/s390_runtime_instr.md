---
title: "s390_runtime_instr(2)"
name: "s390_runtime_instr"
section: "2"
letter: "s"
url: "/docs/linux/man/2-s390_runtime_instr/"
description: "s390_runtime_instr – enable/disable s390 CPU run-time instrumentation"
---

<h2 class="name">NAME</h2>
<p> s390_runtime_instr &#8211; enable/disable s390 CPU run-time instrumentation </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/runtime_instr.h&gt;
int s390_runtime_instr(int command, int signum);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>s390_runtime_instr</code>() system call starts or stops CPU run-time instrumentation for the calling thread. </p>
<p> The <i>command</i> argument controls whether run-time instrumentation is started (<code>S390_RUNTIME_INSTR_START</code>, 1) or stopped (<code>S390_RUNTIME_INSTR_STOP</code>, 2) for the calling thread. </p>
<p> The <i>signum</i> argument specifies the number of a real-time signal. This argument was used to specify a signal number that should be delivered to the thread if the run-time instrumentation buffer was full or if the run-time-instrumentation-halted interrupt had occurred. This feature was never used, and in Linux 4.4 support for this feature was removed; thus, in current kernels, this argument is ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>s390_runtime_instr</code>() returns 0 and enables the thread for run-time instrumentation by assigning the thread a default run-time instrumentation control block. The caller can then read and modify the control block and start the run-time instrumentation. On error, -1 is returned and <i>errno</i> is set to one of the error codes listed below.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The value specified in <i>command</i> is not a valid command.</p>
<dt><code>EINVAL</code></p>
<dd> The value specified in <i>signum</i> is not a real-time signal number. From Linux 4.4 onwards, the <i>signum</i> argument has no effect, so that an invalid signal number will not result in an error.</p>
<dt><code>ENOMEM</code></p>
<dd> Allocating memory for the run-time instrumentation control block failed.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The run-time instrumentation facility is not available.</dl>
<h2>VERSIONS</h2>
<p> This system call is available since Linux 3.7.</p>
<h2>CONFORMING TO</h2>
<p> This Linux-specific system call is available only on the s390 architecture. The run-time instrumentation facility is available beginning with System z EC12.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) to call it. </p>
<p> The <i>asm/runtime_instr.h</i> header file is available since Linux 4.16. </p>
<p> Starting with Linux 4.4, support for signalling was removed, as was the check whether <i>signum</i> is a valid real-time signal. For backwards compatibility with older kernels, it is recommended to pass a valid real-time signal number in <i>signum</i> and install a handler for that signal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
