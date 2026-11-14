---
title: "signalfd(2)"
name: "signalfd"
section: "2"
letter: "s"
url: "/docs/linux/man/2-signalfd/"
description: "signalfd – create a file descriptor for accepting signals"
---

<h2 class="name">NAME</h2>
<p> signalfd &#8211; create a file descriptor for accepting signals </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/signalfd.h&gt;</code> </p>
<p> <code>int signalfd(int </code><i>fd</i><code>, const sigset_t *</code><i>mask</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>signalfd</code>() creates a file descriptor that can be used to accept signals targeted at the caller. This provides an alternative to the use of a signal handler or <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), and has the advantage that the file descriptor may be monitored by <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). </p>
<p> The <i>mask</i> argument specifies the set of signals that the caller wishes to accept via the file descriptor. This argument is a signal set whose contents can be initialized using the macros described in <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3). Normally, the set of signals to be received via the file descriptor should be blocked using <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), to prevent the signals being handled according to their default dispositions. It is not possible to receive <code>SIGKILL</code> or <code>SIGSTOP</code> signals via a signalfd file descriptor; these signals are silently ignored if specified in <i>mask</i>. </p>
<p> If the <i>fd</i> argument is -1, then the call creates a new file descriptor and associates the signal set specified in <i>mask</i> with that file descriptor. If <i>fd</i> is not -1, then it must specify a valid existing signalfd file descriptor, and <i>mask</i> is used to replace the signal set associated with that file descriptor. </p>
<p> Starting with Linux 2.6.27, the following values may be bitwise ORed in <i>flags</i> to change the behavior of <code>signalfd</code>():</p>
<dl>
<dt><code>SFD_NONBLOCK</code></p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the new file descriptor. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</p>
<dt><code>SFD_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<p> In Linux up to version 2.6.26, the <i>flags</i> argument is unused, and must be specified as zero. </p>
<p> <code>signalfd</code>() returns a file descriptor that supports the following operations:</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> If one or more of the signals specified in <i>mask</i> is pending for the process, then the buffer supplied to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is used to return one or more <i>signalfd_siginfo</i> structures (see below) that describe the signals. The <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns information for as many signals as are pending and will fit in the supplied buffer. The buffer must be at least <i>sizeof(struct signalfd_siginfo)</i> bytes. The return value of the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is the total number of bytes read.</p>
<dt>
<dd> As a consequence of the <code><a href="/docs/linux/man/2-read/">read</a></code>(2), the signals are consumed, so that they are no longer pending for the process (i.e., will not be caught by signal handlers, and cannot be accepted using <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2)).</p>
<dt>
<dd> If none of the signals in <i>mask</i> is pending for the process, then the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) either blocks until one of the signals in <i>mask</i> is generated for the process, or fails with the error <code>EAGAIN</code> if the file descriptor has been made nonblocking.</p>
<dt><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2) (and similar)</p>
<dd> The file descriptor is readable (the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) <i>readfds</i> argument; the <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) <code>POLLIN</code> flag) if one or more of the signals in <i>mask</i> is pending for the process.</p>
<dt>
<dd> The signalfd file descriptor also supports the other file-descriptor multiplexing APIs: <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2), and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7).</p>
<dt><code><a href="/docs/linux/man/2-close/">close</a></code>(2)</p>
<dd> When the file descriptor is no longer required it should be closed. When all file descriptors associated with the same signalfd object have been closed, the resources for object are freed by the kernel.</dl>
<h3>The signalfd_siginfo structure</h3>
<p> The format of the <i>signalfd_siginfo</i> structure(s) returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2)s from a signalfd file descriptor is as follows: </p>
<p> struct signalfd_siginfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_signo;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Signal number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;ssi_errno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Error number&nbsp;(unused)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;ssi_code;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Signal code&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_pid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;PID of sender&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_uid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Real UID of sender&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;ssi_fd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;File descriptor&nbsp;(SIGIO)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_tid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Kernel timer ID&nbsp;(POSIX timers)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_band;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Band event&nbsp;(SIGIO)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_overrun;&nbsp;<wbr>&nbsp;/*&nbsp;POSIX timer overrun count&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t ssi_trapno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Trap number that caused signal&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;ssi_status;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Exit status or signal&nbsp;(SIGCHLD)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;ssi_int;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Integer sent by&nbsp;<a href="/docs/linux/man/3-sigqueue/">sigqueue</a>(3)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ssi_ptr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer sent by&nbsp;<a href="/docs/linux/man/3-sigqueue/">sigqueue</a>(3)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ssi_utime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User CPU time consumed&nbsp;(SIGCHLD)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ssi_stime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;System CPU time consumed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(SIGCHLD)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t ssi_addr;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Address that generated signal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(for hardware-generated signals)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t ssi_addr_lsb;&nbsp;/*&nbsp;Least significant bit of address<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(SIGBUS;&nbsp;since Linux 2.6.37)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;pad[<i>X</i>];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pad size to 128 bytes&nbsp;(allow for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;additional fields in the future)&nbsp;*/ }; </p>
<p> Each of the fields in this structure is analogous to the similarly named field in the <i>siginfo_t</i> structure. The <i>siginfo_t</i> structure is described in <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2). Not all fields in the returned <i>signalfd_siginfo</i> structure will be valid for a specific signal; the set of valid fields can be determined from the value returned in the <i>ssi_code</i> field. This field is the analog of the <i>siginfo_t</i> <i>si_code</i> field; see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) for details.</p>
<h3><a href="/docs/linux/man/2-fork/">fork</a>(2) semantics</h3>
<p> After a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the child inherits a copy of the signalfd file descriptor. A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the file descriptor in the child will return information about signals queued to the child.</p>
<h3>Semantics of file descriptor passing</h3>
<p> As with other file descriptors, signalfd file descriptors can be passed to another process via a UNIX domain socket (see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)). In the receiving process, a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the received file descriptor will return information about signals queued to that process.</p>
<h3><a href="/docs/linux/man/2-execve/">execve</a>(2) semantics</h3>
<p> Just like any other file descriptor, a signalfd file descriptor remains open across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), unless it has been marked for close-on-exec (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)). Any signals that were available for reading before the <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) remain available to the newly loaded program. (This is analogous to traditional signal semantics, where a blocked signal that is pending remains pending across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).)</p>
<h3>Thread semantics</h3>
<p> The semantics of signalfd file descriptors in a multithreaded program mirror the standard semantics for signals. In other words, when a thread reads from a signalfd file descriptor, it will read the signals that are directed to the thread itself and the signals that are directed to the process (i.e., the entire thread group). (A thread will not be able to read signals that are directed to other threads in the process.)</p>
<h3><a href="/docs/linux/man/7-epoll/">epoll</a>(7) semantics</h3>
<p> If a process adds (via <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2)) a signalfd file descriptor to an <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instance, then <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) returns events only for signals sent to that process. In particular, if the process then uses <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) to create a child process, then the child will be able to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) signals that are sent to it using the signalfd file descriptor, but <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) will <code>not</code> indicate that the signalfd file descriptor is ready. In this scenario, a possible workaround is that after the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the child process can close the signalfd file descriptor that it inherited from the parent process and then create another signalfd file descriptor and add it to the epoll instance. Alternatively, the parent and the child could delay creating their (separate) signalfd file descriptors and adding them to the epoll instance until after the call to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>signalfd</code>() returns a signalfd file descriptor; this is either a new file descriptor (if <i>fd</i> was -1), or <i>fd</i> if <i>fd</i> was a valid signalfd file descriptor. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> The <i>fd</i> file descriptor is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is not a valid signalfd file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> <i>flags</i> is invalid; or, in Linux 2.6.26 or earlier, <i>flags</i> is nonzero.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd> Could not mount (internal) anonymous inode device.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient memory to create a new signalfd file descriptor.</dl>
<h2>VERSIONS</h2>
<p> <code>signalfd</code>() is available on Linux since kernel 2.6.22. Working support is provided in glibc since version 2.8. The <code>signalfd4</code>() system call (see NOTES) is available on Linux since kernel 2.6.27.</p>
<h2>CONFORMING TO</h2>
<p> <code>signalfd</code>() and <code>signalfd4</code>() are Linux-specific.</p>
<h2>NOTES</h2>
<p> A process can create multiple signalfd file descriptors. This makes it possible to accept different signals on different file descriptors. (This may be useful if monitoring the file descriptors using <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7): the arrival of different signals will make different file descriptors ready.) If a signal appears in the <i>mask</i> of more than one of the file descriptors, then occurrences of that signal can be read (once) from any one of the file descriptors. </p>
<p> Attempts to include <code>SIGKILL</code> and <code>SIGSTOP</code> in <i>mask</i> are silently ignored. </p>
<p> The signal mask employed by a signalfd file descriptor can be viewed via the entry for the corresponding file descriptor in the process&#8217;s <i>/proc/[pid]/fdinfo</i> directory. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further details.</p>
<h3>Limitations</h3>
<p> The signalfd mechanism can&#8217;t be used to receive signals that are synchronously generated, such as the <code>SIGSEGV</code> signal that results from accessing an invalid memory address or the <code>SIGFPE</code> signal that results from an arithmetic error. Such signals can be caught only via signal handler. </p>
<p> As described above, in normal usage one blocks the signals that will be accepted via <code>signalfd</code>(). If spawning a child process to execute a helper program (that does not need the signalfd file descriptor), then, after the call to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), you will normally want to unblock those signals before calling <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so that the helper program can see any signals that it expects to see. Be aware, however, that this won&#8217;t be possible in the case of a helper program spawned behind the scenes by any library function that the program may call. In such cases, one must fall back to using a traditional signal handler that writes to a file descriptor monitored by <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7).</p>
<h3>C library/kernel differences</h3>
<p> The underlying Linux system call requires an additional argument, <i>size_t sizemask</i>, which specifies the size of the <i>mask</i> argument. The glibc <code>signalfd</code>() wrapper function does not include this argument, since it provides the required value for the underlying system call. </p>
<p> There are two underlying Linux system calls: <code>signalfd</code>() and the more recent <code>signalfd4</code>(). The former system call does not implement a <i>flags</i> argument. The latter system call implements the <i>flags</i> values described above. Starting with glibc 2.9, the <code>signalfd</code>() wrapper function will use <code>signalfd4</code>() where it is available.</p>
<h2>BUGS</h2>
<p> In kernels before 2.6.25, the <i>ssi_ptr</i> and <i>ssi_int</i> fields are not filled in with the data accompanying a signal sent by <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3).</p>
<h2>EXAMPLES</h2>
<p> The program below accepts the signals <code>SIGINT</code> and <code>SIGQUIT</code> via a signalfd file descriptor. The program terminates after accepting a <code>SIGQUIT</code> signal. The following shell session demonstrates the use of the program: </p>
<p> $<code> ./signalfd_demo</code> <code>haC</code> # Control-C generates SIGINT Got SIGINT <code>haC</code> Got SIGINT <code>ha\</code> # Control-\ generates SIGQUIT Got SIGQUIT $</p>
<h3>Program source</h3>
<p> #include &lt;sys/signalfd.h&gt; #include &lt;signal.h&gt; #include &lt;unistd.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigset_t mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct signalfd_siginfo fdsi;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigemptyset(&amp;mask);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigaddset(&amp;mask, SIGINT);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigaddset(&amp;mask, SIGQUIT); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Block signals so that they aren&#8217;t handled<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;according to their default dispositions&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sigprocmask(SIG_BLOCK,&nbsp;&amp;mask, NULL)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;sigprocmask&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sfd&nbsp;=&nbsp;signalfd(-1,&nbsp;&amp;mask, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sfd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;signalfd&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(;;)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;read(sfd,&nbsp;&amp;fdsi, sizeof(fdsi));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;sizeof(fdsi))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;read&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fdsi.ssi_signo&nbsp;==&nbsp;SIGINT)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Got SIGINT
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else if&nbsp;(fdsi.ssi_signo&nbsp;==&nbsp;SIGQUIT)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Got SIGQUIT
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Read unexpected signal
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-eventfd/">eventfd</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
