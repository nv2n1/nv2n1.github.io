---
title: "strace(1)"
name: "strace"
section: "1"
letter: "s"
url: "/docs/linux/man/1-strace/"
description: "strace – trace system calls and signals"
---

<h2 class="name">NAME</h2>
<p> strace &#8211; trace system calls and signals </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-ACdffhikqqrtttTvVwxxyyzZ</code> ] [ <code>-I </code><i>n</i> ] [ <code>-b </code><i>execve</i> ] [<code>-e</code><i>&nbsp;expr</i>]&#8230; [ <code>-O </code><i>overhead</i> ] [ <code>-S </code><i>sortby</i> ] [ <code>-U </code><i>columns</i> ] [ <code>-a </code><i>column</i> ] [ <code>-o </code><i>file</i> ] [ <code>-s </code><i>strsize</i> ] [ <code>-X </code><i>format</i> ] [<code>-P</code><i>&nbsp;path</i>]&#8230; [<code>-p</code><i>&nbsp;pid</i>]&#8230; [ <code>&#8211;seccomp-bpf</code> ] { <code>-p</code><i>&nbsp;pid</i> | [ <code>-DDD</code> ] [<code>-E</code><i>&nbsp;var[=<i>val</i>]</i>]&#8230; [ <code>-u </code><i>username</i> ] <i>command</i> [<i>args</i>] } <code>-c</code> [ <code>-dfwzZ</code> ] [ <code>-I </code><i>n</i> ] [ <code>-b </code><i>execve</i> ] [<code>-e</code><i>&nbsp;expr</i>]&#8230; [ <code>-O </code><i>overhead</i> ] [ <code>-S </code><i>sortby</i> ] [ <code>-U </code><i>columns</i> ] [<code>-P</code><i>&nbsp;path</i>]&#8230; [<code>-p</code><i>&nbsp;pid</i>]&#8230; [ <code>&#8211;seccomp-bpf</code> ] { <code>-p</code><i>&nbsp;pid</i> | [ <code>-DDD</code> ] [<code>-E</code><i>&nbsp;var[=<i>val</i>]</i>]&#8230; [ <code>-u </code><i>username</i> ] <i>command</i> [<i>args</i>] }</p>
<h2>DESCRIPTION</h2>
<p> In the simplest case <code>strace</code> runs the specified <i>command</i> until it exits. It intercepts and records the system calls which are called by a process and the signals which are received by a process. The name of each system call, its arguments and its return value are printed on standard error or to the file specified with the <code>-o</code> option. </p>
<p> <code>strace</code> is a useful diagnostic, instructional, and debugging tool. System administrators, diagnosticians and trouble-shooters will find it invaluable for solving problems with programs for which the source is not readily available since they do not need to be recompiled in order to trace them. Students, hackers and the overly-curious will find that a great deal can be learned about a system and its system calls by tracing even ordinary programs. And programmers will find that since system calls and signals are events that happen at the user/kernel interface, a close examination of this boundary is very useful for bug isolation, sanity checking and attempting to capture race conditions. </p>
<p> Each line in the trace contains the system call name, followed by its arguments in parentheses and its return value. An example from stracing the command &quot;cat /dev/null&quot; is: </p>
<pre>
open(&quot;/dev/null&quot;, O_RDONLY) = 3
</pre>
<p> Errors (typically a return value of -1) have the errno symbol and error string appended. </p>
<pre>
open(&quot;/foo/bar&quot;, O_RDONLY) = -1 ENOENT (No such file or directory)
</pre>
<p> Signals are printed as signal symbol and decoded siginfo structure. An excerpt from stracing and interrupting the command &quot;sleep 666&quot; is: </p>
<pre><code>
sigsuspend([] &lt;unfinished ...&gt;
--- SIGINT {
    si_signo = SIGINT, si_code = SI_USER, si_pid = ...} ---
+++ killed by SIGINT +++
</code></pre>
<p> If a system call is being executed and meanwhile another one is being called from a different thread/process then <code>strace</code> will try to preserve the order of those events and mark the ongoing call as being <i>unfinished</i>. When the call returns it will be marked as <i>resumed</i>. </p>
<p>[pid 28772] select(4, [3], NULL, NULL, NULL&lt;unfinished&#8230;&gt;[pid 28779] clock_gettime(CLOCK_REALTIME, {1130322148, 939977000}) = 0 [pid 28772]&lt;&#8230; select resumed&gt;) = 1(in[3])</p>
<p> Interruption of a (restartable) system call by a signal delivery is processed differently as kernel terminates the system call and also arranges its immediate reexecution after the signal handler completes. </p>
<pre>
read(0, 0x7ffff72cf5cf, 1)              = ? ERESTARTSYS (To be restarted)
--- SIGALRM ... ---
rt_sigreturn(0xe)                       = 0
read(0, &quot;&quot;, 1)                          = 0
</pre>
<p> Arguments are printed in symbolic form with passion. This example shows the shell performing &quot;&gt;&gt;xyzzy&quot; output redirection: </p>
<pre>
open(&quot;xyzzy&quot;, O_WRONLY|O_APPEND|O_CREAT, 0666) = 3
</pre>
<p> Here, the second and the third argument of <code><a href="/docs/linux/man/2-open/">open</a></code>(2) are decoded by breaking down the flag argument into its three bitwise-OR constituents and printing the mode value in octal by tradition. Where the traditional or native usage differs from ANSI or POSIX, the latter forms are preferred. In some cases, <code>strace</code> output is proven to be more readable than the source. </p>
<p> Structure pointers are dereferenced and the members are displayed as appropriate. In most cases, arguments are formatted in the most C-like fashion possible. For example, the essence of the command &quot;ls -l /dev/null&quot; is captured as: </p>
<pre>
lstat(&quot;/dev/null&quot;, {st_mode=S_IFCHR|0666, st_rdev=makedev(0x1, 0x3), ...}) = 0
</pre>
<p> Notice how the &#8216;struct stat&#8217; argument is dereferenced and how each member is displayed symbolically. In particular, observe how the <code>st_mode</code> member is carefully decoded into a bitwise-OR of symbolic and numeric values. Also notice in this example that the first argument to <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) is an input to the system call and the second argument is an output. Since output arguments are not modified if the system call fails, arguments may not always be dereferenced. For example, retrying the &quot;ls -l&quot; example with a non-existent file produces the following line: </p>
<pre>
lstat(&quot;/foo/bar&quot;, 0xb004) = -1 ENOENT (No such file or directory)
</pre>
<p> In this case the porch light is on but nobody is home. </p>
<p> Syscalls unknown to <code>strace</code> are printed raw, with the unknown system call number printed in hexadecimal form and prefixed with &quot;syscall_&quot;: </p>
<pre>
syscall_0xbad(0x1, 0x2, 0x3, 0x4, 0x5, 0x6) = -1 ENOSYS (Function not implemented)
</pre>
<p> Character pointers are dereferenced and printed as C strings. Non-printing characters in strings are normally represented by ordinary C escape codes. Only the first <i>strsize</i> (32 by default) bytes of strings are printed; longer strings have an ellipsis appended following the closing quote. Here is a line from &quot;ls -l&quot; where the <code><a href="/docs/linux/man/3-getpwuid/">getpwuid</a></code>(3) library routine is reading the password file: </p>
<pre>
read(3, &quot;root::0:0:System Administrator:/&quot;..., 1024) = 422
</pre>
<p> While structures are annotated using curly braces, simple pointers and arrays are printed using square brackets with commas separating elements. Here is an example from the command <code><a href="/docs/linux/man/1-id/">id</a></code>(1) on a system with supplementary group ids: </p>
<pre>
getgroups(32, [100, 0]) = 2
</pre>
<p> On the other hand, bit-sets are also shown using square brackets, but set elements are separated only by a space. Here is the shell, preparing to execute an external command: </p>
<p>sigprocmask(SIG_BLOCK, [CHLD TTOU], []) = 0</p>
<p> Here, the second argument is a bit-set of two signals, <code>SIGCHLD</code> and <code>SIGTTOU</code>. In some cases, the bit-set is so full that printing out the unset elements is more valuable. In that case, the bit-set is prefixed by a tilde like this: </p>
<pre>
sigprocmask(SIG_UNBLOCK, ~[], NULL) = 0
</pre>
<p> Here, the second argument represents the full set of all signals.</p>
<h2>OPTIONS</h2>
<h3>General</h3>
<dl>
<dt><code>-e </code><i>expr</i></p>
<dd> A qualifying expression which modifies which events to trace or how to trace them. The format of the expression is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> [,<i>qualifier/</i><code>=</code>][<code>!</code>],<i>value/</i>[<code>,</code>,<i>value/</i>]&#8230;</dl>
</dl>
<dt>
<dd> where <i>qualifier</i> is one of <code>trace</code> (or <code>t</code>), <code>abbrev</code> (or <code>a</code>), <code>verbose</code> (or <code>v</code>), <code>raw</code> (or <code>x</code>), <code>signal</code> (or <code>signals</code> or <code>s</code>), <code>read</code> (or <code>reads</code> or <code>r</code>), <code>write</code> (or <code>writes</code> or <code>w</code>), <code>fault</code>, <code>inject</code>, <code>status</code>, <code>quiet</code> (or <code>silent</code> or <code>silence</code> or <code>q</code>), <code>decode-fds</code> (or <code>decode-fd</code>), <code>decode-pids</code> (or <code>decode-pid</code>), or <code>kvm</code>, and <i>value</i> is a qualifier-dependent symbol or number. The default qualifier is <code>trace</code>. Using an exclamation mark negates the set of values. For example, <code>-e</code>&nbsp;<code>open</code> means literally <code>-e</code>&nbsp;<code>trace</code>=<code>open</code> which in turn means trace only the <code>open</code> system call. By contrast, <code>-e</code>&nbsp;<code>trace</code>=!<code>open</code> means to trace every system call except <code>open</code>. In addition, the special values <code>all</code> and <code>none</code> have the obvious meanings.</p>
<dt>
<dd> Note that some shells use the exclamation point for history expansion even inside quoted arguments. If so, you must escape the exclamation point with a backslash.</dl>
<h3>Startup</h3>
<dl>
<dt><code>-E&nbsp;</code><i>var</i>=,<i>val</i></p>
<dd> <code>&#8211;env</code>=<i>var</i>=<i>val</i> Run command with <i>var</i>=<i>val</i> in its list of environment variables.</p>
<dt><code>-E </code><i>var</i></p>
<dd> <code>&#8211;env</code>=<i>var</i> Remove <i>var</i> from the inherited list of environment variables before passing it on to the command.</p>
<dt><code>-p </code><i>pid</i></p>
<dd> <code>&#8211;attach</code>=<i>pid</i> Attach to the process with the process <font SIZE="-1">ID</font> <i>pid</i> and begin tracing. The trace may be terminated at any time by a keyboard interrupt signal (<code>CTRL-C</code>). <code>strace</code> will respond by detaching itself from the traced process(es) leaving it (them) to continue running. Multiple <code>-p</code> options can be used to attach to many processes in addition to <i>command</i> (which is optional if at least one <code>-p</code> option is given). Multiple process IDs, separated by either comma (&#8220;,&#8221;), space (&#8221; &#8220;), tab, or newline character, can be provided as an argument to a single <code>-p</code> option, so, for example, <code>-p</code> &quot;$(pidof PROG)&quot; and <code>-p</code> &quot;$(pgrep PROG)&quot; syntaxes are supported.</p>
<dt><code>-u </code><i>username</i></p>
<dd> <code>&#8211;user</code>=<i>username</i> Run command with the user <font SIZE="-1">ID</font>, group <font SIZE="-2">ID</font>, and supplementary groups of <i>username</i>. This option is only useful when running as root and enables the correct execution of setuid and/or setgid binaries. Unless this option is used setuid and setgid programs are executed without effective privileges.</dl>
<h3>Tracing</h3>
<dl>
<dt><code>-b </code><i>syscall</i></p>
<dd> <code>&#8211;detach-on</code>=<i>syscall</i> If specified syscall is reached, detach from traced process. Currently, only <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) syscall is supported. This option is useful if you want to trace multi-threaded process and therefore require <code>-f</code>, but don&#8217;t want to trace its (potentially very complex) children.</p>
<dt><code>-D</code></p>
<dd> <code>&#8211;daemonize</code> <code>&#8211;daemonize</code>=<code>grandchild</code> Run tracer process as a grandchild, not as the parent of the tracee. This reduces the visible effect of <code>strace</code> by keeping the tracee a direct child of the calling process.</p>
<dt><code>-DD</code></p>
<dd> <code>&#8211;daemonize</code>=<code>pgroup</code> <code>&#8211;daemonize</code>=<code>pgrp</code> Run tracer process as tracee&#8217;s grandchild in a separate process group. In addition to reduction of the visible effect of <code>strace</code>, it also avoids killing of <code>strace</code> with <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2) issued to the whole process group.</p>
<dt><code>-DDD</code></p>
<dd> <code>&#8211;daemonize</code>=<code>session</code> Run tracer process as tracee&#8217;s grandchild in a separate session (&quot;true daemonisation&quot;). In addition to reduction of the visible effect of <code>strace</code>, it also avoids killing of <code>strace</code> upon session termination.</p>
<dt><code>-f</code></p>
<dd> <code>&#8211;follow-forks</code> Trace child processes as they are created by currently traced processes as a result of the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-vfork/">vfork</a></code>(2) and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) system calls. Note that <code>-p</code> <i>PID</i> <code>-f</code> will attach all threads of process <i>PID</i> if it is multi-threaded, not only thread with <i>thread_id</i> = <i>PID</i>.</p>
<dt><code>&#8211;output-separately</code></p>
<dd> If the <code>&#8211;output</code>=<i>filename</i> option is in effect, each processes trace is written to <i>filename</i>.<i>pid</i> where <i>pid</i> is the numeric process id of each process.</p>
<dt><code>-ff</code></p>
<dd> <code>&#8211;follow-forks &#8211;output-separately</code> Combine the effects of <code>&#8211;follow-forks</code> and <code>&#8211;output-separately</code> options. This is incompatible with <code>-c</code>, since no per-process counts are kept.</p>
<dt>
<dd> One might want to consider using <code><a href="/docs/linux/man/1-strace-log-merge/">strace-log-merge</a></code>(1) to obtain a combined strace log view.</p>
<dt><code>-I </code><i>interruptible</i></p>
<dd> <code>&#8211;interruptible</code>=<i>interruptible</i> When <code>strace</code> can be interrupted by signals (such as pressing <code>CTRL-C</code>).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1</code>, <code>anywhere</code></p>
<dd> no signals are blocked; <code>2</code>, <code>waiting</code> fatal signals are blocked while decoding syscall (default); <code>3</code>, <code>never</code> fatal signals are always blocked (default if <code>-o</code> <i>FILE</i> <i>PROG</i>); <code>4</code>, <code>never_tstp</code> fatal signals and <code>SIGTSTP</code> (<code>CTRL-Z</code>) are always blocked (useful to make <code>strace -o </code><i>FILE PROG</i> not stop on <code>CTRL-Z</code>, default if <code>-D</code>).</dl>
</dl>
</dl>
<h3>Filtering</h3>
<dl>
<dt><code>-e trace</code>=,<i>syscall_set</i></p>
<dd> <code>&#8211;trace</code>=,<i>syscall_set</i> Trace only the specified set of system calls. <i>syscall_set</i> is defined as [<code>!</code>],<i>value</i>[<code>,</code>,<i>value/</i>], and <i>value</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>syscall</i></p>
<dd> Trace specific syscall, specified by its name (but see <code>NOTES</code>).</p>
<dt><code>?</code><i>value</i></p>
<dd> Question mark before the syscall qualification allows suppression of error in case no syscalls matched the qualification provided.</p>
<dt><code>/</code><i>regex</i></p>
<dd> Trace only those system calls that match the <i>regex</i>. You can use <code>POSIX</code> Extended Regular Expression syntax (see <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7)).</p>
<dt><i>syscall</i><code>@64</code></p>
<dd> Trace <i>syscall</i> only for the 64-bit personality.</p>
<dt><i>syscall</i><code>@32</code></p>
<dd> Trace <i>syscall</i> only for the 32-bit personality.</p>
<dt><i>syscall</i><code>@x32</code></p>
<dd> Trace <i>syscall</i> only for the 32-on-64-bit personality.</p>
<dt><code>%file</code></p>
<dd> <code>file</code> Trace all system calls which take a file name as an argument. You can think of this as an abbreviation for <code>-e trace</code>=<code>open</code>,<code>stat</code>,<code>chmod</code>,<code>unlink</code>,&#8230; which is useful to seeing what files the process is referencing. Furthermore, using the abbreviation will ensure that you don&#8217;t accidentally forget to include a call like <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) in the list. Betchya woulda forgot that one. The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>file</code>&quot;) is deprecated.</p>
<dt><code>%process</code></p>
<dd> <code>process</code> Trace system calls associated with process lifecycle (creation, exec, termination). The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>process</code>&quot;) is deprecated.</p>
<dt><code>%net</code></p>
<dd> <code>%network</code> <code>network</code> Trace all the network related system calls. The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>network</code>&quot;) is deprecated.</p>
<dt><code>%signal</code></p>
<dd> <code>signal</code> Trace all signal related system calls. The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>signal</code>&quot;) is deprecated.</p>
<dt><code>%ipc</code></p>
<dd> <code>ipc</code> Trace all IPC related system calls. The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>ipc</code>&quot;) is deprecated.</p>
<dt><code>%desc</code></p>
<dd> <code>desc</code> Trace all file descriptor related system calls. The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>desc</code>&quot;) is deprecated.</p>
<dt><code>%memory</code></p>
<dd> <code>memory</code> Trace all memory mapping related system calls. The syntax without a preceding percent sign (&quot;<code>-e trace</code>=<code>memory</code>&quot;) is deprecated.</p>
<dt><code>%creds</code></p>
<dd> Trace system calls that read or modify user and group identifiers or capability sets.</p>
<dt><code>%stat</code></p>
<dd> Trace stat syscall variants.</p>
<dt><code>%lstat</code></p>
<dd> Trace lstat syscall variants.</p>
<dt><code>%fstat</code></p>
<dd> Trace fstat, fstatat, and statx syscall variants.</p>
<dt><code>%%stat</code></p>
<dd> Trace syscalls used for requesting file status (stat, lstat, fstat, fstatat, statx, and their variants).</p>
<dt><code>%statfs</code></p>
<dd> Trace statfs, statfs64, statvfs, osf_statfs, and osf_statfs64 system calls. The same effect can be achieved with <code>-e trace</code>=<code>/^(.*_)?statv?fs</code> regular expression.</p>
<dt><code>%fstatfs</code></p>
<dd> Trace fstatfs, fstatfs64, fstatvfs, osf_fstatfs, and osf_fstatfs64 system calls. The same effect can be achieved with <code>-e trace</code>=<code>/fstatv?fs</code> regular expression.</p>
<dt><code>%%statfs</code></p>
<dd> Trace syscalls related to file system statistics (statfs-like, fstatfs-like, and ustat). The same effect can be achieved with <code>-e trace</code>=<code>/statv?fs|fsstat|ustat</code> regular expression.</p>
<dt><code>%clock</code></p>
<dd> Trace system calls that read or modify system clocks.</p>
<dt><code>%pure</code></p>
<dd> Trace syscalls that always succeed and have no arguments. Currently, this list includes <code><a href="/docs/linux/man/2-arc_gettls/">arc_gettls</a></code>(2), <code><a href="/docs/linux/man/2-getdtablesize/">getdtablesize</a></code>(2), <code><a href="/docs/linux/man/2-getegid/">getegid</a></code>(2), <code><a href="/docs/linux/man/2-getegid32/">getegid32</a></code>(2), <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2), <code><a href="/docs/linux/man/2-geteuid32/">geteuid32</a></code>(2), <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-getgid32/">getgid32</a></code>(2), <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></code>(2), <code><a href="/docs/linux/man/2-getpid/">getpid</a></code>(2), <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2), <code><a href="/docs/linux/man/2-get_thread_area/">get_thread_area</a></code>(2) (on architectures other than x86), <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2), <code><a href="/docs/linux/man/2-get_tls/">get_tls</a></code>(2), <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-getuid32/">getuid32</a></code>(2), <code><a href="/docs/linux/man/2-getxgid/">getxgid</a></code>(2), <code><a href="/docs/linux/man/2-getxpid/">getxpid</a></code>(2), <code><a href="/docs/linux/man/2-getxuid/">getxuid</a></code>(2), <code><a href="/docs/linux/man/2-kern_features/">kern_features</a></code>(2), and <code><a href="/docs/linux/man/2-metag_get_tls/">metag_get_tls</a></code>(2) syscalls.</dl>
</dl>
<dt>
<dd> The <code>-c</code> option is useful for determining which system calls might be useful to trace. For example, <code>trace</code>=<code>open,close,read,write</code> means to only trace those four system calls. Be careful when making inferences about the user/kernel boundary if only a subset of system calls are being monitored. The default is <code>trace</code>=<code>all</code>.</p>
<dt><code>-e signal</code>=,<i>set</i></p>
<dd> <code>&#8211;signal</code>=,<i>set</i> Trace only the specified subset of signals. The default is <code>signal</code>=<code>all</code>. For example, <code>signal</code>=!<code>SIGIO</code> (or <code>signal</code>=!<code>io</code>) causes <code>SIGIO</code> signals not to be traced.</p>
<dt><code>-e status</code>=,<i>set</i></p>
<dd> <code>&#8211;status</code>=,<i>set</i> Print only system calls with the specified return status. The default is <code>status</code>=<code>all</code>. When using the <code>status</code> qualifier, because <code>strace</code> waits for system calls to return before deciding whether they should be printed or not, the traditional order of events may not be preserved anymore. If two system calls are executed by concurrent threads, <code>strace</code> will first print both the entry and exit of the first system call to exit, regardless of their respective entry time. The entry and exit of the second system call to exit will be printed afterwards. Here is an example when <code><a href="/docs/linux/man/2-select/">select</a></code>(2) is called, but a different thread calls <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) before <code><a href="/docs/linux/man/2-select/">select</a></code>(2) finishes: </p>
<pre><code>
[pid 28779] 1130322148.939977 clock_gettime(CLOCK_REALTIME, {1130322148, 939977000}) = 0
    [pid 28772] 1130322148.438139 select(4, [3], NULL, NULL, NULL) = 1(in[3])
