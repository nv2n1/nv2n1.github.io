---
title: "pidfd_send_signal(2)"
name: "pidfd_send_signal"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pidfd_send_signal/"
description: "pidfd_send_signal – send a signal to a process specified by a file descriptor"
---

<h2 class="name">NAME</h2>
<p> pidfd_send_signal &#8211; send a signal to a process specified by a file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;signal.h&gt;
int pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                      unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pidfd_send_signal</code>() system call sends the signal <i>sig</i> to the target process referred to by <i>pidfd</i>, a PID file descriptor that refers to a process. </p>
<p> If the <i>info</i> argument points to a <i>siginfo_t</i> buffer, that buffer should be populated as described in <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2). </p>
<p> If the <i>info</i> argument is a NULL pointer, this is equivalent to specifying a pointer to a <i>siginfo_t</i> buffer whose fields match the values that are implicitly supplied when a signal is sent using <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2): </p>
<dl>
<dt>*</p>
<dd> <i>si_signo</i> is set to the signal number;</p>
<dt>*</p>
<dd> <i>si_errno</i> is set to 0;</p>
<dt>*</p>
<dd> <i>si_code</i> is set to <code>SI_USER</code>;</p>
<dt>*</p>
<dd> <i>si_pid</i> is set to the caller&#8217;s PID; and</p>
<dt>*</p>
<dd> <i>si_uid</i> is set to the caller&#8217;s real user ID.</dl>
<p> The calling process must either be in the same PID namespace as the process referred to by <i>pidfd</i>, or be in an ancestor of that namespace. </p>
<p> The <i>flags</i> argument is reserved for future use; currently, this argument must be specified as 0.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>pidfd_send_signal</code>() returns 0. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>pidfd</i> is not a valid PID file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> <i>sig</i> is not a valid signal.</p>
<dt><code>EINVAL</code></p>
<dd> The calling process is not in a PID namespace from which it can send a signal to the target process.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is not 0.</p>
<dt><code>EPERM</code></p>
<dd> The calling process does not have permission to send the signal to the target process.</p>
<dt><code>EPERM</code></p>
<dd> <i>pidfd</i> doesn&#8217;t refer to the calling process, and <i>info.si_code</i> is invalid (see <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2)).</p>
<dt><code>ESRCH</code></p>
<dd> The target process does not exist (i.e., it has terminated and been waited on).</dl>
<h2>VERSIONS</h2>
<p> <code>pidfd_send_signal</code>() first appeared in Linux 5.1.</p>
<h2>CONFORMING TO</h2>
<p> <code>pidfd_send_signal</code>() is Linux specific.</p>
<h2>NOTES</h2>
<p> Currently, there is no glibc wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h3>PID file descriptors</h3>
<p> The <i>pidfd</i> argument is a PID file descriptor, a file descriptor that refers to process. Such a file descriptor can be obtained in any of the following ways:</p>
<dl>
<dt>*</p>
<dd> by opening a <i>/proc/[pid]</i> directory;</p>
<dt>*</p>
<dd> using <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2); or</p>
<dt>*</p>
<dd> via the PID file descriptor that is returned by a call to <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) or <code><a href="/docs/linux/man/2-clone3/">clone3</a></code>(2) that specifies the <code>CLONE_PIDFD</code> flag.</dl>
<p> The <code>pidfd_send_signal</code>() system call allows the avoidance of race conditions that occur when using traditional interfaces (such as <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2)) to signal a process. The problem is that the traditional interfaces specify the target process via a process ID (PID), with the result that the sender may accidentally send a signal to the wrong process if the originally intended target process has terminated and its PID has been recycled for another process. By contrast, a PID file descriptor is a stable reference to a specific process; if that process terminates, <code>pidfd_send_signal</code>() fails with the error <code>ESRCH</code>.</p>
<h2>EXAMPLES</h2>
<p> #define _GNU_SOURCE #include &lt;limits.h&gt; #include &lt;signal.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdio.h&gt; #include &lt;string.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;sys/syscall.h&gt; </p>
<p> #ifndef __NR_pidfd_send_signal #define __NR_pidfd_send_signal 424 #endif </p>
<p> static int pidfd_send_signal(int pidfd, int sig, siginfo_t *info,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int flags) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;siginfo_t info;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char path[PATH_MAX];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int pidfd, sig; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;pid&gt;&nbsp;&lt;signal&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sig&nbsp;=&nbsp;atoi(argv[2]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Obtain a PID file descriptor by opening the&nbsp;/proc/PID directory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;of the target process&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(path, sizeof(path),&nbsp;&quot;/proc/%s&quot;, argv[1]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pidfd&nbsp;=&nbsp;open(path, O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pidfd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Populate a&nbsp;&#8216;siginfo_t&#8217;&nbsp;structure for use with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pidfd_send_signal()&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;info, 0, sizeof(info));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info.si_code&nbsp;=&nbsp;SI_QUEUE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info.si_signo&nbsp;=&nbsp;sig;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info.si_errno&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info.si_uid&nbsp;=&nbsp;getuid();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info.si_pid&nbsp;=&nbsp;getpid();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;info.si_value.sival_int&nbsp;=&nbsp;1234; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Send the signal&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pidfd_send_signal(pidfd, sig,&nbsp;&amp;info, 0)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;pidfd_send_signal&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2), <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/7-pid_namespaces/">pid_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
