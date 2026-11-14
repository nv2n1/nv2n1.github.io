---
title: "spu_create(2)"
name: "spu_create"
section: "2"
letter: "s"
url: "/docs/linux/man/2-spu_create/"
description: "spu_create – create a new spu context"
---

<h2 class="name">NAME</h2>
<p> spu_create &#8211; create a new spu context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/spu.h&gt;
#include &lt;sys/types.h&gt;
int spu_create(const char *pathname, int flags, mode_t mode,
               int neighbor_fd);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>spu_create</code>() system call is used on PowerPC machines that implement the Cell Broadband Engine Architecture in order to access Synergistic Processor Units (SPUs). It creates a new logical context for an SPU in <i>pathname</i> and returns a file descriptor associated with it. <i>pathname</i> must refer to a nonexistent directory in the mount point of the SPU filesystem (<code>spufs</code>). If <code>spu_create</code>() is successful, a directory is created at <i>pathname</i> and it is populated with the files described in <code><a href="/docs/linux/man/7-spufs/">spufs</a></code>(7). </p>
<p> When a context is created, the returned file descriptor can only be passed to <code><a href="/docs/linux/man/2-spu_run/">spu_run</a></code>(2), used as the <i>dirfd</i> argument to the <code>*at</code> family of system calls (e.g., <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2)), or closed; other operations are not defined. A logical SPU context is destroyed (along with all files created within the context&#8217;s <i>pathname</i> directory) once the last reference to the context has gone; this usually occurs when the file descriptor returned by <code>spu_create</code>() is closed. </p>
<p> The <i>mode</i> argument (minus any bits set in the process&#8217;s <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)) specifies the permissions used for creating the new directory in <code>spufs</code>. See <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) for a full list of the possible <i>mode</i> values. </p>
<p> The <i>neighbor_fd</i> is used only when the <code>SPU_CREATE_AFFINITY_SPU</code> flag is specified; see below. </p>
<p> The <i>flags</i> argument can be zero or any bitwise OR-ed combination of the following constants:</p>
<dl>
<dt><code>SPU_CREATE_EVENTS_ENABLED</code></p>
<dd> Rather than using signals for reporting DMA errors, use the <i>event</i> argument to <code><a href="/docs/linux/man/2-spu_run/">spu_run</a></code>(2).</p>
<dt><code>SPU_CREATE_GANG</code></p>
<dd> Create an SPU gang instead of a context. (A gang is a group of SPU contexts that are functionally related to each other and which share common scheduling parameters&#8212;priority and policy. In the future, gang scheduling may be implemented causing the group to be switched in and out as a single unit.)</p>
<dt>
<dd> A new directory will be created at the location specified by the <i>pathname</i> argument. This gang may be used to hold other SPU contexts, by providing a pathname that is within the gang directory to further calls to <code>spu_create</code>().</p>
<dt><code>SPU_CREATE_NOSCHED</code></p>
<dd> Create a context that is not affected by the SPU scheduler. Once the context is run, it will not be scheduled out until it is destroyed by the creating process.</p>
<dt>
<dd> Because the context cannot be removed from the SPU, some functionality is disabled for <code>SPU_CREATE_NOSCHED</code> contexts. Only a subset of the files will be available in this context directory in <code>spufs</code>. Additionally, <code>SPU_CREATE_NOSCHED</code> contexts cannot dump a core file when crashing.</p>
<dt>
<dd> Creating <code>SPU_CREATE_NOSCHED</code> contexts requires the <code>CAP_SYS_NICE</code> capability.</p>
<dt><code>SPU_CREATE_ISOLATE</code></p>
<dd> Create an isolated SPU context. Isolated contexts are protected from some PPE (PowerPC Processing Element) operations, such as access to the SPU local store and the NPC register.</p>
<dt>
<dd> Creating <code>SPU_CREATE_ISOLATE</code> contexts also requires the <code>SPU_CREATE_NOSCHED</code> flag.</p>
<dt><code>SPU_CREATE_AFFINITY_SPU</code> (since Linux 2.6.23)</p>
<dd> Create a context with affinity to another SPU context. This affinity information is used within the SPU scheduling algorithm. Using this flag requires that a file descriptor referring to the other SPU context be passed in the <i>neighbor_fd</i> argument.</p>
<dt><code>SPU_CREATE_AFFINITY_MEM</code> (since Linux 2.6.23)</p>
<dd> Create a context with affinity to system memory. This affinity information is used within the SPU scheduling algorithm.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>spu_create</code>() returns a new file descriptor. On error, -1 is returned, and <i>errno</i> is set to one of the error codes listed below.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The current user does not have write access to the <code><a href="/docs/linux/man/7-spufs/">spufs</a></code>(7) mount point.</p>
<dt><code>EEXIST</code></p>
<dd> An SPU context already exists at the given pathname.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> is not a valid string pointer in the calling process&#8217;s address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>pathname</i> is not a directory in the <code><a href="/docs/linux/man/7-spufs/">spufs</a></code>(7) mount point, or invalid flags have been provided.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were found while resolving <i>pathname</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd> An isolated context was requested, but the hardware does not support SPU isolation.</p>
<dt><code>ENOENT</code></p>
<dd> Part of <i>pathname</i> could not be resolved.</p>
<dt><code>ENOMEM</code></p>
<dd> The kernel could not allocate all resources required.</p>
<dt><code>ENOSPC</code></p>
<dd> There are not enough SPU resources available to create a new context or the user-specific limit for the number of SPU contexts has been reached.</p>
<dt><code>ENOSYS</code></p>
<dd> The functionality is not provided by the current system, because either the hardware does not provide SPUs or the spufs module is not loaded.</p>
<dt><code>ENOTDIR</code></p>
<dd> A part of <i>pathname</i> is not a directory.</p>
<dt><code>EPERM</code></p>
<dd> The <code>SPU_CREATE_NOSCHED</code> flag has been given, but the user does not have the <code>CAP_SYS_NICE</code> capability.</dl>
<h2>FILES</h2>
<p> <i>pathname</i> must point to a location beneath the mount point of <code>spufs</code>. By convention, it gets mounted in <i>/spu</i>.</p>
<h2>VERSIONS</h2>
<p> The <code>spu_create</code>() system call was added to Linux in kernel 2.6.16.</p>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific and implemented only on the PowerPC architecture. Programs using this system call are not portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). Note however, that <code>spu_create</code>() is meant to be used from libraries that implement a more abstract interface to SPUs, not to be used from regular applications. See for the recommended libraries. </p>
<p> Prior to the addition of the <code>SPU_CREATE_AFFINITY_SPU</code> flag in Linux 2.6.23, the <code>spu_create</code>() system call took only three arguments (i.e., there was no <i>neighbor_fd</i> argument).</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-spu_run/">spu_run</a></code>(2) for an example of the use of <code>spu_create</code>()</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-spu_run/">spu_run</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-spufs/">spufs</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