</code></pre>
<p> <i>set</i> can include the following elements:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>successful</code></p>
<dd> Trace system calls that returned without an error code. The <code>-z</code> option has the effect of <code>status</code>=<code>successful</code>. <code>failed</code> Trace system calls that returned with an error code. The <code>-Z</code> option has the effect of <code>status</code>=<code>failed</code>. <code>unfinished</code> Trace system calls that did not return. This might happen, for example, due to an execve call in a neighbour thread. <code>unavailable</code> Trace system calls that returned but strace failed to fetch the error status. <code>detached</code> Trace system calls for which strace detached before the return.</dl>
</dl>
<dt><code>-P </code><i>path</i></p>
<dd> <code>&#8211;trace-path</code>=<i>path</i> Trace only system calls accessing <i>path</i>. Multiple <code>-P</code> options can be used to specify several paths.</p>
<dt><code>-z</code></p>
<dd> <code>&#8211;successful-only</code> Print only syscalls that returned without an error code.</p>
<dt><code>-Z</code></p>
<dd> <code>&#8211;failed-only</code> Print only syscalls that returned with an error code.</dl>
<h3>Output format</h3>
<dl>
<dt><code>-a </code><i>column</i></p>
<dd> <code>&#8211;columns</code>=<i>column</i> Align return values in a specific column (default column 40).</p>
<dt><code>-e abbrev</code>=,<i>syscall_set</i></p>
<dd> <code>&#8211;abbrev</code>=,<i>syscall_set</i> Abbreviate the output from printing each member of large structures. The syntax of the <i>syscall_set</i> specification is the same as in the <code>-e trace</code> option. The default is <code>abbrev</code>=<code>all</code>. The <code>-v</code> option has the effect of <code>abbrev</code>=<code>none</code>.</p>
<dt><code>-e verbose</code>=,<i>syscall_set</i></p>
<dd> <code>&#8211;verbose</code>=,<i>syscall_set</i> Dereference structures for the specified set of system calls. The syntax of the <i>syscall_set</i> specification is the same as in the <code>-e trace</code> option. The default is <code>verbose</code>=<code>all</code>.</p>
<dt><code>-e raw</code>=,<i>syscall_set</i></p>
<dd> <code>&#8211;raw</code>=,<i>syscall_set</i> Print raw, undecoded arguments for the specified set of system calls. The syntax of the <i>syscall_set</i> specification is the same as in the <code>-e trace</code> option. This option has the effect of causing all arguments to be printed in hexadecimal. This is mostly useful if you don&#8217;t trust the decoding or you need to know the actual numeric value of an argument. See also <code>-X raw</code> option.</p>
<dt><code>-e read</code>=,<i>set</i></p>
<dd> <code>&#8211;read</code>=,<i>set</i> Perform a full hexadecimal and ASCII dump of all the data read from file descriptors listed in the specified set. For example, to see all input activity on file descriptors <i>3</i> and <i>5</i> use <code>-e read</code>=,<i>3</i>,<i>5</i>. Note that this is independent from the normal tracing of the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) system call which is controlled by the option <code>-e</code>&nbsp;<code>trace</code>=<code>read</code>.</p>
<dt><code>-e write</code>=,<i>set</i></p>
<dd> <code>&#8211;write</code>=,<i>set</i> Perform a full hexadecimal and ASCII dump of all the data written to file descriptors listed in the specified set. For example, to see all output activity on file descriptors <i>3</i> and <i>5</i> use <code>-e write</code>=,<i>3</i>,,<i>5</i>. Note that this is independent from the normal tracing of the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) system call which is controlled by the option <code>-e</code>&nbsp;<code>trace</code>=<code>write</code>.</p>
<dt><code>-e quiet</code>=,<i>set</i></p>
<dd> <code>&#8211;quiet</code>=,<i>set</i> <code>&#8211;silent</code>=,<i>set</i> <code>&#8211;silence</code>=,<i>set</i> Suppress various information messages. The default is <code>quiet</code>=<code>none</code>. <i>set</i> can include the following elements:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>attach</code></p>
<dd> Suppress messages about attaching and detaching (&quot;<code>[ Process NNNN attached ]</code>&quot;, &quot;<code>[ Process NNNN detached ]</code>&quot;). <code>exit</code> Suppress messages about process exits (&quot;<code>+++ exited with SSS +++</code>&quot;). <code>path-resolution</code> Suppress messages about resolution of paths provided via the <code>-P</code> option (&quot;<code>Requested path &quot;&#8230;&quot; resolved into &quot;&#8230;&quot;</code>&quot;). <code>personality</code> Suppress messages about process personality changes (&quot;<code>[ Process PID=NNNN runs in PPP mode. ]</code>&quot;). <code>thread-execve</code> <code>superseded</code> Suppress messages about process being superseded by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in another thread (&quot;<code>+++ superseded by execve in pid NNNN +++</code>&quot;).</dl>
</dl>
<dt><code>-e decode-fds</code>=,<i>set</i></p>
<dd> <code>&#8211;decode-fds</code>=,<i>set</i> Decode various information associated with file descriptors. The default is <code>decode-fds</code>=<code>none</code>. <i>set</i> can include the following elements:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>path</code></p>
<dd> Print file paths. Also enables printing of tracee&#8217;s current working directory when <code>AT_FDCWD</code> constant is used. <code>socket</code> Print socket protocol-specific information, <code>dev</code> Print character/block device numbers. <code>pidfd</code> Print PIDs associated with pidfd file descriptors.</dl>
</dl>
<dt><code>-e decode-pids</code>=,<i>set</i></p>
<dd> <code>&#8211;decode-pids</code>=,<i>set</i> Decode various information associated with process IDs (and also thread IDs, process group IDs, and session IDs). The default is <code>decode-pids</code>=<code>none</code>. <i>set</i> can include the following elements:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>comm</code></p>
<dd> Print command names associated with thread or process IDs. <code>pidns</code> Print thread, process, process group, and session IDs in strace&#8217;s PID namespace if the tracee is in a different PID namespace.</dl>
</dl>
<dt><code>-e kvm</code>=<code>vcpu</code></p>
<dd> <code>&#8211;kvm</code>=<code>vcpu</code> Print the exit reason of kvm vcpu. Requires Linux kernel version 4.16.0 or higher.</p>
<dt><code>-i</code></p>
<dd> <code>&#8211;instruction-pointer</code> Print the instruction pointer at the time of the system call.</p>
<dt><code>-n</code></p>
<dd> <code>&#8211;syscall-number</code> Print the syscall number.</p>
<dt><code>-k</code></p>
<dd> <code>&#8211;stack-traces</code> Print the execution stack trace of the traced processes after each system call.</p>
<dt><code>-o </code><i>filename</i></p>
<dd> <code>&#8211;output</code>=<i>filename</i> Write the trace output to the file <i>filename</i> rather than to stderr. <i>filename</i>.<i>pid</i> form is used if <code>-ff</code> option is supplied. If the argument begins with &#8216;|&#8217; or &#8216;!&#8217;, the rest of the argument is treated as a command and all output is piped to it. This is convenient for piping the debugging output to a program without affecting the redirections of executed programs. The latter is not compatible with <code>-ff</code> option currently.</p>
<dt><code>-A</code></p>
<dd> <code>&#8211;output-append-mode</code> Open the file provided in the <code>-o</code> option in append mode.</p>
<dt><code>-q</code></p>
<dd> <code>&#8211;quiet</code> <code>&#8211;quiet</code>=<code>attach</code>,<code>personality</code> Suppress messages about attaching, detaching, and personality changes. This happens automatically when output is redirected to a file and the command is run directly instead of attaching.</p>
<dt><code>-qq</code></p>
<dd> <code>&#8211;quiet</code>=<code>attach</code>,<code>personality</code>,<code>exit</code> Suppress messages attaching, detaching, personality changes, and about process exit status.</p>
<dt><code>-qqq</code></p>
<dd> <code>&#8211;quiet</code>=<code>all</code> Suppress all suppressible messages (please refer to the <code>-e quiet</code> option description for the full list of suppressible messages).</p>
<dt><code>-r</code></p>
<dd> <code>&#8211;relative-timestamps</code>[=<i>precision</i>] Print a relative timestamp upon entry to each system call. This records the time difference between the beginning of successive system calls. <i>precision</i> can be one of <code>s</code> (for seconds), <code>ms</code> (milliseconds), <code>us</code> (microseconds), or <code>ns</code> (nanoseconds), and allows setting the precision of time value being printed. Default is <code>us</code> (microseconds). Note that since <code>-r</code> option uses the monotonic clock time for measuring time difference and not the wall clock time, its measurements can differ from the difference in time reported by the <code>-t</code> option.</p>
<dt><code>-s </code><i>strsize</i></p>
<dd> <code>&#8211;string-limit</code>=<i>strsize</i> Specify the maximum string size to print (the default is 32). Note that filenames are not considered strings and are always printed in full.</p>
<dt><code>&#8211;absolute-timestamps</code>[=[[<code>format:</code>]<i>format</i>],[[<code>precision:</code>]<i>precision</i>]]</p>
<dd> <code>&#8211;timestamps</code>[=[[<code>format:</code>]<i>format</i>],[[<code>precision:</code>]<i>precision</i>]] Prefix each line of the trace with the wall clock time in the specified <i>format</i> with the specified <i>precision</i>. <i>format</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> No time stamp is printed. Can be used to override the previous setting. <code>time</code> Wall clock time (<code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) format string is <code>%T</code>). <code>unix</code> Number of seconds since the epoch (<code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) format string is <code>%s</code>).</dl>
</dl>
<dt>
<dd> <i>precision</i> can be one of <code>s</code> (for seconds), <code>ms</code> (milliseconds), <code>us</code> (microseconds), or <code>ns</code> (nanoseconds). Default arguments for the option are <code>format:time</code>,<code>precision:s</code>.</p>
<dt><code>-t</code></p>
<dd> <code>&#8211;absolute-timestamps</code> Prefix each line of the trace with the wall clock time.</p>
<dt><code>-tt</code></p>
<dd> <code>&#8211;absolute-timestamps</code>=<code>precision:us</code> If given twice, the time printed will include the microseconds.</p>
<dt><code>-ttt</code></p>
<dd> <code>&#8211;absolute-timestamps</code>=<code>format:unix</code>,<code>precision:us</code> If given thrice, the time printed will include the microseconds and the leading portion will be printed as the number of seconds since the epoch.</p>
<dt><code>-T</code></p>
<dd> <code>&#8211;syscall-times</code>[=<i>precision</i>] Show the time spent in system calls. This records the time difference between the beginning and the end of each system call. <i>precision</i> can be one of <code>s</code> (for seconds), <code>ms</code> (milliseconds), <code>us</code> (microseconds), or <code>ns</code> (nanoseconds), and allows setting the precision of time value being printed. Default is <code>us</code> (microseconds).</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;no-abbrev</code> Print unabbreviated versions of environment, stat, termios, etc. calls. These structures are very common in calls and so the default behavior displays a reasonable subset of structure members. Use this option to get all of the gory details.</p>
<dt><code>&#8211;strings-in-hex</code>[=<i>option</i>]</p>
<dd> Control usage of escape sequences with hexadecimal numbers in the printed strings. Normally (when no <code>&#8211;strings-in-hex</code> or <code>-x</code> option is supplied), escape sequences are used to print non-printable and non-ASCII characters (that is, characters with a character code less than 32 or greater than 127), or to disambiguate the output (so, for quotes and other characters that encase the printed string, for example, angle brackets, in case of file descriptor path output); for the former use case, unless it is a white space character that has a symbolic escape sequence defined in the C standard (that is, &#8220;<code>	</code>&#8221; for a horizontal tab, &#8220;<code>
</code>&#8221; for a newline, &#8220;<code></code>&#8221; for a vertical tab, &#8220;<code></code>&#8221; for a form feed page break, and &#8220;<code></code>&#8221; for a carriage return) are printed using escape sequences with numbers that correspond to their byte values, with octal number format being the default. <i>option</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Hexadecimal numbers are not used in the output at all. When there is a need to emit an escape sequence, octal numbers are used. <code>non-ascii-chars</code> Hexadecimal numbers are used instead of octal in the escape sequences. <code>non-ascii</code> Strings that contain non-ASCII characters are printed using escape sequences with hexadecimal numbers. <code>all</code> All strings are printed using escape sequences with hexadecimal numbers.</dl>
</dl>
<dt>
<dd> When the option is supplied without an argument, <code>all</code> is assumed.</p>
<dt><code>-x</code></p>
<dd> <code>&#8211;strings-in-hex</code>=<code>non-ascii</code> Print all non-ASCII strings in hexadecimal string format.</p>
<dt><code>-xx</code></p>
<dd> <code>&#8211;strings-in-hex</code>[=<code>all</code>] Print all strings in hexadecimal string format.</p>
<dt><code>-X </code><i>format</i></p>
<dd> <code>&#8211;const-print-style</code>=<i>format</i> Set the format for printing of named constants and flags. Supported <i>format</i> values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>raw</code></p>
<dd> Raw number output, without decoding. <code>abbrev</code> Output a named constant or a set of flags instead of the raw number if they are found. This is the default <code>strace</code> behaviour. <code>verbose</code> Output both the raw value and the decoded string (as a comment).</dl>
</dl>
<dt><code>-y</code></p>
<dd> <code>&#8211;decode-fds</code> <code>&#8211;decode-fds</code>=<code>path</code> Print paths associated with file descriptor arguments and with the <code>AT_FDCWD</code> constant.</p>
<dt><code>-yy</code></p>
<dd> <code>&#8211;decode-fds</code>=<code>all</code> Print all available information associated with file descriptors: protocol-specific information associated with socket file descriptors, block/character device number associated with device file descriptors, and PIDs associated with pidfd file descriptors.</p>
<dt><code>&#8211;pidns-translation</code></p>
<dd> <code>&#8211;decode-pids</code>=<code>pidns</code> If strace and tracee are in different PID namespaces, print PIDs in strace&#8217;s namespace, too.</p>
<dt><code>-Y</code></p>
<dd> <code>&#8211;decode-pids</code>=<code>comm</code> Print command names for PIDs.</dl>
<h3>Statistics</h3>
<dl>
<dt><code>-c</code></p>
<dd> <code>&#8211;summary-only</code> Count time, calls, and errors for each system call and report a summary on program exit, suppressing the regular output. This attempts to show system time (CPU time spent running in the kernel) independent of wall clock time. If <code>-c</code> is used with <code>-f</code>, only aggregate totals for all traced processes are kept.</p>
<dt><code>-C</code></p>
<dd> <code>&#8211;summary</code> Like <code>-c</code> but also print regular output while processes are running.</p>
<dt><code>-O </code><i>overhead</i></p>
<dd> <code>&#8211;summary-syscall-overhead</code>=<i>overhead</i> Set the overhead for tracing system calls to <i>overhead</i>. This is useful for overriding the default heuristic for guessing how much time is spent in mere measuring when timing system calls using the <code>-c</code> option. The accuracy of the heuristic can be gauged by timing a given program run without tracing (using <code><a href="/docs/linux/man/1-time/">time</a></code>(1)) and comparing the accumulated system call time to the total produced using <code>-c</code>.</p>
<dt>
<dd> The format of <i>overhead</i> specification is described in section <i>Time specification format description.</i></p>
<dt><code>-S </code><i>sortby</i></p>
<dd> <code>&#8211;summary-sort-by</code>=<i>sortby</i> Sort the output of the histogram printed by the <code>-c</code> option by the specified criterion. Legal values are <code>time</code> (or <code>time-percent</code> or <code>time-total</code> or <code>total-time</code>), <code>min-time</code> (or <code>shortest</code> or <code>time-min</code>), <code>max-time</code> (or <code>longest</code> or <code>time-max</code>), <code>avg-time</code> (or <code>time-avg</code>), <code>calls</code> (or <code>count</code>), <code>errors</code> (or <code>error</code>), <code>name</code> (or <code>syscall</code> or <code>syscall-name</code>), and <code>nothing</code> (or <code>none</code>); default is <code>time</code>.</p>
<dt><code>-U </code><i>columns</i></p>
<dd> <code>&#8211;summary-columns</code>=<i>columns</i> Configure a set (and order) of columns being shown in the call summary. The <i>columns</i> argument is a comma-separated list with items being one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>time-percent</code> (or <code>time</code>)</p>
<dd> Percentage of cumulative time consumed by a specific system call. <code>total-time</code> (or <code>time-total</code>) Total system (or wall clock, if <code>-w</code> option is provided) time consumed by a specific system call. <code>min-time</code> (or <code>shortest</code> or <code>time-min</code>) Minimum observed call duration. <code>max-time</code> (or <code>longest</code> or <code>time-max</code>) Maximum observed call duration. <code>avg-time</code> (or <code>time-avg</code>) Average call duration. <code>calls</code> (or <code>count</code>) Call count. <code>errors</code> (or <code>error</code>) Error count. <code>name</code> (or <code>syscall</code> or <code>syscall-name</code>) Syscall name.</dl>
</dl>
<dt>
<dd> The default value is <code>time-percent</code>,<code>total-time</code>,<code>avg-time</code>,<code>calls</code>,<code>errors</code>,<code>name</code>. If the <code>name</code> field is not supplied explicitly, it is added as the last column.</p>
<dt><code>-w</code></p>
<dd> <code>&#8211;summary-wall-clock</code> Summarise the time difference between the beginning and end of each system call. The default is to summarise the system time.</dl>
<h3>Tampering</h3>
<dl>
<dt><code>-e inject</code>=,<i>syscall_set/</i>[:<code>error</code>=,<i>errno/</i>|:<code>retval</code>=,<i>value/</i>][:<code>signal</code>=,<i>sig/</i>][:<code>syscall</code>=,<i>syscall/</i>][:<code>delay_enter</code>=,<i>delay/</i>][:<code>delay_exit</code>=,<i>delay/</i>][:<code>poke_enter</code>=,<i>@argN=DATAN,@argM=DATAM&#8230;/</i>][:<code>poke_exit</code>=,<i>@argN=DATAN,@argM=DATAM&#8230;/</i>][:<code>when</code>=,<i>expr/</i>]</p>
<dd> <code>&#8211;inject</code>=,<i>syscall_set/</i>[:<code>error</code>=,<i>errno/</i>|:<code>retval</code>=,<i>value/</i>][:<code>signal</code>=,<i>sig/</i>][:<code>syscall</code>=,<i>syscall/</i>][:<code>delay_enter</code>=,<i>delay/</i>][:<code>delay_exit</code>=,<i>delay/</i>][:<code>poke_enter</code>=,<i>@argN=DATAN,@argM=DATAM&#8230;/</i>][:<code>poke_exit</code>=,<i>@argN=DATAN,@argM=DATAM&#8230;/</i>][:<code>when</code>=,<i>expr/</i>] Perform syscall tampering for the specified set of syscalls. The syntax of the <i>syscall_set</i> specification is the same as in the <code>-e trace</code> option.</p>
<dt>
<dd> At least one of <code>error</code>, <code>retval</code>, <code>signal</code>, <code>delay_enter</code>, <code>delay_exit</code>, <code>poke_enter</code>, or <code>poke_exit</code> options has to be specified. <code>error</code> and <code>retval</code> are mutually exclusive.</p>
<dt>
<dd> If :<code>error</code>=,<i>errno/</i> option is specified, a fault is injected into a syscall invocation: the syscall number is replaced by -1 which corresponds to an invalid syscall (unless a syscall is specified with :<code>syscall=</code> option), and the error code is specified using a symbolic <i>errno</i> value like <code>ENOSYS</code> or a numeric value within 1..4095 range.</p>
<dt>
<dd> If :<code>retval</code>=,<i>value/</i> option is specified, success injection is performed: the syscall number is replaced by -1, but a bogus success value is returned to the callee.</p>
<dt>
<dd> If :<code>signal</code>=,<i>sig/</i> option is specified with either a symbolic value like <code>SIGSEGV</code> or a numeric value within 1..<code>SIGRTMAX</code> range, that signal is delivered on entering every syscall specified by the <i>set</i>.</p>
<dt>
<dd> If :<code>delay_enter</code>=,<i>delay/</i> or :<code>delay_exit</code>=,<i>delay/</i> options are specified, delay injection is performed: the tracee is delayed by time period specified by <i>delay</i> on entering or exiting the syscall, respectively. The format of <i>delay</i> specification is described in section <i>Time specification format description.</i></p>
<dt>
<dd> If :<code>poke_enter</code>=<i>@argN=DATAN,@argM=DATAM&#8230;</i> or :<code>poke_exit</code>=<i>@argN=DATAN,@argM=DATAM&#8230;</i> options are specified, tracee&#8217;s memory at locations, pointed to by system call arguments <i>argN</i> and <i>argM</i> (going from <i>arg1</i> to <i>arg7</i>) is overwritten by data <i>DATAN</i> and <i>DATAM</i> (specified in hexadecimal format; for example :<code>poke_enter</code>=<i>@arg1=0000DEAD0000BEEF</i>). :<code>poke_enter</code> modifies memory on syscall enter, and :<code>poke_exit</code> &#8211; on exit.</p>
<dt>
<dd> If :<code>signal</code>=,<i>sig/</i> option is specified without :<code>error</code>=,<i>errno/</i>, :<code>retval</code>=,<i>value/</i> or :<code>delay_{enter,exit}</code>=,<i>usecs/</i> options, then only a signal <i>sig</i> is delivered without a syscall fault or delay injection. Conversely, :<code>error</code>=,<i>errno/</i> or :<code>retval</code>=,<i>value/</i> option without :<code>delay_enter</code>=,<i>delay/</i>, :<code>delay_exit</code>=,<i>delay/</i> or :<code>signal</code>=,<i>sig/</i> options injects a fault without delivering a signal or injecting a delay, etc.</p>
<dt>
<dd> If :<code>signal</code>=,<i>sig/</i> option is specified together with :<code>error</code>=,<i>errno/</i> or :<code>retval</code>=,<i>value/</i>, then both injection of a fault or success and signal delivery are performed.</p>
<dt>
<dd> if :<code>syscall</code>=<i>syscall</i> option is specified, the corresponding syscall with no side effects is injected instead of -1. Currently, only &quot;pure&quot; (see <code>-e trace</code>=<code>%pure</code> description) syscalls can be specified there.</p>
<dt>
<dd> Unless a :<code>when</code>=,<i>expr</i> subexpression is specified, an injection is being made into every invocation of each syscall from the <i>set</i>.</p>
<dt>
<dd> The format of the subexpression is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <i>first/</i>[<code>..</code>,<i>last/</i>][<code>+</code>[,<i>step/</i>]]</dl>
</dl>
<dt>
<dd> Number <i>first</i> stands for the first invocation number in the range, number <i>last</i> stands for the last invocation number in the range, and <i>step</i> stands for the step between two consecutive invocations. The following combinations are useful:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>first</i></p>
<dd> For every syscall from the <i>set</i>, perform an injection for the syscall invocation number <i>first</i> only. <i>first/</i><code>..</code>,<i>last</i> For every syscall from the <i>set</i>, perform an injection for the syscall invocation number <i>first</i> and all subsequent invocations until the invocation number <i>last</i> (inclusive). <i>first/</i><code>+</code> For every syscall from the <i>set</i>, perform injections for the syscall invocation number <i>first</i> and all subsequent invocations. <i>first/</i><code>..</code>,<i>last/</i><code>+</code> For every syscall from the <i>set</i>, perform injections for the syscall invocation number <i>first</i> and all subsequent invocations until the invocation number <i>last</i> (inclusive). <i>first/</i><code>+</code>,<i>step</i> For every syscall from the <i>set</i>, perform injections for syscall invocations number <i>first</i>, <i>first</i>+<i>step</i>, <i>first</i>+<i>step</i>+<i>step</i>, and so on. <i>first/</i><code>..</code>,<i>last</i><code>+</code>,<i>step</i> Same as the previous, but consider only syscall invocations with numbers up to <i>last</i> (inclusive).</dl>
</dl>
<dt>
<dd> For example, to fail each third and subsequent chdir syscalls with <code>ENOENT</code>, use <code>-e inject</code>=,<i>chdir/</i>:<code>error</code>=,<i>ENOENT/</i>:<code>when</code>=,<i>3/</i><code>+</code>.</p>
<dt>
<dd> The valid range for numbers <i>first</i> and <i>step</i> is 1..65535, and for number <i>last</i> is 1..65534.</p>
<dt>
<dd> An injection expression can contain only one <code>error</code>= or <code>retval</code>= specification, and only one <code>signal</code>= specification. If an injection expression contains multiple <code>when</code>= specifications, the last one takes precedence.</p>
<dt>
<dd> Accounting of syscalls that are subject to injection is done per syscall and per tracee.</p>
<dt>
<dd> Specification of syscall injection can be combined with other syscall filtering options, for example, <code>-P </code><i>/dev/urandom </i><code>-e inject</code>=,<i>file/</i>:<code>error</code>=,<i>ENOENT</i>.</p>
<dt><code>-e fault</code>=,<i>syscall_set/</i>[:<code>error</code>=,<i>errno/</i>][:<code>when</code>=,<i>expr/</i>]</p>
<dd> <code>&#8211;fault</code>=,<i>syscall_set/</i>[:<code>error</code>=,<i>errno/</i>][:<code>when</code>=,<i>expr/</i>] Perform syscall fault injection for the specified set of syscalls.</p>
<dt>
<dd> This is equivalent to more generic <code>-e inject</code>= expression with default value of <i>errno</i> option set to <code>ENOSYS</code>.</dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>-d</code></p>
<dd> <code>&#8211;debug</code> Show some debugging output of <code>strace</code> itself on the standard error.</p>
<dt><code>-F</code></p>
<dd> This option is deprecated. It is retained for backward compatibility only and may be removed in future releases. Usage of multiple instances of <code>-F</code> option is still equivalent to a single <code>-f</code>, and it is ignored at all if used along with one or more instances of <code>-f</code> option.</p>
<dt><code>-h</code></p>
<dd> <code>&#8211;help</code> Print the help summary.</p>
<dt><code>&#8211;seccomp-bpf</code></p>
<dd> Try to enable use of seccomp-bpf (see <code><a href="/docs/linux/man/2-seccomp/">seccomp</a></code>(2)) to have <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)-stops only when system calls that are being traced occur in the traced processes. This option has no effect unless <code>-f</code>/<code>&#8211;follow-forks</code> is also specified. <code>&#8211;seccomp-bpf</code> is also not applicable to processes attached using <code>-p</code>/<code>&#8211;attach</code> option. An attempt to enable system calls filtering using seccomp-bpf may fail for various reasons, e.g. there are too many system calls to filter, the seccomp API is not available, or <code>strace</code> itself is being traced. In cases when seccomp-bpf filter setup failed, <code>strace</code> proceeds as usual and stops traced processes on every system call.</p>
<dt><code>-V</code></p>
<dd> <code>&#8211;version</code> Print the version number of <code>strace</code>.</dl>
<h3>Time specification format description</h3>
<p> Time values can be specified as a decimal floating point number (in a format accepted by <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3)), optionally followed by one of the following suffices that specify the unit of time: <code>s</code> (seconds), <code>ms</code> (milliseconds), <code>us</code> (microseconds), or <code>ns</code> (nanoseconds). If no suffix is specified, the value is interpreted as microseconds. </p>
<p> The described format is used for <code>-O</code>, <code>-e inject</code>=<code>delay_enter</code>, and <code>-e inject</code>=<code>delay_exit</code> options.</p>
<h2>DIAGNOSTICS</h2>
<p> When <i>command</i> exits, <code>strace</code> exits with the same exit status. If <i>command</i> is terminated by a signal, <code>strace</code> terminates itself with the same signal, so that <code>strace</code> can be used as a wrapper process transparent to the invoking parent process. Note that parent-child relationship (signal stop notifications, <code><a href="/docs/linux/man/2-getppid/">getppid</a></code>(2) value, etc) between traced process and its parent are not preserved unless <code>-D</code> is used. </p>
<p> When using <code>-p</code> without a <i>command</i>, the exit status of <code>strace</code> is zero unless no processes has been attached or there was an unexpected error in doing the tracing.</p>
<h2>SETUID INSTALLATION</h2>
<p> If <code>strace</code> is installed setuid to root then the invoking user will be able to attach to and trace processes owned by any user. In addition setuid and setgid programs will be executed and traced with the correct effective privileges. Since only users trusted with full root privileges should be allowed to do these things, it only makes sense to install <code>strace</code> as setuid to root when the users who can execute it are restricted to those users who have this trust. For example, it makes sense to install a special version of <code>strace</code> with mode &#8216;rwsr-xr&#8211;&#8216;, user <code>root</code> and group <code>trace</code>, where members of the <code>trace</code> group are trusted users. If you do use this feature, please remember to install a regular non-setuid version of <code>strace</code> for ordinary users to use.</p>
<h2>MULTIPLE PERSONALITIES SUPPORT</h2>
<p> On some architectures, <code>strace</code> supports decoding of syscalls for processes that use different ABI rather than the one <code>strace</code> uses. Specifically, in addition to decoding native ABI, <code>strace</code> can decode the following ABIs on the following architectures: </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Architecture</code></td>
<td><code>ABIs supported</code>
</td>
</tr>
<tr VALIGN=top>
<td>x86_64</td>
<td>i386, x32 [1]; i386 [2]
</td>
</tr>
<tr VALIGN=top>
<td>AArch64</td>
<td>ARM 32-bit EABI
</td>
</tr>
<tr VALIGN=top>
<td>PowerPC 64-bit [3]</td>
<td>PowerPC 32-bit
</td>
</tr>
<tr VALIGN=top>
<td>s390x</td>
<td>s390
</td>
</tr>
<tr VALIGN=top>
<td>SPARC 64-bit</td>
<td>SPARC 32-bit
</td>
</tr>
<tr VALIGN=top>
<td>TILE 64-bit</td>
<td>TILE 32-bit
</td>
</tr>
</table>
<dl>
<dt>
<dd>
<dl>
<dt>[1]</p>
<dd> When <code>strace</code> is built as an x86_64 application [2] When <code>strace</code> is built as an x32 application [3] Big endian only</dl>
</dl>
<p> This support is optional and relies on ability to generate and parse structure definitions during the build time. Please refer to the output of the <code>strace -V</code> command in order to figure out what support is available in your <code>strace</code> build (&quot;non-native&quot; refers to an ABI that differs from the ABI <code>strace</code> has):</p>
<dl>
<dt><code>m32-mpers</code></p>
<dd> <code>strace</code> can trace and properly decode non-native 32-bit binaries. <code>no-m32-mpers</code> <code>strace</code> can trace, but cannot properly decode non-native 32-bit binaries. <code>mx32-mpers</code> <code>strace</code> can trace and properly decode non-native 32-on-64-bit binaries. <code>no-mx32-mpers</code> <code>strace</code> can trace, but cannot properly decode non-native 32-on-64-bit binaries.</dl>
<p> If the output contains neither <code>m32-mpers</code> nor <code>no-m32-mpers</code>, then decoding of non-native 32-bit binaries is not implemented at all or not applicable. </p>
<p> Likewise, if the output contains neither <code>mx32-mpers</code> nor <code>no-mx32-mpers</code>, then decoding of non-native 32-on-64-bit binaries is not implemented at all or not applicable.</p>
<h2>NOTES</h2>
<p> It is a pity that so much tracing clutter is produced by systems employing shared libraries. </p>
<p> It is instructive to think about system call inputs and outputs as data-flow across the user/kernel boundary. Because user-space and kernel-space are separate and address-protected, it is sometimes possible to make deductive inferences about process behavior using inputs and outputs as propositions. </p>
<p> In some cases, a system call will differ from the documented behavior or have a different name. For example, the <code><a href="/docs/linux/man/2-faccessat/">faccessat</a></code>(2) system call does not have <i>flags</i> argument, and the <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2) library function uses <code><a href="/docs/linux/man/2-prlimit64/">prlimit64</a></code>(2) system call on modern (2.6.38+) kernels. These discrepancies are normal but idiosyncratic characteristics of the system call interface and are accounted for by C library wrapper functions. </p>
<p> Some system calls have different names in different architectures and personalities. In these cases, system call filtering and printing uses the names that match corresponding <code>__NR_</code>* kernel macros of the tracee&#8217;s architecture and personality. There are two exceptions from this general rule: <code><a href="/docs/linux/man/2-arm_fadvise64_64/">arm_fadvise64_64</a></code>(2) ARM syscall and <code><a href="/docs/linux/man/2-xtensa_fadvise64_64/">xtensa_fadvise64_64</a></code>(2) Xtensa syscall are filtered and printed as <code><a href="/docs/linux/man/2-fadvise64_64/">fadvise64_64</a></code>(2). </p>
<p> On x32, syscalls that are intended to be used by 64-bit processes and not x32 ones (for example, <code><a href="/docs/linux/man/2-readv/">readv</a></code>(2), that has syscall number 19 on x86_64, with its x32 counterpart has syscall number 515), but called with <code>__X32_SYSCALL_BIT</code> flag being set, are designated with <code>#64</code> suffix. </p>
<p> On some platforms a process that is attached to with the <code>-p</code> option may observe a spurious <code>EINTR</code> return from the current system call that is not restartable. (Ideally, all system calls should be restarted on <code>strace</code> attach, making the attach invisible to the traced process, but a few system calls aren&#8217;t. Arguably, every instance of such behavior is a kernel bug.) This may have an unpredictable effect on the process if the process takes no action to restart the system call. </p>
<p> As <code>strace</code> executes the specified <i>command</i> directly and does not employ a shell for that, scripts without shebang that usually run just fine when invoked by shell fail to execute with <code>ENOEXEC</code> error. It is advisable to manually supply a shell as a <i>command</i> with the script as its argument.</p>
<h2>BUGS</h2>
<p> Programs that use the <i>setuid</i> bit do not have effective user <font SIZE="-1">ID</font> privileges while being traced. </p>
<p> A traced process runs slowly (but check out the <code>&#8211;seccomp-bpf</code> option). </p>
<p> Traced processes which are descended from <i>command</i> may be left running after an interrupt signal (<code>CTRL-C</code>).</p>
<h2>HISTORY</h2>
<p> The original <code>strace</code> was written by Paul Kranenburg for SunOS and was inspired by its <code>trace</code> utility. The SunOS version of <code>strace</code> was ported to Linux and enhanced by Branko Lankester, who also wrote the Linux kernel support. Even though Paul released <code>strace</code> 2.5 in 1992, Branko&#8217;s work was based on Paul&#8217;s <code>strace</code> 1.5 release from 1991. In 1993, Rick Sladkey merged <code>strace</code> 2.5 for SunOS and the second release of <code>strace</code> for Linux, added many of the features of <code><a href="/docs/linux/man/1-truss/">truss</a></code>(1) from SVR4, and produced an <code>strace</code> that worked on both platforms. In 1994 Rick ported <code>strace</code> to SVR4 and Solaris and wrote the automatic configuration support. In 1995 he ported <code>strace</code> to Irix and tired of writing about himself in the third person. </p>
<p> Beginning with 1996, <code>strace</code> was maintained by Wichert Akkerman. During his tenure, <code>strace</code> development migrated to CVS; ports to FreeBSD and many architectures on Linux (including ARM, IA-64, MIPS, PA-RISC, PowerPC, s390, SPARC) were introduced. In 2002, the burden of <code>strace</code> maintainership was transferred to Roland McGrath. Since then, <code>strace</code> gained support for several new Linux architectures (AMD64, s390x, SuperH), bi-architecture support for some of them, and received numerous additions and improvements in syscalls decoders on Linux; <code>strace</code> development migrated to <code>git</code> during that period. Since 2009, <code>strace</code> is actively maintained by Dmitry Levin. <code>strace</code> gained support for AArch64, ARC, AVR32, Blackfin, Meta, Nios II, OpenRISC 1000, RISC-V, Tile/TileGx, Xtensa architectures since that time. In 2012, unmaintained and apparently broken support for non-Linux operating systems was removed. Also, in 2012 <code>strace</code> gained support for path tracing and file descriptor path decoding. In 2014, support for stack traces printing was added. In 2016, syscall fault injection was implemented. </p>
<p> For the additional information, please refer to the <code>NEWS</code> file and <code>strace</code> repository commit log.</p>
<h2>REPORTING BUGS</h2>
<p> Problems with <code>strace</code> should be reported to the <code>strace</code> mailing list</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-strace-log-merge/">strace-log-merge</a></code>(1), <code><a href="/docs/linux/man/1-ltrace/">ltrace</a></code>(1), <code><a href="/docs/linux/man/1-perf-trace/">perf-trace</a></code>(1), <code><a href="/docs/linux/man/1-trace-cmd/">trace-cmd</a></code>(1), <code><a href="/docs/linux/man/1-time/">time</a></code>(1), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) </p>
<p> <code>strace</code> Home Page</p>
<h2>AUTHORS</h2>
<p> The complete list of <code>strace</code> contributors can be found in the <code>CREDITS</code> file. </p>
<h2>Index</h2>
