---
title: "ibv_fork_init(3)"
name: "ibv_fork_init"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_fork_init/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_fork_init - initialize libibverbs to support fork() 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_fork_init(void);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_fork_init() initializes libibverbs's data structures to handle fork() function calls correctly and avoid data corruption, whether fork() is called explicitly or implicitly (such as in system()). 

 It is not necessary to use this function if all parent process threads are always blocked until all child processes end or change address spaces via an exec() operation.

<h2>RETURN VALUE</h2>

 

 ibv_fork_init() returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>NOTES</h2>

 

 ibv_fork_init() works on Linux kernels supporting the MADV_DONTFORK flag for madvise() (2.6.17 and higher). 

 Setting the environment variable RDMAV_FORK_SAFE or IBV_FORK_SAFE has the same effect as calling ibv_fork_init(). 

 Setting the environment variable RDMAV_HUGEPAGES_SAFE tells the library to check the underlying page size used by the kernel for memory regions. This is required if an application uses huge pages either directly or indirectly via a library such as libhugetlbfs. 

 Calling ibv_fork_init() will reduce performance due to an extra system call for every memory registration, and the additional memory allocated to track memory regions. The precise performance impact depends on the workload and usually will not be significant. 

 Setting RDMAV_HUGEPAGES_SAFE adds further overhead to all memory registrations.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-exec/">exec</a>(3), <a HREF="/docs/linux/man/2-fork/">fork</a>(2), <a HREF="/docs/linux/man/3-ibv_get_device_list/">ibv_get_device_list</a>(3), <a HREF="/docs/linux/man/3-system/">system</a>(3), <a HREF="/docs/linux/man/2-wait/">wait</a>(2)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


