---
title: "pipe(2)"
name: "pipe"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pipe/"
description: "pipe, pipe2 – create pipe"
---

<h2 class="name">NAME</h2>
<p> pipe, pipe2 &#8211; create pipe </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
/* On Alpha, IA-64, MIPS, SuperH, and SPARC/SPARC64; see NOTES */
struct fd_pair {
    long fd[2];
};
struct fd_pair pipe();
/* On all other architectures */
int pipe(int pipefd[2]);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;fcntl.h&gt;  /* Obtain O_* constant definitions */
#include &lt;unistd.h&gt;
int pipe2(int pipefd[2], int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pipe</code>() creates a pipe, a unidirectional data channel that can be used for interprocess communication. The array <i>pipefd</i> is used to return two file descriptors referring to the ends of the pipe. <i>pipefd[0]</i> refers to the read end of the pipe. <i>pipefd[1]</i> refers to the write end of the pipe. Data written to the write end of the pipe is buffered by the kernel until it is read from the read end of the pipe. For further details, see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7). </p>
<p> If <i>flags</i> is 0, then <code>pipe2</code>() is the same as <code>pipe</code>(). The following values can be bitwise ORed in <i>flags</i> to obtain different behavior:</p>
<dl>
<dt><code>O_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the two new file descriptors. See the description of the same flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</p>
<dt><code>O_DIRECT</code> (since Linux 3.4)</p>
<dd> Create a pipe that performs I/O in &quot;packet&quot; mode. Each <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to the pipe is dealt with as a separate packet, and <code><a href="/docs/linux/man/2-read/">read</a></code>(2)s from the pipe will read one packet at a time. Note the following points:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Writes of greater than <code>PIPE_BUF</code> bytes (see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)) will be split into multiple packets. The constant <code>PIPE_BUF</code> is defined in <i>&lt;limits.h&gt;</i>.</p>
<dt>*</p>
<dd> If a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) specifies a buffer size that is smaller than the next packet, then the requested number of bytes are read, and the excess bytes in the packet are discarded. Specifying a buffer size of <code>PIPE_BUF</code> will be sufficient to read the largest possible packets (see the previous point).</p>
<dt>*</p>
<dd> Zero-length packets are not supported. (A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) that specifies a buffer size of zero is a no-op, and returns 0.)</dl>
</dl>
<dt>
<dd> Older kernels that do not support this flag will indicate this via an <code>EINVAL</code> error.</p>
<dt>
<dd> Since Linux 4.5, it is possible to change the <code>O_DIRECT</code> setting of a pipe file descriptor using <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>O_NONBLOCK</code></p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file descriptions referred to by the new file descriptors. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, <i>errno</i> is set appropriately, and <i>pipefd</i> is left unchanged. </p>
<p> On Linux (and other systems), <code>pipe</code>() does not modify <i>pipefd</i> on failure. A requirement standardizing this behavior was added in POSIX.1-2008 TC2. The Linux-specific <code>pipe2</code>() system call likewise does not modify <i>pipefd</i> on failure.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>pipefd</i> is not valid.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>pipe2</code>()) Invalid value in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The user hard limit on memory that can be allocated for pipes has been reached and the caller is not privileged; see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7).</dl>
<h2>VERSIONS</h2>
<p> <code>pipe2</code>() was added to Linux in version 2.6.27; glibc support is available starting with version 2.9.</p>
<h2>CONFORMING TO</h2>
<p> <code>pipe</code>(): POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>pipe2</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> The System V ABI on some architectures allows the use of more than one register for returning multiple values; several architectures (namely, Alpha, IA-64, MIPS, SuperH, and SPARC/SPARC64) (ab)use this feature in order to implement the <code>pipe</code>() system call in a functional manner: the call doesn&#8217;t take any arguments and returns a pair of file descriptors as the return value on success. The glibc <code>pipe</code>() wrapper function transparently deals with this. See <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) for information regarding registers used for storing second file descriptor.</p>
<h2>EXAMPLES</h2>
<p> The following program creates a pipe, and then <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)s to create a child process; the child inherits a duplicate set of file descriptors that refer to the same pipe. After the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), each process closes the file descriptors that it doesn&#8217;t need for the pipe (see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)). The parent then writes the string contained in the program&#8217;s command-line argument to the pipe, and the child reads this string a byte at a time from the pipe and echoes it on standard output.</p>
<h3>Program source</h3>
<p> #include &lt;sys/types.h&gt; #include &lt;sys/wait.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int pipefd[2];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t cpid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;string&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pipe(pipefd)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;pipe&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cpid&nbsp;=&nbsp;fork();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cpid&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fork&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cpid&nbsp;==&nbsp;0)&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Child reads from pipe&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(pipefd[1]);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close unused write end&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(read(pipefd[0],&nbsp;&amp;buf, 1)&nbsp;&gt;&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;write(STDOUT_FILENO,&nbsp;&amp;buf, 1); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;write(STDOUT_FILENO,&nbsp;&quot;
&quot;, 1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(pipefd[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_exit(EXIT_SUCCESS); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Parent writes argv[1]&nbsp;to pipe&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(pipefd[0]);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Close unused read end&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;write(pipefd[1], argv[1], strlen(argv[1]));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(pipefd[1]);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Reader will see EOF&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wait(NULL);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for child&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2), <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2), <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-popen/">popen</a></code>(3), <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAM">COLOPHON</a></p>
<dd></dl>
