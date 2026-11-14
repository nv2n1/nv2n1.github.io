---
title: "shm_overview(7)"
name: "shm_overview"
section: "7"
letter: "s"
url: "/docs/linux/man/7-shm_overview/"
description: "shm_overview – overview of POSIX shared memory"
---

<p>shm_overview &#8211; overview of POSIX shared memory</p>
<h2>Description</h2>
<p>The POSIX shared memory API allows processes to communicate information by sharing a region of memory. </p>
<p> The interfaces employed in the API are:</p>
<dl>
<dt><code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3)</p>
<dd>Create and open a new object, or open an existing object. This is analogous to <code><a href="/docs/linux/man/2-open/">open</a></code>(2). The call returns a file descriptor for use by the other interfaces listed below.</p>
<dt><code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2)</p>
<dd>Set the size of the shared memory object. (A newly created shared memory object has a length of zero.)</p>
<dt><code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)</p>
<dd>Map the shared memory object into the virtual address space of the calling process.</p>
<dt><code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2)</p>
<dd>Unmap the shared memory object from the virtual address space of the calling process.</p>
<dt><code><a href="/docs/linux/man/3-shm_unlink/">shm_unlink</a></code>(3)</p>
<dd>Remove a shared memory object name.</p>
<dt><code><a href="/docs/linux/man/2-close/">close</a></code>(2)</p>
<dd>Close the file descriptor allocated by <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3) when it is no longer needed.</p>
<dt><code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2)</p>
<dd>Obtain a <i>stat</i> structure that describes the shared memory object. Among the information returned by this call are the object&#8217;s size (<i>st_size</i>), permissions (<i>st_mode</i>), owner (<i>st_uid</i>), and group (<i>st_gid</i>).</p>
<dt><code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2)</p>
<dd>To change the ownership of a shared memory object.</p>
<dt><code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2)</p>
<dd>To change the permissions of a shared memory object.</dl>
<h3>Versions</h3>
<p>POSIX shared memory is supported since Linux 2.4 and glibc 2.2.</p>
<h3>Persistence</h3>
<p>POSIX shared memory objects have kernel persistence: a shared memory object will exist until the system is shut down, or until all processes have unmapped the object and it has been deleted with <code><a href="/docs/linux/man/3-shm_unlink/">shm_unlink</a></code>(3)</p>
<h3>Linking</h3>
<p>Programs using the POSIX shared memory API must be compiled with <i>cc -lrt</i> to link against the real-time library, <i>librt</i>.</p>
<h3>Accessing shared memory objects via the filesystem</h3>
<p>On Linux, shared memory objects are created in a (<i><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></i>(5)) virtual filesystem, normally mounted under <i>/dev/shm</i>. Since kernel 2.6.19, Linux supports the use of access control lists (ACLs) to control the permissions of objects in the virtual filesystem.</p>
<h2>Notes</h2>
<p>Typically, processes must synchronize their access to a shared memory object, using, for example, POSIX semaphores. </p>
<p> System V shared memory (<code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/2-shmop/">shmop</a></code>(2), etc.) is an older shared memory API. POSIX shared memory provides a simpler, and better designed interface; on the other hand POSIX shared memory is somewhat less widely available (especially on older systems) than System V shared memory.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-fchmod/">fchmod</a></code>(2), <code><a href="/docs/linux/man/2-fchown/">fchown</a></code>(2), <code><a href="/docs/linux/man/2-fstat/">fstat</a></code>(2), <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2), <code><a href="/docs/linux/man/2-shmop/">shmop</a></code>(2), <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3), <code><a href="/docs/linux/man/3-shm_unlink/">shm_unlink</a></code>(3), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
