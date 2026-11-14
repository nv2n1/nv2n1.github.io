---
title: "intro(2)"
name: "intro"
section: "2"
letter: "i"
url: "/docs/linux/man/2-intro/"
description: "intro – introduction to system calls"
---

<h2 class="name">NAME</h2>
<p> intro &#8211; introduction to system calls </p>
<h2>DESCRIPTION</h2>
<p> Section 2 of the manual describes the Linux system calls. A system call is an entry point into the Linux kernel. Usually, system calls are not invoked directly: instead, most system calls have corresponding C library wrapper functions which perform the steps required (e.g., trapping to kernel mode) in order to invoke the system call. Thus, making a system call looks the same as invoking a normal library function. </p>
<p> In many cases, the C library wrapper function does nothing more than:</p>
<dl>
<dt>*</p>
<dd> copying arguments and the unique system call number to the registers where the kernel expects them;</p>
<dt>*</p>
<dd> trapping to kernel mode, at which point the kernel does the real work of the system call;</p>
<dt>*</p>
<dd> setting <i>errno</i> if the system call returns an error number when the kernel returns the CPU to user mode.</dl>
<p> However, in a few cases, a wrapper function may do rather more than this, for example, performing some preprocessing of the arguments before trapping to kernel mode, or postprocessing of values returned by the system call. Where this is the case, the manual pages in Section 2 generally try to note the details of both the (usually GNU) C library API interface and the raw system call. Most commonly, the main DESCRIPTION will focus on the C library interface, and differences for the system call are covered in the NOTES section. </p>
<p> For a list of the Linux system calls, see <code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On error, most system calls return a negative error number (i.e., the negated value of one of the constants described in <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3)). The C library wrapper hides this detail from the caller: when a system call returns a negative value, the wrapper copies the absolute value into the <i>errno</i> variable, and returns -1 as the return value of the wrapper. </p>
<p> The value returned by a successful system call depends on the call. Many system calls return 0 on success, but some can return nonzero values from a successful call. The details are described in the individual manual pages. </p>
<p> In some cases, the programmer must define a feature test macro in order to obtain the declaration of a system call from the header file specified in the man page SYNOPSIS section. (Where required, these feature test macros must be defined before including <i>any</i> header files.) In such cases, the required macro is described in the man page. For further information on feature test macros, see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7).</p>
<h2>CONFORMING TO</h2>
<p> Certain terms and abbreviations are used to indicate UNIX variants and standards to which calls in this section conform. See <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7).</p>
<h2>NOTES</h2>
<h3>Calling directly</h3>
<p> In most cases, it is unnecessary to invoke a system call directly, but there are times when the Standard C library does not implement a nice wrapper function for you. In this case, the programmer must manually invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). Historically, this was also possible using one of the _syscall macros described in <code><a href="/docs/linux/man/2-_syscall/">_syscall</a></code>(2).</p>
<h3>Authors and copyright conditions</h3>
<p> Look at the header of the manual page source for the author(s) and copyright conditions. Note that these can be different from page to page!</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-_syscall/">_syscall</a></code>(2), <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2), <code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-intro/">intro</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7), <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7), <code><a href="/docs/linux/man/7-system_data_types/">system_data_types</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
