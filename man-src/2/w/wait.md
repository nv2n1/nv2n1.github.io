---
title: "wait(2)"
name: "wait"
section: "2"
letter: "w"
url: "/docs/linux/man/2-wait/"
description: "wait, waitpid, waitid – wait for process to change state"
---

<h2 class="name">NAME</h2>
<p> wait, waitpid, waitid &#8211; wait for process to change state </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;sys/wait.h&gt;</code> </p>
<p> <code>pid_t wait(int *</code><i>wstatus</i><code>);</code> </p>
<p> <code>pid_t waitpid(pid_t </code><i>pid</i><code>, int *</code><i>wstatus</i><code>, int </code><i>options</i><code>);</code> </p>
<p> <code>int waitid(idtype_t </code><i>idtype</i><code>, id_t </code><i>id</i><code>, siginfo_t *</code><i>infop</i><code>, int </code><i>options</i><code>);</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;This is the glibc and POSIX interface;&nbsp;see<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;NOTES for information on the raw system call.&nbsp;*/ </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>waitid</code>():</p>
<dl>
<dt>
<dd> Since glibc 2.26: _XOPEN_SOURCE &gt;= 500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
 Glibc 2.25 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> All of these system calls are used to wait for state changes in a child of the calling process, and obtain information about the child whose state has changed. A state change is considered to be: the child terminated; the child was stopped by a signal; or the child was resumed by a signal. In the case of a terminated child, performing a wait allows the system to release the resources associated with the child; if a wait is not performed, then the terminated child remains in a &quot;zombie&quot; state (see NOTES below). </p>
