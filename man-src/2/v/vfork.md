---
title: "vfork(2)"
name: "vfork"
section: "2"
letter: "v"
url: "/docs/linux/man/2-vfork/"
description: "vfork – create a child process and block parent"
---

<h2 class="name">NAME</h2>
<p> vfork &#8211; create a child process and block parent </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>pid_t vfork(void);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>vfork</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
<pre><code>
(_XOPEN_SOURCE &amp;nbsp; &gt;= &amp;nbsp; 500) &amp;&amp; !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200809L) || /* Since glibc 2.19: */ _DEFAULT_SOURCE
    || /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<h3>Standard description</h3>
<p> (From POSIX.1) The <code>vfork</code>() function has the same effect as <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), except that the behavior is undefined if the process created by <code>vfork</code>() either modifies any data other than a variable of type <i>pid_t</i> used to store the return value from <code>vfork</code>(), or returns from the function in which <code>vfork</code>() was called, or calls any other function before successfully calling <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) or one of the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) family of functions.</p>
<h3>Linux description</h3>
<p> <code>vfork</code>(), just like <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), creates a child process of the calling process. For details and return value and errors, see <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> <code>vfork</code>() is a special case of <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2). It is used to create new processes without copying the page tables of the parent process. It may be useful in performance-sensitive applications where a child is created which then immediately issues an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> <code>vfork</code>() differs from <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) in that the calling thread is suspended until the child terminates (either normally, by calling <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), or abnormally, after delivery of a fatal signal), or it makes a call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). Until that point, the child shares all memory with its parent, including the stack. The child must not return from the current function or call <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) (which would have the effect of calling exit handlers established by the parent process and flushing the parent&#8217;s <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) buffers), but may call <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2). </p>
<p> As with <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the child process created by <code>vfork</code>() inherits copies of various of the caller&#8217;s process attributes (e.g., file descriptors, signal dispositions, and current working directory); the <code>vfork</code>() call differs only in the treatment of the virtual address space, as described above. </p>
<p> Signals sent to the parent arrive after the child releases the parent&#8217;s memory (i.e., after the child terminates or calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)).</p>
<h3>Historic description</h3>
<p> Under Linux, <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) is implemented using copy-on-write pages, so the only penalty incurred by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) is the time and memory required to duplicate the parent&#8217;s page tables, and to create a unique task structure for the child. However, in the bad old days a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) would require making a complete copy of the caller&#8217;s data space, often needlessly, since usually immediately afterward an <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) is done. Thus, for greater efficiency, BSD introduced the <code>vfork</code>() system call, which did not fully copy the address space of the parent process, but borrowed the parent&#8217;s memory and thread of control until a call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) or an exit occurred. The parent process was suspended while the child was using its resources. The use of <code>vfork</code>() was tricky: for example, not modifying data in the parent process depended on knowing which variables were held in a register.</p>
<h2>CONFORMING TO</h2>
<p> 4.3BSD; POSIX.1-2001 (but marked OBSOLETE). POSIX.1-2008 removes the specification of <code>vfork</code>(). </p>
<p> The requirements put on <code>vfork</code>() by the standards are weaker than those put on <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), so an implementation where the two are synonymous is compliant. In particular, the programmer cannot rely on the parent remaining blocked until the child either terminates or calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), and cannot rely on any specific behavior with respect to shared memory.</p>
<h2>NOTES</h2>
<p> Some consider the semantics of <code>vfork</code>() to be an architectural blemish, and the 4.2BSD man page stated: &quot;This system call will be eliminated when proper system sharing mechanisms are implemented. Users should not depend on the memory sharing semantics of <code>vfork</code>() as it will, in that case, be made synonymous to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).&quot; However, even though modern memory management hardware has decreased the performance difference between <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code>vfork</code>(), there are various reasons why Linux and other systems have retained <code>vfork</code>():</p>
<dl>
<dt>*</p>
<dd> Some performance-critical applications require the small performance advantage conferred by <code>vfork</code>().</p>
<dt>*</p>
<dd> <code>vfork</code>() can be implemented on systems that lack a memory-management unit (MMU), but <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) can&#8217;t be implemented on such systems. (POSIX.1-2008 removed <code>vfork</code>() from the standard; the POSIX rationale for the <code><a href="/docs/linux/man/3-posix_spawn/">posix_spawn</a></code>(3) function notes that that function, which provides functionality equivalent to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)+<code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), is designed to be implementable on systems that lack an MMU.)</p>
<dt>*</p>
<dd> On systems where memory is constrained, <code>vfork</code>() avoids the need to temporarily commit memory (see the description of <i>/proc/sys/vm/overcommit_memory</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)) in order to execute a new program. (This can be especially beneficial where a large parent process wishes to execute a small helper program in a child process.) By contrast, using <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) in this scenario requires either committing an amount of memory equal to the size of the parent process (if strict overcommitting is in force) or overcommitting memory with the risk that a process is terminated by the out-of-memory (OOM) killer.</dl>
<h3>Caveats</h3>
<p> The child process should take care not to modify the memory in unintended ways, since such changes will be seen by the parent process once the child terminates or executes another program. In this regard, signal handlers can be especially problematic: if a signal handler that is invoked in the child of <code>vfork</code>() changes memory, those changes may result in an inconsistent process state from the perspective of the parent process (e.g., memory changes would be visible in the parent, but changes to the state of open file descriptors would not be visible). </p>
<p> When <code>vfork</code>() is called in a multithreaded process, only the calling thread is suspended until the child terminates or executes a new program. This means that the child is sharing an address space with other running code. This can be dangerous if another thread in the parent process changes credentials (using <code><a href="/docs/linux/man/2-setuid/">setuid</a></code>(2) or similar), since there are now two processes with different privilege levels running in the same address space. As an example of the dangers, suppose that a multithreaded program running as root creates a child using <code>vfork</code>(). After the <code>vfork</code>(), a thread in the parent process drops the process to an unprivileged user in order to run some untrusted code (e.g., perhaps via plug-in opened with <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3)). In this case, attacks are possible where the parent process uses <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) to map in code that will be executed by the privileged child process.</p>
<h3>Linux notes</h3>
<p> Fork handlers established using <code><a href="/docs/linux/man/3-pthread_atfork/">pthread_atfork</a></code>(3) are not called when a multithreaded program employing the NPTL threading library calls <code>vfork</code>(). Fork handlers are called in this case in a program using the LinuxThreads threading library. (See <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7) for a description of Linux threading libraries.) </p>
<p> A call to <code>vfork</code>() is equivalent to calling <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) with <i>flags</i> specified as: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;CLONE_VM | CLONE_VFORK | SIGCHLD</p>
<h3>History</h3>
<p> The <code>vfork</code>() system call appeared in 3.0BSD. In 4.4BSD it was made synonymous to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) but NetBSD introduced it again; see In Linux, it has been equivalent to <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) until 2.2.0-pre6 or so. Since 2.2.0-pre9 (on i386, somewhat later on other architectures) it is an independent system call. Support was added in glibc 2.0.112.</p>
<h2>BUGS</h2>
<p> Details of the signal handling are obscure and differ between systems. The BSD man page states: &quot;To avoid a possible deadlock situation, processes that are children in the middle of a <code>vfork</code>() are never sent <code>SIGTTOU</code> or <code>SIGTTIN</code> signals; rather, output or <i>ioctl</i>s are allowed and input attempts result in an end-of-file indication.&quot;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-unshare/">unshare</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
