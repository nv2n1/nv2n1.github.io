---
title: "shmget(2)"
name: "shmget"
section: "2"
letter: "s"
url: "/docs/linux/man/2-shmget/"
description: "shmget – allocates a System V shared memory segment"
---

<h2 class="name">NAME</h2>
<p> shmget &#8211; allocates a System V shared memory segment </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/ipc.h&gt;</code><br />
 <code>#include &lt;sys/shm.h&gt;</code> </p>
<p> <code>int shmget(key_t </code><i>key</i><code>, size_t </code><i>size</i><code>, int </code><i>shmflg</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>shmget</code>() returns the identifier of the System V shared memory segment associated with the value of the argument <i>key</i>. It may be used either to obtain the identifier of a previously created shared memory segment (when <i>shmflg</i> is zero and <i>key</i> does not have the value <code>IPC_PRIVATE</code>), or to create a new set. </p>
<p> A new shared memory segment, with size equal to the value of <i>size</i> rounded up to a multiple of <code>PAGE_SIZE</code>, is created if <i>key</i> has the value <code>IPC_PRIVATE</code> or <i>key</i> isn&#8217;t <code>IPC_PRIVATE</code>, no shared memory segment corresponding to <i>key</i> exists, and <code>IPC_CREAT</code> is specified in <i>shmflg</i>. </p>
<p> If <i>shmflg</i> specifies both <code>IPC_CREAT</code> and <code>IPC_EXCL</code> and a shared memory segment already exists for <i>key</i>, then <code>shmget</code>() fails with <i>errno</i> set to <code>EEXIST</code>. (This is analogous to the effect of the combination <code>O_CREAT | O_EXCL</code> for <code><a href="/docs/linux/man/2-open/">open</a></code>(2).) </p>
<p> The value <i>shmflg</i> is composed of:</p>
<dl>
<dt><code>IPC_CREAT</code></p>
<dd> Create a new segment. If this flag is not used, then <code>shmget</code>() will find the segment associated with <i>key</i> and check to see if the user has permission to access the segment.</p>
<dt><code>IPC_EXCL</code></p>
<dd> This flag is used with <code>IPC_CREAT</code> to ensure that this call creates the segment. If the segment already exists, the call fails.</p>
<dt><code>SHM_HUGETLB</code> (since Linux 2.6)</p>
<dd> Allocate the segment using &quot;huge pages.&quot; See the Linux kernel source file <i>Documentation/admin-guide/mm/hugetlbpage.rst</i> for further information.</p>
<dt><code>SHM_HUGE_2MB</code>, <code>SHM_HUGE_1GB</code> (since Linux 3.8)</p>
<dd> Used in conjunction with <code>SHM_HUGETLB</code> to select alternative hugetlb page sizes (respectively, 2 MB and 1 GB) on systems that support multiple hugetlb page sizes.</p>
<dt>
<dd> More generally, the desired huge page size can be configured by encoding the base-2 logarithm of the desired page size in the six bits at the offset <code>SHM_HUGE_SHIFT</code>. Thus, the above two constants are defined as:</p>
<dt>
<dd> #define SHM_HUGE_2MB (21 &lt;&lt; SHM_HUGE_SHIFT) #define SHM_HUGE_1GB (30 &lt;&lt; SHM_HUGE_SHIFT)</p>
<dt>
<dd> For some additional details, see the discussion of the similarly named constants in <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<dt><code>SHM_NORESERVE</code> (since Linux 2.6.15)</p>
<dd> This flag serves the same purpose as the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_NORESERVE</code> flag. Do not reserve swap space for this segment. When swap space is reserved, one has the guarantee that it is possible to modify the segment. When swap space is not reserved one might get <code>SIGSEGV</code> upon a write if no physical memory is available. See also the discussion of the file <i>/proc/sys/vm/overcommit_memory</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</dl>
<p> In addition to the above flags, the least significant 9 bits of <i>shmflg</i> specify the permissions granted to the owner, group, and others. These bits have the same format, and the same meaning, as the <i>mode</i> argument of <code><a href="/docs/linux/man/2-open/">open</a></code>(2). Presently, execute permissions are not used by the system. </p>
<p> When a new shared memory segment is created, its contents are initialized to zero values, and its associated data structure, <i>shmid_ds</i> (see <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2)), is initialized as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>shm_perm.cuid</i> and <i>shm_perm.uid</i> are set to the effective user ID of the calling process.</p>
<dt>&bull;</p>
<dd> <i>shm_perm.cgid</i> and <i>shm_perm.gid</i> are set to the effective group ID of the calling process.</p>
<dt>&bull;</p>
<dd> The least significant 9 bits of <i>shm_perm.mode</i> are set to the least significant 9 bit of <i>shmflg</i>.</p>
<dt>&bull;</p>
<dd> <i>shm_segsz</i> is set to the value of <i>size</i>.</p>
<dt>&bull;</p>
<dd> <i>shm_lpid</i>, <i>shm_nattch</i>, <i>shm_atime</i>, and <i>shm_dtime</i> are set to 0.</p>
<dt>&bull;</p>
<dd> <i>shm_ctime</i> is set to the current time.</dl>
<p> If the shared memory segment already exists, the permissions are verified, and a check is made to see if it is marked for destruction.</p>
<h2>RETURN VALUE</h2>
<p> On success, a valid shared memory identifier is returned. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> On failure, <i>errno</i> is set to one of the following:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The user does not have permission to access the shared memory segment, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EEXIST</code></p>
<dd> <code>IPC_CREAT</code> and <code>IPC_EXCL</code> were specified in <i>shmflg</i>, but a shared memory segment already exists for <i>key</i>.</p>
<dt><code>EINVAL</code></p>
<dd> A new segment was to be created and <i>size</i> is less than <code>SHMMIN</code> or greater than <code>SHMMAX</code>.</p>
<dt><code>EINVAL</code></p>
<dd> A segment for the given <i>key</i> exists, but <i>size</i> is greater than the size of that segment.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOENT</code></p>
<dd> No segment exists for the given <i>key</i>, and <code>IPC_CREAT</code> was not specified.</p>
<dt><code>ENOMEM</code></p>
<dd> No memory could be allocated for segment overhead.</p>
<dt><code>ENOSPC</code></p>
<dd> All possible shared memory IDs have been taken (<code>SHMMNI</code>), or allocating a segment of the requested <i>size</i> would cause the system to exceed the system-wide limit on shared memory (<code>SHMALL</code>).</p>
<dt><code>EPERM</code></p>
<dd> The <code>SHM_HUGETLB</code> flag was specified, but the caller was not privileged (did not have the <code>CAP_IPC_LOCK</code> capability).</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. </p>
<p> <code>SHM_HUGETLB</code> and <code>SHM_NORESERVE</code> are Linux extensions.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> <code>IPC_PRIVATE</code> isn&#8217;t a flag field but a <i>key_t</i> type. If this special value is used for <i>key</i>, the system call ignores all but the least significant 9 bits of <i>shmflg</i> and creates a new shared memory segment.</p>
<h3>Shared memory limits</h3>
<p> The following limits on shared memory segment resources affect the <code>shmget</code>() call:</p>
<dl>
<dt><code>SHMALL</code></p>
<dd> System-wide limit on the total amount of shared memory, measured in units of the system page size.</p>
<dt>
<dd> On Linux, this limit can be read and modified via <i>/proc/sys/kernel/shmall</i>. Since Linux 3.16, the default value for this limit is:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ULONG_MAX &#8211; 2^24</p>
<dt>
<dd> The effect of this value (which is suitable for both 32-bit and 64-bit systems) is to impose no limitation on allocations. This value, rather than <code>ULONG_MAX</code>, was chosen as the default to prevent some cases where historical applications simply raised the existing limit without first checking its current value. Such applications would cause the value to overflow if the limit was set at <code>ULONG_MAX</code>.</p>
<dt>
<dd> From Linux 2.4 up to Linux 3.15, the default value for this limit was:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;SHMMAX&nbsp;/&nbsp;PAGE_SIZE&nbsp;*&nbsp;(SHMMNI&nbsp;/&nbsp;16)</p>
<dt>
<dd> If <code>SHMMAX</code> and <code>SHMMNI</code> were not modified, then multiplying the result of this formula by the page size (to get a value in bytes) yielded a value of 8 GB as the limit on the total memory used by all shared memory segments.</p>
<dt><code>SHMMAX</code></p>
<dd> Maximum size in bytes for a shared memory segment.</p>
<dt>
<dd> On Linux, this limit can be read and modified via <i>/proc/sys/kernel/shmmax</i>. Since Linux 3.16, the default value for this limit is:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ULONG_MAX &#8211; 2^24</p>
<dt>
<dd> The effect of this value (which is suitable for both 32-bit and 64-bit systems) is to impose no limitation on allocations. See the description of <code>SHMALL</code> for a discussion of why this default value (rather than <code>ULONG_MAX</code>) is used.</p>
<dt>
<dd> From Linux 2.2 up to Linux 3.15, the default value of this limit was 0x2000000 (32 MB).</p>
<dt>
<dd> Because it is not possible to map just part of a shared memory segment, the amount of virtual memory places another limit on the maximum size of a usable segment: for example, on i386 the largest segments that can be mapped have a size of around 2.8 GB, and on x86-64 the limit is around 127 TB.</p>
<dt><code>SHMMIN</code></p>
<dd> Minimum size in bytes for a shared memory segment: implementation dependent (currently 1 byte, though <code>PAGE_SIZE</code> is the effective minimum size).</p>
<dt><code>SHMMNI</code></p>
<dd> System-wide limit on the number of shared memory segments. In Linux 2.2, the default value for this limit was 128; since Linux 2.4, the default value is 4096.</p>
<dt>
<dd> On Linux, this limit can be read and modified via <i>/proc/sys/kernel/shmmni</i>.</dl>
<p> The implementation has no specific limits for the per-process maximum number of shared memory segments (<code>SHMSEG</code>).</p>
<h3>Linux notes</h3>
<p> Until version 2.3.30, Linux would return <code>EIDRM</code> for a <code>shmget</code>() on a shared memory segment scheduled for deletion.</p>
<h2>BUGS</h2>
<p> The name choice <code>IPC_PRIVATE</code> was perhaps unfortunate, <code>IPC_NEW</code> would more clearly show its function.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-shmop/">shmop</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmctl/">shmctl</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/3-ftok/">ftok</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