<p> If a child has already changed state, then these calls return immediately. Otherwise, they block until either a child changes state or a signal handler interrupts the call (assuming that system calls are not automatically restarted using the <code>SA_RESTART</code> flag of <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)). In the remainder of this page, a child whose state has changed and which has not yet been waited upon by one of these system calls is termed <i>waitable</i>.</p>
<h3>wait() and waitpid()</h3>
<p> The <code>wait</code>() system call suspends execution of the calling thread until one of its children terminates. The call <i>wait(&amp;wstatus)</i> is equivalent to: </p>
<p> waitpid(-1, &amp;wstatus, 0); </p>
<p> The <code>waitpid</code>() system call suspends execution of the calling thread until a child specified by <i>pid</i> argument has changed state. By default, <code>waitpid</code>() waits only for terminated children, but this behavior is modifiable via the <i>options</i> argument, as described below. </p>
<p> The value of <i>pid</i> can be:</p>
<dl>
<dt>&lt; -1</p>
<dd> meaning wait for any child process whose process group ID is equal to the absolute value of <i>pid</i>.</p>
<dt>-1</p>
<dd> meaning wait for any child process.</p>
<dt>0</p>
<dd> meaning wait for any child process whose process group ID is equal to that of the calling process at the time of the call to <code>waitpid</code>().</p>
<dt>&gt; 0</p>
<dd> meaning wait for the child whose process ID is equal to the value of <i>pid</i>.</dl>
<p> The value of <i>options</i> is an OR of zero or more of the following constants:</p>
<dl>
<dt><code>WNOHANG</code></p>
<dd> return immediately if no child has exited.</p>
<dt><code>WUNTRACED</code></p>
<dd> also return if a child has stopped (but not traced via <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)). Status for <i>traced</i> children which have stopped is provided even if this option is not specified.</p>
<dt><code>WCONTINUED</code> (since Linux 2.6.10)</p>
<dd> also return if a stopped child has been resumed by delivery of <code>SIGCONT</code>.</dl>
<p> (For Linux-only options, see below.) </p>
<p> If <i>wstatus</i> is not NULL, <code>wait</code>() and <code>waitpid</code>() store status information in the <i>int</i> to which it points. This integer can be inspected with the following macros (which take the integer itself as an argument, not a pointer to it, as is done in <code>wait</code>() and <code>waitpid</code>()!):</p>
<dl>
<dt><code>WIFEXITED(</code><i>wstatus</i><code>)</code></p>
<dd> returns true if the child terminated normally, that is, by calling <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) or <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), or by returning from main().</p>
<dt><code>WEXITSTATUS(</code><i>wstatus</i><code>)</code></p>
<dd> returns the exit status of the child. This consists of the least significant 8 bits of the <i>status</i> argument that the child specified in a call to <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) or <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) or as the argument for a return statement in main(). This macro should be employed only if <code>WIFEXITED</code> returned true.</p>
<dt><code>WIFSIGNALED(</code><i>wstatus</i><code>)</code></p>
<dd> returns true if the child process was terminated by a signal.</p>
<dt><code>WTERMSIG(</code><i>wstatus</i><code>)</code></p>
<dd> returns the number of the signal that caused the child process to terminate. This macro should be employed only if <code>WIFSIGNALED</code> returned true.</p>
<dt><code>WCOREDUMP(</code><i>wstatus</i><code>)</code></p>
<dd> returns true if the child produced a core dump (see <code><a href="/docs/linux/man/5-core/">core</a></code>(5)). This macro should be employed only if <code>WIFSIGNALED</code> returned true.</p>
<dt>
<dd> This macro is not specified in POSIX.1-2001 and is not available on some UNIX implementations (e.g., AIX, SunOS). Therefore, enclose its use inside <i>#ifdef WCOREDUMP &#8230; #endif</i>.</p>
<dt><code>WIFSTOPPED(</code><i>wstatus</i><code>)</code></p>
<dd> returns true if the child process was stopped by delivery of a signal; this is possible only if the call was done using <code>WUNTRACED</code> or when the child is being traced (see <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)).</p>
<dt><code>WSTOPSIG(</code><i>wstatus</i><code>)</code></p>
<dd> returns the number of the signal which caused the child to stop. This macro should be employed only if <code>WIFSTOPPED</code> returned true.</p>
<dt><code>WIFCONTINUED(</code><i>wstatus</i><code>)</code></p>
<dd> (since Linux 2.6.10) returns true if the child process was resumed by delivery of <code>SIGCONT</code>.</dl>
<h3>waitid()</h3>
<p> The <code>waitid</code>() system call (available since Linux 2.6.9) provides more precise control over which child state changes to wait for. </p>
<p> The <i>idtype</i> and <i>id</i> arguments select the child(ren) to wait for, as follows:</p>
<dl>
<dt><i>idtype</i> == <code>P_PID</code></p>
<dd> Wait for the child whose process ID matches <i>id</i>.</p>
<dt><i>idtype</i> == <code>P_PIDFD</code> (since Linux 5.4)</p>
<dd> Wait for the child referred to by the PID file descriptor specified in <i>id</i>. (See <code><a href="/docs/linux/man/2-pidfd_open/">pidfd_open</a></code>(2) for further information on PID file descriptors.)</p>
<dt><i>idtype</i> == <code>P_PGID</code></p>
<dd> Wait for any child whose process group ID matches <i>id</i>. Since Linux 5.4, if <i>id</i> is zero, then wait for any child that is in the same process group as the caller&#8217;s process group at the time of the call.</p>
<dt><i>idtype</i> == <code>P_ALL</code></p>
<dd> Wait for any child; <i>id</i> is ignored.</dl>
<p> The child state changes to wait for are specified by ORing one or more of the following flags in <i>options</i>:</p>
<dl>
<dt><code>WEXITED</code></p>
<dd> Wait for children that have terminated.</p>
<dt><code>WSTOPPED</code></p>
<dd> Wait for children that have been stopped by delivery of a signal.</p>
<dt><code>WCONTINUED</code></p>
<dd> Wait for (previously stopped) children that have been resumed by delivery of <code>SIGCONT</code>.</dl>
<p> The following flags may additionally be ORed in <i>options</i>:</p>
<dl>
<dt><code>WNOHANG</code></p>
<dd> As for <code>waitpid</code>().</p>
<dt><code>WNOWAIT</code></p>
<dd> Leave the child in a waitable state; a later wait call can be used to again retrieve the child status information.</dl>
<p> Upon successful return, <code>waitid</code>() fills in the following fields of the <i>siginfo_t</i> structure pointed to by <i>infop</i>:</p>
<dl>
<dt><i>si_pid</i></p>
<dd> The process ID of the child.</p>
<dt><i>si_uid</i></p>
<dd> The real user ID of the child. (This field is not set on most other implementations.)</p>
<dt><i>si_signo</i></p>
<dd> Always set to <code>SIGCHLD</code>.</p>
<dt><i>si_status</i></p>
<dd> Either the exit status of the child, as given to <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) (or <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3)), or the signal that caused the child to terminate, stop, or continue. The <i>si_code</i> field can be used to determine how to interpret this field.</p>
<dt><i>si_code</i></p>
<dd> Set to one of: <code>CLD_EXITED</code> (child called <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2)); <code>CLD_KILLED</code> (child killed by signal); <code>CLD_DUMPED</code> (child killed by signal, and dumped core); <code>CLD_STOPPED</code> (child stopped by signal); <code>CLD_TRAPPED</code> (traced child has trapped); or <code>CLD_CONTINUED</code> (child continued by <code>SIGCONT</code>).</dl>
<p> If <code>WNOHANG</code> was specified in <i>options</i> and there were no children in a waitable state, then <code>waitid</code>() returns 0 immediately and the state of the <i>siginfo_t</i> structure pointed to by <i>infop</i> depends on the implementation. To (portably) distinguish this case from that where a child was in a waitable state, zero out the <i>si_pid</i> field before the call and check for a nonzero value in this field after the call returns. </p>
<p> POSIX.1-2008 Technical Corrigendum 1 (2013) adds the requirement that when <code>WNOHANG</code> is specified in <i>options</i> and there were no children in a waitable state, then <code>waitid</code>() should zero out the <i>si_pid</i> and <i>si_signo</i> fields of the structure. On Linux and other implementations that adhere to this requirement, it is not necessary to zero out the <i>si_pid</i> field before calling <code>waitid</code>(). However, not all implementations follow the POSIX.1 specification on this point.</p>
<h2>RETURN VALUE</h2>
<p> <code>wait</code>(): on success, returns the process ID of the terminated child; on error, -1 is returned. </p>
<p> <code>waitpid</code>(): on success, returns the process ID of the child whose state has changed; if <code>WNOHANG</code> was specified and one or more child(ren) specified by <i>pid</i> exist, but have not yet changed state, then 0 is returned. On error, -1 is returned. </p>
<p> <code>waitid</code>(): returns 0 on success or if <code>WNOHANG</code> was specified and no child(ren) specified by <i>id</i> has yet changed state; on error, -1 is returned. </p>
<p> Each of these calls sets <i>errno</i> to an appropriate value in the case of an error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ECHILD</code></p>
<dd> (for <code>wait</code>()) The calling process does not have any unwaited-for children.</p>
<dt><code>ECHILD</code></p>
<dd> (for <code>waitpid</code>() or <code>waitid</code>()) The process specified by <i>pid</i> (<code>waitpid</code>()) or <i>idtype</i> and <i>id</i> (<code>waitid</code>()) does not exist or is not a child of the calling process. (This can happen for one&#8217;s own child if the action for <code>SIGCHLD</code> is set to <code>SIG_IGN</code>. See also the <i>Linux Notes</i> section about threads.)</p>
<dt><code>EINTR</code></p>
<dd> <code>WNOHANG</code> was not set and an unblocked signal or a <code>SIGCHLD</code> was caught; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> The <i>options</i> argument was invalid.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.3BSD, POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> A child that terminates, but has not been waited for becomes a &quot;zombie&quot;. The kernel maintains a minimal set of information about the zombie process (PID, termination status, resource usage information) in order to allow the parent to later perform a wait to obtain information about the child. As long as a zombie is not removed from the system via a wait, it will consume a slot in the kernel process table, and if this table fills, it will not be possible to create further processes. If a parent process terminates, then its &quot;zombie&quot; children (if any) are adopted by <code><a href="/docs/linux/man/1-init/">init</a></code>(1), (or by the nearest &quot;subreaper&quot; process as defined through the use of the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_CHILD_SUBREAPER</code> operation); <code><a href="/docs/linux/man/1-init/">init</a></code>(1) automatically performs a wait to remove the zombies. </p>
<p> POSIX.1-2001 specifies that if the disposition of <code>SIGCHLD</code> is set to <code>SIG_IGN</code> or the <code>SA_NOCLDWAIT</code> flag is set for <code>SIGCHLD</code> (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)), then children that terminate do not become zombies and a call to <code>wait</code>() or <code>waitpid</code>() will block until all children have terminated, and then fail with <i>errno</i> set to <code>ECHILD</code>. (The original POSIX standard left the behavior of setting <code>SIGCHLD</code> to <code>SIG_IGN</code> unspecified. Note that even though the default disposition of <code>SIGCHLD</code> is &quot;ignore&quot;, explicitly setting the disposition to <code>SIG_IGN</code> results in different treatment of zombie process children.) </p>
<p> Linux 2.6 conforms to the POSIX requirements. However, Linux 2.4 (and earlier) does not: if a <code>wait</code>() or <code>waitpid</code>() call is made while <code>SIGCHLD</code> is being ignored, the call behaves just as though <code>SIGCHLD</code> were not being ignored, that is, the call blocks until the next child terminates and then returns the process ID and status of that child.</p>
<h3>Linux notes</h3>
<p> In the Linux kernel, a kernel-scheduled thread is not a distinct construct from a process. Instead, a thread is simply a process that is created using the Linux-unique <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) system call; other routines such as the portable <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) call are implemented using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). Before Linux 2.4, a thread was just a special case of a process, and as a consequence one thread could not wait on the children of another thread, even when the latter belongs to the same thread group. However, POSIX prescribes such functionality, and since Linux 2.4 a thread can, and by default will, wait on children of other threads in the same thread group. </p>
<p> The following Linux-specific <i>options</i> are for use with children created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2); they can also, since Linux 4.7, be used with <code>waitid</code>():</p>
<dl>
<dt><code>__WCLONE</code></p>
<dd> Wait for &quot;clone&quot; children only. If omitted, then wait for &quot;non-clone&quot; children only. (A &quot;clone&quot; child is one which delivers no signal, or a signal other than <code>SIGCHLD</code> to its parent upon termination.) This option is ignored if <code>__WALL</code> is also specified.</p>
<dt><code>__WALL</code> (since Linux 2.4)</p>
<dd> Wait for all children, regardless of type (&quot;clone&quot; or &quot;non-clone&quot;).</p>
<dt><code>__WNOTHREAD</code> (since Linux 2.4)</p>
<dd> Do not wait for children of other threads in the same thread group. This was the default before Linux 2.4.</dl>
<p> Since Linux 4.7, the <code>__WALL</code> flag is automatically implied if the child is being ptraced.</p>
<h3>C library/kernel differences</h3>
<p> <code>wait</code>() is actually a library function that (in glibc) is implemented as a call to <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2). </p>
<p> On some architectures, there is no <code>waitpid</code>() system call; instead, this interface is implemented via a C library wrapper function that calls <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2). </p>
<p> The raw <code>waitid</code>() system call takes a fifth argument, of type <i>struct rusage&nbsp;*</i>. If this argument is non-NULL, then it is used to return resource usage information about the child, in the same manner as <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2). See <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2) for details.</p>
<h2>BUGS</h2>
<p> According to POSIX.1-2008, an application calling <code>waitid</code>() must ensure that <i>infop</i> points to a <i>siginfo_t</i> structure (i.e., that it is a non-null pointer). On Linux, if <i>infop</i> is NULL, <code>waitid</code>() succeeds, and returns the process ID of the waited-for child. Applications should avoid relying on this inconsistent, nonstandard, and unnecessary feature.</p>
<h2>EXAMPLES</h2>
<p> The following program demonstrates the use of <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code>waitpid</code>(). The program creates a child process. If no command-line argument is supplied to the program, then the child suspends its execution using <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), to allow the user to send signals to the child. Otherwise, if a command-line argument is supplied, then the child exits immediately, using the integer supplied on the command line as the exit status. The parent process executes a loop that monitors the child using <code>waitpid</code>(), and uses the W*() macros described above to analyze the wait status value. </p>
<p> The following shell session demonstrates the use of the program: </p>
<p> $<code> ./a.out &amp;</code> Child PID is 32360 [1] 32359 $<code> kill -STOP 32360</code> stopped by signal 19 $<code> kill -CONT 32360</code> continued $<code> kill -TERM 32360</code> killed by signal 15 [1]+ Done ./a.out $</p>
<h3>Program source</h3>
<p> #include &lt;sys/wait.h&gt; #include &lt;stdint.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t cpid, w;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int wstatus; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cpid&nbsp;=&nbsp;fork();<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cpid&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fork&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cpid&nbsp;==&nbsp;0)&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Code executed by child&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Child PID is&nbsp;%jd
&quot;,&nbsp;(intmax_t)&nbsp;getpid());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;==&nbsp;1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pause();&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait for signals&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_exit(atoi(argv[1])); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Code executed by parent&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;w&nbsp;=&nbsp;waitpid(cpid,&nbsp;&amp;wstatus, WUNTRACED | WCONTINUED);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(w&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;waitpid&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(WIFEXITED(wstatus))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;exited, status=%d
&quot;, WEXITSTATUS(wstatus));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else if&nbsp;(WIFSIGNALED(wstatus))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;killed by signal&nbsp;%d
&quot;, WTERMSIG(wstatus));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else if&nbsp;(WIFSTOPPED(wstatus))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;stopped by signal&nbsp;%d
&quot;, WSTOPSIG(wstatus));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else if&nbsp;(WIFCONTINUED(wstatus))&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;continued
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(!WIFEXITED(wstatus)&nbsp;&amp;&amp;&nbsp;!WIFSIGNALED(wstatus));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/5-core/">core</a></code>(5), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
