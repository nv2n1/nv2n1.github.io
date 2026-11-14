---
title: "munlockall(2)"
name: "munlockall"
section: "2"
letter: "m"
url: "/docs/linux/man/2-munlockall/"
description: "mlock, mlock2, munlock, mlockall, munlockall – lock and unlock memory"
---

<h2 class="name">NAME</h2>
<p> mlock, mlock2, munlock, mlockall, munlockall &#8211; lock and unlock memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/mman.h&gt;
int mlock(const void *addr, size_t len);
int mlock2(const void *addr, size_t len, int flags);
int munlock(const void *addr, size_t len);
int mlockall(int flags);
int munlockall(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mlock</code>(), <code>mlock2</code>(), and <code>mlockall</code>() lock part or all of the calling process&#8217;s virtual address space into RAM, preventing that memory from being paged to the swap area. </p>
<p> <code>munlock</code>() and <code>munlockall</code>() perform the converse operation, unlocking part or all of the calling process&#8217;s virtual address space, so that pages in the specified virtual address range may once more to be swapped out if required by the kernel memory manager. </p>
<p> Memory locking and unlocking are performed in units of whole pages.</p>
<h3>mlock(), mlock2(), and munlock()</h3>
<p> <code>mlock</code>() locks pages in the address range starting at <i>addr</i> and continuing for <i>len</i> bytes. All pages that contain a part of the specified address range are guaranteed to be resident in RAM when the call returns successfully; the pages are guaranteed to stay in RAM until later unlocked. </p>
<p> <code>mlock2</code>() also locks pages in the specified range starting at <i>addr</i> and continuing for <i>len</i> bytes. However, the state of the pages contained in that range after the call returns successfully will depend on the value in the <i>flags</i> argument. </p>
<p> The <i>flags</i> argument can be either 0 or the following constant:</p>
<dl>
<dt><code>MLOCK_ONFAULT</code></p>
<dd> Lock pages that are currently resident and mark the entire range so that the remaining nonresident pages are locked when they are populated by a page fault.</dl>
<p> If <i>flags</i> is 0, <code>mlock2</code>() behaves exactly the same as <code>mlock</code>(). </p>
<p> <code>munlock</code>() unlocks pages in the address range starting at <i>addr</i> and continuing for <i>len</i> bytes. After this call, all pages that contain a part of the specified memory range can be moved to external swap space again by the kernel.</p>
<h3>mlockall() and munlockall()</h3>
<p> <code>mlockall</code>() locks all pages mapped into the address space of the calling process. This includes the pages of the code, data and stack segment, as well as shared libraries, user space kernel data, shared memory, and memory-mapped files. All mapped pages are guaranteed to be resident in RAM when the call returns successfully; the pages are guaranteed to stay in RAM until later unlocked. </p>
<p> The <i>flags</i> argument is constructed as the bitwise OR of one or more of the following constants:</p>
<dl>
<dt><code>MCL_CURRENT</code></p>
<dd> Lock all pages which are currently mapped into the address space of the process.</p>
<dt><code>MCL_FUTURE</code></p>
<dd> Lock all pages which will become mapped into the address space of the process in the future. These could be, for instance, new pages required by a growing heap and stack as well as new memory-mapped files or shared memory regions.</p>
<dt><code>MCL_ONFAULT</code> (since Linux 4.4)</p>
<dd> Used together with <code>MCL_CURRENT</code>, <code>MCL_FUTURE</code>, or both. Mark all current (with <code>MCL_CURRENT</code>) or future (with <code>MCL_FUTURE</code>) mappings to lock pages when they are faulted in. When used with <code>MCL_CURRENT</code>, all present pages are locked, but <code>mlockall</code>() will not fault in non-present pages. When used with <code>MCL_FUTURE</code>, all future mappings will be marked to lock pages when they are faulted in, but they will not be populated by the lock when the mapping is created. <code>MCL_ONFAULT</code> must be used with either <code>MCL_CURRENT</code> or <code>MCL_FUTURE</code> or both.</dl>
<p> If <code>MCL_FUTURE</code> has been specified, then a later system call (e.g., <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)), may fail if it would cause the number of locked bytes to exceed the permitted maximum (see below). In the same circumstances, stack growth may likewise fail: the kernel will deny stack expansion and deliver a <code>SIGSEGV</code> signal to the process. </p>
<p> <code>munlockall</code>() unlocks all pages mapped into the address space of the calling process.</p>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return 0. On error, -1 is returned, <i>errno</i> is set appropriately, and no changes are made to any locks in the address space of the process.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> (Linux 2.6.9 and later) the caller had a nonzero <code>RLIMIT_MEMLOCK</code> soft resource limit, but tried to lock more memory than the limit permitted. This limit is not enforced if the process is privileged (<code>CAP_IPC_LOCK</code>).</p>
<dt><code>ENOMEM</code></p>
<dd> (Linux 2.4 and earlier) the calling process tried to lock more than half of RAM.</p>
<dt><code>EPERM</code></p>
<dd> The caller is not privileged, but needs privilege (<code>CAP_IPC_LOCK</code>) to perform the requested operation.</dl>
<p> For <code>mlock</code>(), <code>mlock2</code>(), and <code>munlock</code>():</p>
<dl>
<dt><code>EAGAIN</code></p>
<dd> Some or all of the specified address range could not be locked.</p>
<dt><code>EINVAL</code></p>
<dd> The result of the addition <i>addr</i>+<i>len</i> was less than <i>addr</i> (e.g., the addition may have resulted in an overflow).</p>
<dt><code>EINVAL</code></p>
<dd> (Not on Linux) <i>addr</i> was not a multiple of the page size.</p>
<dt><code>ENOMEM</code></p>
<dd> Some of the specified address range does not correspond to mapped pages in the address space of the process.</p>
<dt><code>ENOMEM</code></p>
<dd> Locking or unlocking a region would result in the total number of mappings with distinct attributes (e.g., locked versus unlocked) exceeding the allowed maximum. (For example, unlocking a range in the middle of a currently locked mapping would result in three mappings: two locked mappings at each end and an unlocked mapping in the middle.)</dl>
<p> For <code>mlock2</code>():</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> Unknown <i>flags</i> were specified.</dl>
<p> For <code>mlockall</code>():</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> Unknown <i>flags</i> were specified or <code>MCL_ONFAULT</code> was specified without either <code>MCL_FUTURE</code> or <code>MCL_CURRENT</code>.</dl>
<p> For <code>munlockall</code>():</p>
<dl>
<dt><code>EPERM</code></p>
<dd> (Linux 2.6.8 and earlier) The caller was not privileged (<code>CAP_IPC_LOCK</code>).</dl>
<h2>VERSIONS</h2>
<p> <code>mlock2</code>() is available since Linux 4.4; glibc support was added in version 2.27.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. </p>
<p> <code>mlock2</code>() is Linux specific. </p>
<p> On POSIX systems on which <code>mlock</code>() and <code>munlock</code>() are available, <code>_POSIX_MEMLOCK_RANGE</code> is defined in <i>&lt;unistd.h&gt;</i> and the number of bytes in a page can be determined from the constant <code>PAGESIZE</code> (if defined) in <i>&lt;limits.h&gt;</i> or by calling <i>sysconf(_SC_PAGESIZE)</i>. </p>
<p> On POSIX systems on which <code>mlockall</code>() and <code>munlockall</code>() are available, <code>_POSIX_MEMLOCK</code> is defined in <i>&lt;unistd.h&gt;</i> to a value greater than 0. (See also <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3).)</p>
<h2>NOTES</h2>
<p> Memory locking has two main applications: real-time algorithms and high-security data processing. Real-time applications require deterministic timing, and, like scheduling, paging is one major cause of unexpected program execution delays. Real-time applications will usually also switch to a real-time scheduler with <code><a href="/docs/linux/man/2-sched_setscheduler/">sched_setscheduler</a></code>(2). Cryptographic security software often handles critical bytes like passwords or secret keys as data structures. As a result of paging, these secrets could be transferred onto a persistent swap store medium, where they might be accessible to the enemy long after the security software has erased the secrets in RAM and terminated. (But be aware that the suspend mode on laptops and some desktop computers will save a copy of the system&#8217;s RAM to disk, regardless of memory locks.) </p>
<p> Real-time processes that are using <code>mlockall</code>() to prevent delays on page faults should reserve enough locked stack pages before entering the time-critical section, so that no page fault can be caused by function calls. This can be achieved by calling a function that allocates a sufficiently large automatic variable (an array) and writes to the memory occupied by this array in order to touch these stack pages. This way, enough pages will be mapped for the stack and can be locked into RAM. The dummy writes ensure that not even copy-on-write page faults can occur in the critical section. </p>
<p> Memory locks are not inherited by a child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and are automatically removed (unlocked) during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) or when the process terminates. The <code>mlockall</code>() <code>MCL_FUTURE</code> and <code>MCL_FUTURE | MCL_ONFAULT</code> settings are not inherited by a child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and are cleared during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Note that <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) will prepare the address space for a copy-on-write operation. The consequence is that any write access that follows will cause a page fault that in turn may cause high latencies for a real-time process. Therefore, it is crucial not to invoke <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) after an <code>mlockall</code>() or <code>mlock</code>() operation&#8212;not even from a thread which runs at a low priority within a process which also has a thread running at elevated priority. </p>
<p> The memory lock on an address range is automatically removed if the address range is unmapped via <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2). </p>
<p> Memory locks do not stack, that is, pages which have been locked several times by calls to <code>mlock</code>(), <code>mlock2</code>(), or <code>mlockall</code>() will be unlocked by a single call to <code>munlock</code>() for the corresponding range or by <code>munlockall</code>(). Pages which are mapped to several locations or by several processes stay locked into RAM as long as they are locked at least at one location or by at least one process. </p>
<p> If a call to <code>mlockall</code>() which uses the <code>MCL_FUTURE</code> flag is followed by another call that does not specify this flag, the changes made by the <code>MCL_FUTURE</code> call will be lost. </p>
<p> The <code>mlock2</code>() <code>MLOCK_ONFAULT</code> flag and the <code>mlockall</code>() <code>MCL_ONFAULT</code> flag allow efficient memory locking for applications that deal with large mappings where only a (small) portion of pages in the mapping are touched. In such cases, locking all of the pages in a mapping would incur a significant penalty for memory locking.</p>
<h3>Linux notes</h3>
<p> Under Linux, <code>mlock</code>(), <code>mlock2</code>(), and <code>munlock</code>() automatically round <i>addr</i> down to the nearest page boundary. However, the POSIX.1 specification of <code>mlock</code>() and <code>munlock</code>() allows an implementation to require that <i>addr</i> is page aligned, so portable applications should ensure this. </p>
<p> The <i>VmLck</i> field of the Linux-specific <i>/proc/[pid]/status</i> file shows how many kilobytes of memory the process with ID <i>PID</i> has locked using <code>mlock</code>(), <code>mlock2</code>(), <code>mlockall</code>(), and <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_LOCKED</code>.</p>
<h3>Limits and permissions</h3>
<p> In Linux 2.6.8 and earlier, a process must be privileged (<code>CAP_IPC_LOCK</code>) in order to lock memory and the <code>RLIMIT_MEMLOCK</code> soft resource limit defines a limit on how much memory the process may lock. </p>
<p> Since Linux 2.6.9, no limits are placed on the amount of memory that a privileged process can lock and the <code>RLIMIT_MEMLOCK</code> soft resource limit instead defines a limit on how much memory an unprivileged process may lock.</p>
<h2>BUGS</h2>
<p> In Linux 4.8 and earlier, a bug in the kernel&#8217;s accounting of locked memory for unprivileged processes (i.e., without <code>CAP_IPC_LOCK</code>) meant that if the region specified by <i>addr</i> and <i>len</i> overlapped an existing lock, then the already locked bytes in the overlapping region were counted twice when checking against the limit. Such double accounting could incorrectly calculate a &quot;total locked memory&quot; value for the process that exceeded the <code>RLIMIT_MEMLOCK</code> limit, with the result that <code>mlock</code>() and <code>mlock2</code>() would fail on requests that should have succeeded. This bug was fixed in Linux 4.9. </p>
<p> In the 2.4 series Linux kernels up to and including 2.4.17, a bug caused the <code>mlockall</code>() <code>MCL_FUTURE</code> flag to be inherited across a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). This was rectified in kernel 2.4.18. </p>
<p> Since kernel 2.6.9, if a privileged process calls <i>mlockall(MCL_FUTURE)</i> and later drops privileges (loses the <code>CAP_IPC_LOCK</code> capability by, for example, setting its effective UID to a nonzero value), then subsequent memory allocations (e.g., <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2)) will fail if the <code>RLIMIT_MEMLOCK</code> resource limit is encountered.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
