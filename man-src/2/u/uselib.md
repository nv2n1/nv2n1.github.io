---
title: "uselib(2)"
name: "uselib"
section: "2"
letter: "u"
url: "/docs/linux/man/2-uselib/"
description: "uselib – load shared library"
---

<h2 class="name">NAME</h2>
<p> uselib &#8211; load shared library </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int uselib(const char *</code><i>library</i><code>);</code> </p>
<p> <i>Note</i>: No declaration of this system call is provided in glibc headers; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The system call <code>uselib</code>() serves to load a shared library to be used by the calling process. It is given a pathname. The address where to load is found in the library itself. The library can have any recognized binary format.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> In addition to all of the error codes returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), the following may also be returned:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The library specified by <i>library</i> does not have read or execute permission, or the caller does not have search permission for one of the directories in the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOEXEC</code></p>
<dd> The file specified by <i>library</i> is not an executable of a known type; for example, it does not have the correct magic numbers.</dl>
<h2>CONFORMING TO</h2>
<p> <code>uselib</code>() is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> This obsolete system call is not supported by glibc. No declaration is provided in glibc headers, but, through a quirk of history, glibc versions before 2.23 did export an ABI for this system call. Therefore, in order to employ this system call, it was sufficient to manually declare the interface in your code; alternatively, you could invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> In ancient libc versions (before glibc 2.0), <code>uselib</code>() was used to load the shared libraries with names found in an array of names in the binary. </p>
<p> Since Linux 3.15, this system call is available only when the kernel is configured with the <code>CONFIG_USELIB</code> option.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ar/">ar</a></code>(1), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1), <code><a href="/docs/linux/man/1-ldd/">ldd</a></code>(1), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
