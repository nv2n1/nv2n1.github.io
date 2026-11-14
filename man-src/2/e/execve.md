---
title: "execve(2)"
name: "execve"
section: "2"
letter: "e"
url: "/docs/linux/man/2-execve/"
description: "execve – execute program"
---

<h2 class="name">NAME</h2>
<p> execve &#8211; execute program </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int execve(const char *</code><i>pathname</i><code>, char *const </code><i>argv</i><code>[],</code><br />
 <code> char *const </code><i>envp</i><code>[]);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>execve</code>() executes the program referred to by <i>pathname</i>. This causes the program that is currently being run by the calling process to be replaced with a new program, with newly initialized stack, heap, and (initialized and uninitialized) data segments. </p>
<p> <i>pathname</i> must be either a binary executable, or a script starting with a line of the form: </p>
<p> <code>#!</code><i>interpreter </i>[optional-arg] </p>
<p> For details of the latter case, see &quot;Interpreter scripts&quot; below. </p>
<p> <i>argv</i> is an array of pointers to strings passed to the new program as its command-line arguments. By convention, the first of these strings (i.e., <i>argv[0]</i>) should contain the filename associated with the file being executed. The <i>argv</i> array must be terminated by a NULL pointer. (Thus, in the new program, <i>argv[argc]</i> will be NULL.) </p>
<p> <i>envp</i> is an array of pointers to strings, conventionally of the form <code>key=value</code>, which are passed as the environment of the new program. The <i>envp</i> array must be terminated by a NULL pointer. </p>
<p> The argument vector and environment can be accessed by the new program&#8217;s main function, when it is defined as: </p>
<p> int main(int argc, char *argv[], char *envp[]) </p>
<p> Note, however, that the use of a third argument to the main function is not specified in POSIX.1; according to POSIX.1, the environment should be accessed via the external variable <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). </p>
<p> <code>execve</code>() does not return on success, and the text, initialized data, uninitialized data (bss), and stack of the calling process are overwritten according to the contents of the newly loaded program. </p>
<p> If the current program is being ptraced, a <code>SIGTRAP</code> signal is sent to it after a successful <code>execve</code>(). </p>
<p> If the set-user-ID bit is set on the program file referred to by <i>pathname</i>, then the effective user ID of the calling process is changed to that of the owner of the program file. Similarly, if the set-group-ID bit is set on the program file, then the effective group ID of the calling process is set to the group of the program file. </p>
<p> The aforementioned transformations of the effective IDs are <i>not</i> performed (i.e., the set-user-ID and set-group-ID bits are ignored) if any of the following is true:</p>
<dl>
<dt>*</p>
<dd> the <i>no_new_privs</i> attribute is set for the calling thread (see <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2));</p>
<dt>*</p>
<dd> the underlying filesystem is mounted <i>nosuid</i> (the <code>MS_NOSUID</code> flag for <code><a href="/docs/linux/man/2-mount/">mount</a></code>(2)); or</p>
<dt>*</p>
<dd> the calling process is being ptraced.</dl>
<p> The capabilities of the program file (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)) are also ignored if any of the above are true. </p>
<p> The effective user ID of the process is copied to the saved set-user-ID; similarly, the effective group ID is copied to the saved set-group-ID. This copying takes place after any effective ID changes that occur because of the set-user-ID and set-group-ID mode bits. </p>
<p> The process&#8217;s real UID and real GID, as well its supplementary group IDs, are unchanged by a call to <code>execve</code>(). </p>
<p> If the executable is an a.out dynamically linked binary executable containing shared-library stubs, the Linux dynamic linker <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) is called at the start of execution to bring needed shared objects into memory and link the executable with them. </p>
<p> If the executable is a dynamically linked ELF executable, the interpreter named in the PT_INTERP segment is used to load the needed shared objects. This interpreter is typically <i>/lib/ld-linux.so.2</i> for binaries linked with glibc (see <code><a href="/docs/linux/man/8-ld-linux-so/">ld-linux.so</a></code>(8)).</p>
<h3>Effect on process attributes</h3>
<p> All process attributes are preserved during an <code>execve</code>(), except the following:</p>
<dl>
<dt>*</p>
<dd> The dispositions of any signals that are being caught are reset to the default (<code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)).</p>
<dt>*</p>
<dd> Any alternate signal stack is not preserved (<code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)).</p>
<dt>*</p>
<dd> Memory mappings are not preserved (<code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)).</p>
<dt>*</p>
<dd> Attached System V shared memory segments are detached (<code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2)).</p>
<dt>*</p>
<dd> POSIX shared memory regions are unmapped (<code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3)).</p>
<dt>*</p>
<dd> Open POSIX message queue descriptors are closed (<code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)).</p>
<dt>*</p>
<dd> Any open POSIX named semaphores are closed (<code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)).</p>
<dt>*</p>
<dd> POSIX timers are not preserved (<code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2)).</p>
<dt>*</p>
<dd> Any open directory streams are closed (<code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3)).</p>
<dt>*</p>
<dd> Memory locks are not preserved (<code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2)).</p>
<dt>*</p>
<dd> Exit handlers are not preserved (<code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3), <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3)).</p>
<dt>*</p>
<dd> The floating-point environment is reset to the default (see <code><a href="/docs/linux/man/3-fenv/">fenv</a></code>(3)).</dl>
<p> The process attributes in the preceding list are all specified in POSIX.1. The following Linux-specific process attributes are also not preserved during an <code>execve</code>():</p>
<dl>
<dt>*</p>
<dd> The process&#8217;s &quot;dumpable&quot; attribute is set to the value 1, unless a set-user-ID program, a set-group-ID program, or a program with capabilities is being executed, in which case the dumpable flag may instead be reset to the value in <i>/proc/sys/fs/suid_dumpable</i>, in the circumstances described under <code>PR_SET_DUMPABLE</code> in <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2). Note that changes to the &quot;dumpable&quot; attribute may cause ownership of files in the process&#8217;s <i>/proc/[pid]</i> directory to change to <i>root:root</i>, as described in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
<dt>*</p>
<dd> The <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_KEEPCAPS</code> flag is cleared.</p>
<dt>*</p>
<dd> (Since Linux 2.4.36 / 2.6.23) If a set-user-ID or set-group-ID program is being executed, then the parent death signal set by <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_PDEATHSIG</code> flag is cleared.</p>
<dt>*</p>
<dd> The process name, as set by <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_NAME</code> (and displayed by <i>ps -o comm</i>), is reset to the name of the new executable file.</p>
<dt>*</p>
<dd> The <code>SECBIT_KEEP_CAPS</code> <i>securebits</i> flag is cleared. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).</p>
<dt>*</p>
<dd> The termination signal is reset to <code>SIGCHLD</code> (see <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2)).</p>
<dt>*</p>
<dd> The file descriptor table is unshared, undoing the effect of the <code>CLONE_FILES</code> flag of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2).</dl>
<p> Note the following further points:</p>
<dl>
<dt>*</p>
<dd> All threads other than the calling thread are destroyed during an <code>execve</code>(). Mutexes, condition variables, and other pthreads objects are not preserved.</p>
<dt>*</p>
<dd> The equivalent of <i>setlocale(LC_ALL, &quot;C&quot;)</i> is executed at program start-up.</p>
<dt>*</p>
<dd> POSIX.1 specifies that the dispositions of any signals that are ignored or set to the default are left unchanged. POSIX.1 specifies one exception: if <code>SIGCHLD</code> is being ignored, then an implementation may leave the disposition unchanged or reset it to the default; Linux does the former.</p>
<dt>*</p>
<dd> Any outstanding asynchronous I/O operations are canceled (<code><a href="/docs/linux/man/3-aio_read/">aio_read</a></code>(3), <code><a href="/docs/linux/man/3-aio_write/">aio_write</a></code>(3)).</p>
<dt>*</p>
<dd> For the handling of capabilities during <code>execve</code>(), see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).</p>
<dt>*</p>
<dd> By default, file descriptors remain open across an <code>execve</code>(). File descriptors that are marked close-on-exec are closed; see the description of <code>FD_CLOEXEC</code> in <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2). (If a file descriptor is closed, this will cause the release of all record locks obtained on the underlying file by this process. See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for details.) POSIX.1 says that if file descriptors 0, 1, and 2 would otherwise be closed after a successful <code>execve</code>(), and the process would gain privilege because the set-user-ID or set-group-ID mode bit was set on the executed file, then the system may open an unspecified file for each of these file descriptors. As a general principle, no portable program, whether privileged or not, can assume that these three file descriptors will remain closed across an <code>execve</code>().</dl>
<h3>Interpreter scripts</h3>
<p> An interpreter script is a text file that has execute permission enabled and whose first line is of the form: </p>
<p> <code>#!</code><i>interpreter </i>[optional-arg] </p>
<p> The <i>interpreter</i> must be a valid pathname for an executable file. </p>
<p> If the <i>pathname</i> argument of <code>execve</code>() specifies an interpreter script, then <i>interpreter</i> will be invoked with the following arguments: </p>
<p> <i>interpreter</i> [optional-arg] <i>pathname</i> arg&#8230; </p>
<p> where <i>pathname</i> is the absolute pathname of the file specified as the first argument of <code>execve</code>(), and <i>arg&#8230;</i> is the series of words pointed to by the <i>argv</i> argument of <code>execve</code>(), starting at <i>argv[1]</i>. Note that there is no way to get the <i>argv[0]</i> that was passed to the <code>execve</code>() call. </p>
<p> For portable use, <i>optional-arg</i> should either be absent, or be specified as a single word (i.e., it should not contain white space); see NOTES below. </p>
<p> Since Linux 2.6.28, the kernel permits the interpreter of a script to itself be a script. This permission is recursive, up to a limit of four recursions, so that the interpreter may be a script which is interpreted by a script, and so on.</p>
<h3>Limits on size of arguments and environment</h3>
<p> Most UNIX implementations impose some limit on the total size of the command-line argument (<i>argv</i>) and environment (<i>envp</i>) strings that may be passed to a new program. POSIX.1 allows an implementation to advertise this limit using the <code>ARG_MAX</code> constant (either defined in <i>&lt;limits.h&gt;</i> or available at run time using the call <i>sysconf(_SC_ARG_MAX)</i>). </p>
<p> On Linux prior to kernel 2.6.23, the memory used to store the environment and argument strings was limited to 32 pages (defined by the kernel constant <code>MAX_ARG_PAGES</code>). On architectures with a 4-kB page size, this yields a maximum size of 128 kB. </p>
<p> On kernel 2.6.23 and later, most architectures support a size limit derived from the soft <code>RLIMIT_STACK</code> resource limit (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)) that is in force at the time of the <code>execve</code>() call. (Architectures with no memory management unit are excepted: they maintain the limit that was in effect before kernel 2.6.23.) This change allows programs to have a much larger argument and/or environment list. For these architectures, the total size is limited to 1/4 of the allowed stack size. (Imposing the 1/4-limit ensures that the new program always has some stack space.) Additionally, the total size is limited to 3/4 of the value of the kernel constant <code>_STK_LIM</code> (8 Mibibytes). Since Linux 2.6.25, the kernel also places a floor of 32 pages on this size limit, so that, even when <code>RLIMIT_STACK</code> is set very low, applications are guaranteed to have at least as much argument and environment space as was provided by Linux 2.6.23 and earlier. (This guarantee was not provided in Linux 2.6.23 and 2.6.24.) Additionally, the limit per string is 32 pages (the kernel constant <code>MAX_ARG_STRLEN</code>), and the maximum number of strings is 0x7FFFFFFF.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>execve</code>() does not return, on error -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>E2BIG</code></p>
<dd> The total number of bytes in the environment (<i>envp</i>) and argument list (<i>argv</i>) is too large.</p>
<dt><code>EACCES</code></p>
<dd> Search permission is denied on a component of the path prefix of <i>pathname</i> or the name of a script interpreter. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EACCES</code></p>
<dd> The file or a script interpreter is not a regular file.</p>
<dt><code>EACCES</code></p>
<dd> Execute permission is denied for the file or a script or ELF interpreter.</p>
<dt><code>EACCES</code></p>
<dd> The filesystem is mounted <i>noexec</i>.</p>
<dt><code>EAGAIN</code> (since Linux 3.1)</p>
<dd> Having changed its real UID using one of the <code>set*uid</code>() calls, the caller was&#8212;and is now still&#8212;above its <code>RLIMIT_NPROC</code> resource limit (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)). For a more detailed explanation of this error, see NOTES.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> or one of the pointers in the vectors <i>argv</i> or <i>envp</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> An ELF executable had more than one PT_INTERP segment (i.e., tried to name more than one interpreter).</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>EISDIR</code></p>
<dd> An ELF interpreter was a directory.</p>
<dt><code>ELIBBAD</code></p>
<dd> An ELF interpreter was not in a recognized format.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i> or the name of a script or ELF interpreter.</p>
<dt><code>ELOOP</code></p>
<dd> The maximum recursion limit was reached during recursive script interpretation (see &quot;Interpreter scripts&quot;, above). Before Linux 3.8, the error produced for this case was <code>ENOEXEC</code>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd> The file <i>pathname</i> or a script or ELF interpreter does not exist.</p>
<dt><code>ENOEXEC</code></p>
<dd> An executable is not in a recognized format, is for the wrong architecture, or has some other format error that means it cannot be executed.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of the path prefix of <i>pathname</i> or a script or ELF interpreter is not a directory.</p>
<dt><code>EPERM</code></p>
<dd> The filesystem is mounted <i>nosuid</i>, the user is not the superuser, and the file has the set-user-ID or set-group-ID bit set.</p>
<dt><code>EPERM</code></p>
<dd> The process is being traced, the user is not the superuser and the file has the set-user-ID or set-group-ID bit set.</p>
<dt><code>EPERM</code></p>
<dd> A &quot;capability-dumb&quot; applications would not obtain the full set of permitted capabilities granted by the executable file. See <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7).</p>
<dt><code>ETXTBSY</code></p>
<dd> The specified executable was open for writing by one or more processes.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. POSIX does not document the #! behavior, but it exists (with some variations) on other UNIX systems.</p>
<h2>NOTES</h2>
<p> One sometimes sees <code>execve</code>() (and the related functions described in <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3)) described as &quot;executing a <i>new</i> process&quot; (or similar). This is a highly misleading description: there is no new process; many attributes of the calling process remain unchanged (in particular, its PID). All that <code>execve</code>() does is arrange for an existing process (the calling process) to execute a new program. </p>
<p> Set-user-ID and set-group-ID processes can not be <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2)d. </p>
<p> The result of mounting a filesystem <i>nosuid</i> varies across Linux kernel versions: some will refuse execution of set-user-ID and set-group-ID executables when this would give the user powers they did not have already (and return <code>EPERM</code>), some will just ignore the set-user-ID and set-group-ID bits and <code>exec</code>() successfully. </p>
<p> On Linux, <i>argv</i> and <i>envp</i> can be specified as NULL. In both cases, this has the same effect as specifying the argument as a pointer to a list containing a single null pointer. <code>Do not take advantage of this nonstandard and nonportable misfeature!</code> On many other UNIX systems, specifying <i>argv</i> as NULL will result in an error (<code>EFAULT</code>). <i>Some</i> other UNIX systems treat the <i>envp==NULL</i> case the same as Linux. </p>
<p> POSIX.1 says that values returned by <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3) should be invariant over the lifetime of a process. However, since Linux 2.6.23, if the <code>RLIMIT_STACK</code> resource limit changes, then the value reported by <code>_SC_ARG_MAX</code> will also change, to reflect the fact that the limit on space for holding command-line arguments and environment variables has changed. </p>
<p> In most cases where <code>execve</code>() fails, control returns to the original executable image, and the caller of <code>execve</code>() can then handle the error. However, in (rare) cases (typically caused by resource exhaustion), failure may occur past the point of no return: the original executable image has been torn down, but the new image could not be completely built. In such cases, the kernel kills the process with a <code>SIGSEGV</code> (<code>SIGKILL</code> until Linux 3.17) signal.</p>
<h3>Interpreter scripts</h3>
<p> The kernel imposes a maximum length on the text that follows the &quot;#!&quot; characters at the start of a script; characters beyond the limit are ignored. Before Linux 5.1, the limit is 127 characters. Since Linux 5.1, the limit is 255 characters. </p>
<p> The semantics of the <i>optional-arg</i> argument of an interpreter script vary across implementations. On Linux, the entire string following the <i>interpreter</i> name is passed as a single argument to the interpreter, and this string can include white space. However, behavior differs on some other systems. Some systems use the first white space to terminate <i>optional-arg</i>. On some systems, an interpreter script can have multiple arguments, and white spaces in <i>optional-arg</i> are used to delimit the arguments. </p>
<p> Linux (like most other modern UNIX systems) ignores the set-user-ID and set-group-ID bits on scripts.</p>
<h3>execve() and EAGAIN</h3>
<p> A more detailed explanation of the <code>EAGAIN</code> error that can occur (since Linux 3.1) when calling <code>execve</code>() is as follows. </p>
<p> The <code>EAGAIN</code> error can occur when a <i>preceding</i> call to <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2), <code><a href="/docs/linux/man/2-setreuid/">setreuid</a></code>(2), or <code><a href="/docs/linux/man/2-setresuid/">setresuid</a></code>(2) caused the real user ID of the process to change, and that change caused the process to exceed its <code>RLIMIT_NPROC</code> resource limit (i.e., the number of processes belonging to the new real UID exceeds the resource limit). From Linux 2.6.0 to 3.0, this caused the <code>set*uid</code>() call to fail. (Prior to 2.6, the resource limit was not imposed on processes that changed their user IDs.) </p>
<p> Since Linux 3.1, the scenario just described no longer causes the <code>set*uid</code>() call to fail, because it too often led to security holes where buggy applications didn&#8217;t check the return status and assumed that&#8212;if the caller had root privileges&#8212;the call would always succeed. Instead, the <code>set*uid</code>() calls now successfully change the real UID, but the kernel sets an internal flag, named <code>PF_NPROC_EXCEEDED</code>, to note that the <code>RLIMIT_NPROC</code> resource limit has been exceeded. If the <code>PF_NPROC_EXCEEDED</code> flag is set and the resource limit is still exceeded at the time of a subsequent <code>execve</code>() call, that call fails with the error <code>EAGAIN</code>. This kernel logic ensures that the <code>RLIMIT_NPROC</code> resource limit is still enforced for the common privileged daemon workflow&#8212;namely, <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) + <code>set*uid</code>() + <code>execve</code>(). </p>
<p> If the resource limit was not still exceeded at the time of the <code>execve</code>() call (because other processes belonging to this real UID terminated between the <code>set*uid</code>() call and the <code>execve</code>() call), then the <code>execve</code>() call succeeds and the kernel clears the <code>PF_NPROC_EXCEEDED</code> process flag. The flag is also cleared if a subsequent call to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) by this process succeeds.</p>
<h3>Historical</h3>
<p> With UNIX V6, the argument list of an <code>exec</code>() call was ended by 0, while the argument list of <i>main</i> was ended by -1. Thus, this argument list was not directly usable in a further <code>exec</code>() call. Since UNIX V7, both are NULL.</p>
<h2>EXAMPLES</h2>
<p> The following program is designed to be execed by the second program below. It just echoes its command-line arguments, one per line. </p>
<p> /* myecho.c */ </p>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;argc;&nbsp;j++)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;argv[%d]:&nbsp;%s
&quot;, j, argv[j]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); } </p>
<p> This program can be used to exec the program named in its command-line argument: </p>
<p> /* execve.c */ </p>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*newargv[]&nbsp;=&nbsp;{&nbsp;NULL,&nbsp;&quot;hello&quot;,&nbsp;&quot;world&quot;, NULL&nbsp;};<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*newenviron[]&nbsp;=&nbsp;{&nbsp;NULL&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;file-to-exec&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;newargv[0]&nbsp;=&nbsp;argv[1]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execve(argv[1], newargv, newenviron);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;execve&quot;);&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;execve()&nbsp;returns only on error&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> We can use the second program to exec the first as follows: </p>
<p> $<code> cc myecho.c -o myecho</code> $<code> cc execve.c -o execve</code> $<code> ./execve ./myecho</code> argv[0]: ./myecho argv[1]: hello argv[2]: world </p>
<p> We can also use these programs to demonstrate the use of a script interpreter. To do this we create a script whose &quot;interpreter&quot; is our <i>myecho</i> program: </p>
<p> $<code> cat &gt; script</code> <code>#!./myecho script-arg</code> <code>haD</code> $<code> chmod +x script</code> </p>
<p> We can then use our program to exec the script: </p>
<p> $<code> ./execve ./script</code> argv[0]: ./myecho argv[1]: script-arg argv[2]: ./script argv[3]: hello argv[4]: world</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-ptrace/">ptrace</a></code>(2), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3), <code><a href="/docs/linux/man/3-getopt/">getopt</a></code>(3), <code><a href="/docs/linux/man/3-system/">system</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
