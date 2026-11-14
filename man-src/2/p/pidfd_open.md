---
title: "pidfd_open(2)"
name: "pidfd_open"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pidfd_open/"
description: "pidfd_open – obtain a file descriptor that refers to a process"
---

<h2 class="name">NAME</h2>
<p> pidfd_open &#8211; obtain a file descriptor that refers to a process </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
int pidfd_open(pid_t pid, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pidfd_open</code>() system call creates a file descriptor that refers to the process whose PID is specified in <i>pid</i>. The file descriptor is returned as the function result; the close-on-exec flag is set on the file descriptor. </p>
<p> The <i>flags</i> argument is reserved for future use; currently, this argument must be specified as 0.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>pidfd_open</code>() returns a file descriptor (a nonnegative integer). On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is not 0.</p>
<dt><code>EINVAL</code></p>
<dd> <i>pid</i> is not valid.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached (see the description of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd> The anonymous inode filesystem is not available in this kernel.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ESRCH</code></p>
<dd> The process specified by <i>pid</i> does not exist.</dl>
<h2>VERSIONS</h2>
<p> <code>pidfd_open</code>() first appeared in Linux 5.3.</p>
<h2>CONFORMING TO</h2>
<p> <code>pidfd_open</code>() is Linux specific.</p>
<h2>NOTES</h2>
<p> Currently, there is no glibc wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> The following code sequence can be used to obtain a file descriptor for the child of <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2): </p>
<p> pid = fork(); if (pid &gt; 0) { /* If parent */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pidfd&nbsp;=&nbsp;pidfd_open(pid, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; } </p>
<p> Even if the child has already terminated by the time of the <code>pidfd_open</code>() call, its PID will not have been recycled and the returned file descriptor will refer to the resulting zombie process. Note, however, that this is guaranteed only if the following conditions hold true:</p>
<dl>
<dt>&bull;</p>
<dd> the disposition of <code>SIGCHLD</code> has not been explicitly set to <code>SIG_IGN</code> (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2));</p>
<dt>&bull;</p>
<dd> the <code>SA_NOCLDWAIT</code> flag was not specified while establishing a handler for <code>SIGCHLD</code> or while setting the disposition of that signal to <code>SIG_DFL</code> (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)); and</p>
<dt>&bull;</p>
<dd> the zombie process was not reaped elsewhere in the program (e.g., either by an asynchronously executed signal handler or by <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) or similar in another thread).</dl>
<p> If any of these conditions does not hold, then the child process (along with a PID file descriptor that refers to it) should instead be created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_PIDFD</code> flag.</p>
<h3>Use cases for PID file descriptors</h3>
<p> A PID file descriptor returned by <code>pidfd_open</code>() (or by <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with the <code>CLONE_PID</code> flag) can be used for the following purposes:</p>
<dl>
<dt>&bull;</p>
<dd> The <code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2) system call can be used to send a signal to the process referred to by a PID file descriptor.</p>
<dt>&bull;</p>
<dd> A PID file descriptor can be monitored using <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). When the process that it refers to terminates, these interfaces indicate the file descriptor as readable. Note, however, that in the current implementation, nothing can be read from the file descriptor (<code><a href="/docs/linux/man/2-read/">read</a></code>(2) on the file descriptor fails with the error <code>EINVAL</code>).</p>
<dt>&bull;</p>
<dd> If the PID file descriptor refers to a child of the calling process, then it can be waited on using <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2).</p>
<dt>&bull;</p>
<dd> The <code><a href="/docs/linux/man/2-pidfd_getfd/">pidfd_getfd</a></code>(2) system call can be used to obtain a duplicate of a file descriptor of another process referred to by a PID file descriptor.</p>
<dt>&bull;</p>
<dd> A PID file descriptor can be used as the argument of <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2) in order to move into one or more of the same namespaces as the process referred to by the file descriptor.</dl>
<p> The <code>pidfd_open</code>() system call is the preferred way of obtaining a PID file descriptor for an already existing process. The alternative is to obtain a file descriptor by opening a <i>/proc/[pid]</i> directory. However, the latter technique is possible only if the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem is mounted; furthermore, the file descriptor obtained in this way is <i>not</i> pollable and can&#8217;t be waited on with <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2).</p>
<h2>EXAMPLES</h2>
<p> The program below opens a PID file descriptor for the process whose PID is specified as its command-line argument. It then uses <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) to monitor the file descriptor for process exit, as indicated by an <code>EPOLLIN</code> event.</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;sys/types.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;unistd.h&gt; #include &lt;poll.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> #ifndef __NR_pidfd_open #define __NR_pidfd_open 434 /* System call # on most architectures */ #endif </p>
<p> static int pidfd_open(pid_t pid, unsigned int flags) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(__NR_pidfd_open, pid, flags); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct pollfd pollfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int pidfd, ready; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;pid&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pidfd&nbsp;=&nbsp;pidfd_open(atoi(argv[1]), 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pidfd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;pidfd_open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pollfd.fd&nbsp;=&nbsp;pidfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pollfd.events&nbsp;=&nbsp;POLLIN; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ready&nbsp;=&nbsp;poll(&amp;pollfd, 1, -1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ready&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;poll&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Events&nbsp;(%#x): POLLIN is&nbsp;%sset
&quot;, pollfd.revents,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(pollfd.revents&nbsp;&amp;&nbsp;POLLIN)&nbsp;?&nbsp;&quot;&quot;&nbsp;:&nbsp;&quot;not&nbsp;&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(pidfd);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_getfd/">pidfd_getfd</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-setns/">setns</a></code>(2), <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
