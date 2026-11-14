---
title: "mm(3)"
name: "mm"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mm/"
description: "OSSP mm – Shared Memory Allocation"
---

<p><code>OSSP mm</code> &#8211; <code>Shared Memory Allocation</code></p>
<h2>Version</h2>
<p><font SIZE="-1">OSSP</font> mm <font SIZE="-1">1.4.2 (15-Aug-2006)</font></p>
<h2>Synopsis</h2>
<pre> #include &quot;mm.h&quot;</pre>
<p><code> Global Malloc-Replacement </code><font SIZE="-1"><code>API</code></font> </p>
<pre> int <code>MM_create</code>(size_t size, const char *file);
 int <code>MM_permission</code>(mode_t mode, uid_t owner, gid_t group);
 void <code>MM_reset</code>(void);
 void <code>MM_destroy</code>(void);
 int <code>MM_lock</code>(mm_lock_mode mode);
 int <code>MM_unlock</code>(void);
 void *<code>MM_malloc</code>(size_t size);
 void *<code>MM_realloc</code>(void *ptr, size_t size);
 void <code>MM_free</code>(void *ptr);
 void *<code>MM_calloc</code>(size_t number, size_t size);
 char *<code>MM_strdup</code>(const char *str);
 size_t <code>MM_sizeof</code>(void *ptr);
 size_t <code>MM_maxsize</code>(void);
 size_t <code>MM_available</code>(void);
 char *<code>MM_error</code>(void);</pre>
<p><code> Standard Malloc-Style </code><font SIZE="-1"><code>API</code></font> </p>
<pre> MM *<code>mm_create</code>(size_t size, char *file);
 int <code>mm_permission</code>(MM *mm, mode_t mode, uid_t owner, gid_t group);
 void <code>mm_reset</code>(MM *mm);
 void <code>mm_destroy</code>(MM *mm);
 int <code>mm_lock</code>(MM *mm, mm_lock_mode mode);
 int <code>mm_unlock</code>(MM *mm);
 void *<code>mm_malloc</code>(MM *mm, size_t size);
 void *<code>mm_realloc</code>(MM *mm, void *ptr, size_t size);
 void <code>mm_free</code>(MM *mm, void *ptr);
 void *<code>mm_calloc</code>(MM *mm, size_t number, size_t size);
 char *<code>mm_strdup</code>(MM *mm, const char *str);
 size_t <code>mm_sizeof</code>(MM *mm, void *ptr);
 size_t <code>mm_maxsize</code>(void);
 size_t <code>mm_available</code>(MM *mm);
 char *<code>mm_error</code>(void);
 void <code>mm_display_info</code>(MM *mm);</pre>
<p><code> Low-level Shared Memory </code><font SIZE="-1"><code>API</code></font> </p>
<pre> void *<code>mm_core_create</code>(size_t size, char *file);
 int <code>mm_core_permission</code>(void *core, mode_t mode, uid_t owner, gid_t group);
 void <code>mm_core_delete</code>(void *core);
 int <code>mm_core_lock</code>(void *core, mm_lock_mode mode);
 int <code>mm_core_unlock</code>(void *core);
 size_t <code>mm_core_size</code>(void *core);
 size_t <code>mm_core_maxsegsize</code>(void);
 size_t <code>mm_core_align2page</code>(size_t size);
 size_t <code>mm_core_align2click</code>(size_t size);</pre>
<p><code> Internal Library </code><font SIZE="-1"><code>API</code></font> </p>
<pre> void <code>mm_lib_error_set</code>(unsigned int, const char *str);
 char *<code>mm_lib_error_get</code>(void);
 int <code>mm_lib_version</code>(void);</pre>
<h2>Description</h2>
<p>The <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library is a 2-layer abstraction library which simplifies the usage of shared memory between forked (and this way strongly related) processes under Unix platforms. On the first (lower) layer it hides all platform dependent implementation details (allocation and locking) when dealing with shared memory segments and on the second (higher) layer it provides a high-level <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3)-style <font SIZE="-1">API</font> for a convenient and well known way to work with data-structures inside those shared memory segments. </p>
<p> The abbreviation <font SIZE="-1"><code>OSSP</code></font><code> mm</code> is historically and originally comes from the phrase &#8220;<i>memory mapped</i>&#8221; as used by the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) function. Because this facility is internally used by this library on most platforms to establish the shared memory segments.</p>
<h2><font SIZE="-1">LIBRARY</font> <font SIZE="-1">STRUCTURE</font></h2>
<p>This library is structured into three main APIs which are internally based on each other:</p>
<dl COMPACT>
<dt><code>Global Malloc-Replacement </code><font SIZE="-1"><code>API</code></font></p>
<dd>This is the most high-level <font SIZE="-1">API</font> which directly can be used as replacement <font SIZE="-1">API</font> for the <font SIZE="-1">POSIX</font>.1 memory allocation <font SIZE="-1">API</font> (<i><a href="/docs/linux/man/2-malloc/">malloc</a></i>(2) and friends). This is useful when converting <i>heap</i> based data structures to <i>shared memory</i> based data structures without the need to change the code dramatically. All which is needed is to prefix the <font SIZE="-1">POSIX</font>.1 memory allocation functions with `<tt>&quot;MM_&quot;</tt>&#8216;, i.e. `<tt>&quot;malloc&quot;</tt>&#8216; becomes `<tt>&quot;MM_malloc&quot;</tt>&#8216;, `<tt>&quot;strdup&quot;</tt>&#8216; becomes `<tt>&quot;MM_strdup&quot;</tt>&#8216;, etc. This <font SIZE="-1">API</font> internally uses just a global `<tt>&quot;MM *&quot;</tt>&#8216; pool for calling the corresponding functions (those with prefix `<tt>&quot;mm_&quot;</tt>&#8216;) of the <i>Standard Malloc-Style </i><font SIZE="-1"><i>API</i></font><i></i>.</p>
<dt><code>Standard Malloc-Style </code><font SIZE="-1"><code>API</code></font></p>
<dd>This is the standard high-level memory allocation <font SIZE="-1">API</font>. Its interface is similar to the <i>Global Malloc-Replacement </i><font SIZE="-1"><i>API</i></font><i></i> but it uses an explicit `<tt>&quot;MM *&quot;</tt>&#8216; pool to operate on. That is why every function of this <font SIZE="-1">API</font> has an argument of type `<tt>&quot;MM *&quot;</tt>&#8216; as its first argument. This <font SIZE="-1">API</font> provides a comfortable way to work with small dynamically allocated shared memory chunks inside large statically allocated shared memory segments. It is internally based on the <i>Low-Level Shared Memory </i><font SIZE="-1"><i>API</i></font><i></i> for creating the underlying shared memory segment.</p>
<dt><code>Low-Level Shared Memory </code><font SIZE="-1"><code>API</code></font></p>
<dd>This is the basis of the whole <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library. It provides low-level functions for creating shared memory segments with mutual exclusion (in short <i>mutex</i>) capabilities in a portable way. Internally the shared memory and mutex facility is implemented in various platform-dependent ways. A list of implementation variants follows under the next topic.</dl>
<h2><font SIZE="-1">SHARED</font> <font SIZE="-1">MEMORY</font> <font SIZE="-1">IMPLEMENTATION</font></h2>
<p>Internally the shared memory facility is implemented in various platform-dependent ways. Each way has its own advantages and disadvantages (in addition to the fact that some variants aren&#8217;t available at all on some platforms). The <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library&#8217;s configuration procedure tries hard to make a good decision. The implemented variants are now given for overview and background reasons with their advantages and disadvantages and in an ascending order, i.e. the <font SIZE="-1"><code>OSSP</code></font><code> mm</code> configuration mechanism chooses the last available one in the list as the preferred variant.</p>
<dl COMPACT>
<dt>Classical <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) on temporary file (<font SIZE="-1">MMFILE</font>)</p>
<dd><i>Advantage:</i> maximum portable. <i>Disadvantage:</i> needs a temporary file on the filesystem.</p>
<dt><i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) via <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-shm_open/">shm_open</a></i>(3) on temporary file (<font SIZE="-1">MMPOSX</font>)</p>
<dd><i>Advantage:</i> standardized by <font SIZE="-1">POSIX</font>.1 and theoretically portable. <i>Disadvantage:</i> needs a temporary file on the filesystem and is is usually not available on existing Unix platform.</p>
<dt>SVR4-style <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) on /dev/zero device (<font SIZE="-1">MMZERO</font>)</p>
<dd><i>Advantage:</i> widely available and mostly portable on <font SIZE="-1">SVR4</font> platforms. <i>Disadvantage:</i> needs the <tt>&quot;/dev/zero&quot;</tt> device and a <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) which supports memory mapping through this device.</p>
<dt>SysV <font SIZE="-1">IPC</font> <i><a href="/docs/linux/man/2-shmget/">shmget</a></i>(2) (<font SIZE="-1">IPCSHM</font>)</p>
<dd><i>Advantage:</i> does not need a temporary file or external device. <i>Disadvantage:</i> although available on mostly all modern Unix platforms, it has strong restrictions like the maximum size of a single shared memory segment (can be as small as 100KB, but depends on the platform).</p>
<dt>4.4BSD-style <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) via MAP_ANON facility (<font SIZE="-1">MMANON</font>)</p>
<dd><i>Advantage:</i> does not need a temporary file or external device. <i>Disadvantage:</i> usually only available on <font SIZE="-1">BSD</font> platforms and derivatives.</dl>
<h2><font SIZE="-1">LOCKING</font> <font SIZE="-1">IMPLEMENTATION</font></h2>
<p>As for the shared memory facility, internally the locking facility is implemented in various platform-dependent ways. They are again listed in ascending order, i.e. the <font SIZE="-1"><code>OSSP</code></font><code> mm</code> configuration mechanism chooses the last available one in the list as the preferred variant. The list of implemented variants is:</p>
<dl COMPACT>
<dt>4.2BSD-style <i><a href="/docs/linux/man/2-flock/">flock</a></i>(2) on temporary file (<font SIZE="-1">FLOCK</font>)</p>
<dd><i>Advantage:</i> exists on a lot of platforms, especially on older Unix derivatives. <i>Disadvantage:</i> needs a temporary file on the filesystem and has to re-open file-descriptors to it in each(!) <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2)&#8217;ed child process.</p>
<dt>SysV <font SIZE="-1">IPC</font> <i><a href="/docs/linux/man/2-semget/">semget</a></i>(2) (<font SIZE="-1">IPCSEM</font>)</p>
<dd><i>Advantage:</i> exists on a lot of platforms and does not need a temporary file. <i>Disadvantage:</i> an unmeant termination of the application leads to a semaphore leak because the facility does not allow a &#8220;remove in advance&#8221; trick (as the <font SIZE="-1">IPC</font> shared memory facility does) for safe cleanups.</p>
<dt>SVR4-style <i><a href="/docs/linux/man/2-fcntl/">fcntl</a></i>(2) on temporary file (<font SIZE="-1">FCNTL</font>)</p>
<dd><i>Advantage:</i> exists on a lot of platforms and is also the most powerful variant (although not always the fastest one). <i>Disadvantage:</i> needs a temporary file.</dl>
<h2><font SIZE="-1">MEMORY</font> <font SIZE="-1">ALLOCATION</font> <font SIZE="-1">STRATEGY</font></h2>
<p>The memory allocation strategy the <i>Standard Malloc-Style </i><font SIZE="-1"><i>API</i></font><i></i> functions use internally is the following:</p>
<dl COMPACT>
<dt><code>Allocation</code></p>
<dd>If a chunk of memory has to be allocated, the internal list of free chunks is searched for a minimal-size chunk which is larger or equal than the size of the to be allocated chunk (a <i>best fit</i> strategy). </p>
<p> If a chunk is found which matches this best-fit criteria, but is still a lot larger than the requested size, it is split into two chunks: One with exactly the requested size (which is the resulting chunk given back) and one with the remaining size (which is immediately re-inserted into the list of free chunks). </p>
<p> If no fitting chunk is found at all in the list of free chunks, a new one is created from the spare area of the shared memory segment until the segment is full (in which case an <i>out of memory</i> error occurs).</p>
<dt><code>Deallocation</code></p>
<dd>If a chunk of memory has to be deallocated, it is inserted in sorted manner into the internal list of free chunks. The insertion operation automatically merges the chunk with a previous and/or a next free chunk if possible, i.e. if the free chunks stay physically seamless (one after another) in memory, to automatically form larger free chunks out of smaller ones. </p>
<p> This way the shared memory segment is automatically defragmented when memory is deallocated.</dl>
<p> This strategy reduces memory waste and fragmentation caused by small and frequent allocations and deallocations to a minimum. </p>
<p> The internal implementation of the list of free chunks is not specially optimized (for instance by using binary search trees or even <i>splay</i> trees, etc), because it is assumed that the total amount of entries in the list of free chunks is always small (caused both by the fact that shared memory segments are usually a lot smaller than heaps and the fact that we always defragment by merging the free chunks if possible).</p>
<h2>Api Functions</h2>
<p>In the following, all <font SIZE="-1">API</font> functions are described in detail. The order directly follows the one in the <font SIZE="-1"><code>SYNOPSIS</code></font> section above.</p>
<h2>Global Malloc-Replacement <font SIZE="-1">API</font></h2>
<dl COMPACT>
<dt>int <code>MM_create</code>(size_t <i>size</i>, const char *<i>file</i>);</p>
<dd>This initializes the global shared memory pool with <i>size</i> and <i>file</i> and has to be called <i>before</i> any <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2) operations are performed by the application.</p>
<dt>int <code>MM_permission</code>(mode_t <i>mode</i>, uid_t <i>owner</i>, gid_t <i>group</i>);</p>
<dd>This sets the filesystem <i>mode</i>, <i>owner</i> and <i>group</i> for the global shared memory pool (has effects only if the underlying shared memory segment implementation is actually based on external auxiliary files). The arguments are directly passed through to <i><a href="/docs/linux/man/2-chmod/">chmod</a></i>(2) and <i><a href="/docs/linux/man/2-chown/">chown</a></i>(2).</p>
<dt>void <code>MM_reset</code>(void);</p>
<dd>This resets the global shared memory pool: all chunks that have been allocated in the pool are marked as free and are eligible for reuse. The global memory pool itself is not destroyed.</p>
<dt>void <code>MM_destroy</code>(void);</p>
<dd>This destroys the global shared memory pool and should be called <i>after</i> all child processes were killed.</p>
<dt>int <code>MM_lock</code>(mm_lock_mode <i>mode</i>);</p>
<dd>This locks the global shared memory pool for the current process in order to perform either shared/read-only (<i>mode</i> is <tt>&quot;MM_LOCK_RD&quot;</tt>) or exclusive/read-write (<i>mode</i> is <tt>&quot;MM_LOCK_RW&quot;</tt>) critical operations inside the global shared memory pool.</p>
<dt>int <code>MM_unlock</code>(void);</p>
<dd>This unlocks the global shared memory pool for the current process after the critical operations were performed inside the global shared memory pool.</p>
<dt>void *<code>MM_malloc</code>(size_t <i>size</i>);</p>
<dd>Identical to the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) function but instead of allocating memory from the <i>heap</i> it allocates it from the global shared memory pool.</p>
<dt>void <code>MM_free</code>(void *<i>ptr</i>);</p>
<dd>Identical to the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-free/">free</a></i>(3) function but instead of deallocating memory in the <i>heap</i> it deallocates it in the global shared memory pool.</p>
<dt>void *<code>MM_realloc</code>(void *<i>ptr</i>, size_t <i>size</i>);</p>
<dd>Identical to the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-realloc/">realloc</a></i>(3) function but instead of reallocating memory in the <i>heap</i> it reallocates it inside the global shared memory pool.</p>
<dt>void *<code>MM_calloc</code>(size_t <i>number</i>, size_t <i>size</i>);</p>
<dd>Identical to the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-calloc/">calloc</a></i>(3) function but instead of allocating and initializing memory from the <i>heap</i> it allocates and initializes it from the global shared memory pool.</p>
<dt>char *<code>MM_strdup</code>(const char *<i>str</i>);</p>
<dd>Identical to the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-strdup/">strdup</a></i>(3) function but instead of creating the string copy in the <i>heap</i> it creates it in the global shared memory pool.</p>
<dt>size_t <code>MM_sizeof</code>(const void *<i>ptr</i>);</p>
<dd>This function returns the size in bytes of the chunk starting at <i>ptr</i> when <i>ptr</i> was previously allocated with <i><a href="/docs/linux/man/3-mm_malloc/">MM_malloc</a></i>(3). The result is undefined if <i>ptr</i> was not previously allocated with <i><a href="/docs/linux/man/3-mm_malloc/">MM_malloc</a></i>(3).</p>
<dt>size_t <code>MM_maxsize</code>(void);</p>
<dd>This function returns the maximum size which is allowed as the first argument to the <i><a href="/docs/linux/man/3-mm_create/">MM_create</a></i>(3) function.</p>
<dt>size_t <code>MM_available</code>(void);</p>
<dd>Returns the amount in bytes of still available (free) memory in the global shared memory pool.</p>
<dt>char *<code>MM_error</code>(void);</p>
<dd>Returns the last error message which occurred inside the <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library.</dl>
<h2>Standard Malloc-Style <font SIZE="-1">API</font></h2>
<dl COMPACT>
<dt><font SIZE="-1">MM</font> *<code>mm_create</code>(size_t <i>size</i>, const char *<i>file</i>);</p>
<dd>This creates a shared memory pool which has space for approximately a total of <i>size</i> bytes with the help of <i>file</i>. Here <i>file</i> is a filesystem path to a file which need not to exist (and perhaps is never created because this depends on the platform and chosen shared memory and mutex implementation). The return value is a pointer to a <tt>&quot;MM&quot;</tt> structure which should be treated as opaque by the application. It describes the internals of the created shared memory pool. In case of an error <tt>&quot;NULL&quot;</tt> is returned. A <i>size</i> of 0 means to allocate the maximum allowed size which is platform dependent and is between a few <font SIZE="-1">KB</font> and the soft limit of 64MB.</p>
<dt>int <code>mm_permission</code>(<font SIZE="-1">MM</font> *<i>mm</i>, mode_t <i>mode</i>, uid_t <i>owner</i>, gid_t <i>group</i>);</p>
<dd>This sets the filesystem <i>mode</i>, <i>owner</i> and <i>group</i> for the shared memory pool <i>mm</i> (has effects only when the underlying shared memory segment implementation is actually based on external auxiliary files). The arguments are directly passed through to <i><a href="/docs/linux/man/2-chmod/">chmod</a></i>(2) and <i><a href="/docs/linux/man/2-chown/">chown</a></i>(2).</p>
<dt>void <code>mm_reset</code>(<font SIZE="-1">MM</font> *<i>mm</i>);</p>
<dd>This resets the shared memory pool <i>mm</i>: all chunks that have been allocated in the pool are marked as free and are eligible for reuse. The memory pool itself is not destroyed.</p>
<dt>void <code>mm_destroy</code>(<font SIZE="-1">MM</font> *<i>mm</i>);</p>
<dd>This destroys the complete shared memory pool <i>mm</i> and with it all chunks which were allocated in this pool. Additionally any created files on the filesystem corresponding to the shared memory pool are unlinked.</p>
<dt>int <code>mm_lock</code>(<font SIZE="-1">MM</font> *<i>mm</i>, mm_lock_mode <i>mode</i>);</p>
<dd>This locks the shared memory pool <i>mm</i> for the current process in order to perform either shared/read-only (<i>mode</i> is <tt>&quot;MM_LOCK_RD&quot;</tt>) or exclusive/read-write (<i>mode</i> is <tt>&quot;MM_LOCK_RW&quot;</tt>) critical operations inside the global shared memory pool.</p>
<dt>int <code>mm_unlock</code>(<font SIZE="-1">MM</font> *<i>mm</i>);</p>
<dd>This unlocks the shared memory pool <i>mm</i> for the current process after critical operations were performed inside the global shared memory pool.</p>
<dt>void *<code>mm_malloc</code>(<font SIZE="-1">MM</font> *<i>mm</i>, size_t <i>size</i>);</p>
<dd>This function allocates <i>size</i> bytes from the shared memory pool <i>mm</i> and returns either a (virtual memory word aligned) pointer to it or <tt>&quot;NULL&quot;</tt> in case of an error (out of memory). It behaves like the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) function but instead of allocating memory from the <i>heap</i> it allocates it from the shared memory segment underlying <i>mm</i>.</p>
<dt>void <code>mm_free</code>(<font SIZE="-1">MM</font> *<i>mm</i>, void *<i>ptr</i>);</p>
<dd>This deallocates the chunk starting at <i>ptr</i> in the shared memory pool <i>mm</i>. It behaves like the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-free/">free</a></i>(3) function but instead of deallocating memory from the <i>heap</i> it deallocates it from the shared memory segment underlying <i>mm</i>.</p>
<dt>void *<code>mm_realloc</code>(<font SIZE="-1">MM</font> *<i>mm</i>, void *<i>ptr</i>, size_t <i>size</i>);</p>
<dd>This function reallocates the chunk starting at <i>ptr</i> inside the shared memory pool <i>mm</i> with the new size of <i>size</i> bytes. It behaves like the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-realloc/">realloc</a></i>(3) function but instead of reallocating memory in the <i>heap</i> it reallocates it in the shared memory segment underlying <i>mm</i>.</p>
<dt>void *<code>mm_calloc</code>(<font SIZE="-1">MM</font> *<i>mm</i>, size_t <i>number</i>, size_t <i>size</i>);</p>
<dd>This is similar to <i><a href="/docs/linux/man/3-mm_malloc/">mm_malloc</a></i>(3), but additionally clears the chunk. It behaves like the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-calloc/">calloc</a></i>(3) function. It allocates space for <i>number</i> objects, each <i>size</i> bytes in length from the shared memory pool <i>mm</i>. The result is identical to calling <i><a href="/docs/linux/man/3-mm_malloc/">mm_malloc</a></i>(3) with an argument of &#8220;<i>number</i> * <i>size</i>&#8221;, with the exception that the allocated memory is initialized to nul bytes.</p>
<dt>char *<code>mm_strdup</code>(<font SIZE="-1">MM</font> *<i>mm</i>, const char *<i>str</i>);</p>
<dd>This function behaves like the <font SIZE="-1">POSIX</font>.1 <i><a href="/docs/linux/man/3-strdup/">strdup</a></i>(3) function. It allocates sufficient memory inside the shared memory pool <i>mm</i> for a copy of the string <i>str</i>, does the copy, and returns a pointer to it. The pointer may subsequently be used as an argument to the function <i><a href="/docs/linux/man/3-mm_free/">mm_free</a></i>(3). If insufficient shared memory is available, <tt>&quot;NULL&quot;</tt> is returned.</p>
<dt>size_t <code>mm_sizeof</code>(<font SIZE="-1">MM</font> *<i>mm</i>, const void *<i>ptr</i>);</p>
<dd>This function returns the size in bytes of the chunk starting at <i>ptr</i> when <i>ptr</i> was previously allocated with <i><a href="/docs/linux/man/3-mm_malloc/">mm_malloc</a></i>(3) inside the shared memory pool <i>mm</i>. The result is undefined when <i>ptr</i> was not previously allocated with <i><a href="/docs/linux/man/3-mm_malloc/">mm_malloc</a></i>(3).</p>
<dt>size_t <code>mm_maxsize</code>(void);</p>
<dd>This function returns the maximum size which is allowed as the first argument to the <i><a href="/docs/linux/man/3-mm_create/">mm_create</a></i>(3) function.</p>
<dt>size_t <code>mm_available</code>(<font SIZE="-1">MM</font> *<i>mm</i>);</p>
<dd>Returns the amount in bytes of still available (free) memory in the shared memory pool <i>mm</i>.</p>
<dt>char *<code>mm_error</code>(void);</p>
<dd>Returns the last error message which occurred inside the <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library.</p>
<dt>void <code>mm_display_info</code>(<font SIZE="-1">MM</font> *<i>mm</i>);</p>
<dd>This is debugging function which displays a summary page for the shared memory pool <i>mm</i> describing various internal sizes and counters.</dl>
<h2>Low-Level Shared Memory <font SIZE="-1">API</font></h2>
<dl COMPACT>
<dt>void *<code>mm_core_create</code>(size_t <i>size</i>, const char *<i>file</i>);</p>
<dd>This creates a shared memory area which is at least <i>size</i> bytes in size with the help of <i>file</i>. The value <i>size</i> has to be greater than 0 and less or equal the value returned by <i><a href="/docs/linux/man/3-mm_core_maxsegsize/">mm_core_maxsegsize</a></i>(3). Here <i>file</i> is a filesystem path to a file which need not to exist (and perhaps is never created because this depends on the platform and chosen shared memory and mutex implementation). The return value is either a (virtual memory word aligned) pointer to the shared memory segment or <tt>&quot;NULL&quot;</tt> in case of an error. The application is guaranteed to be able to access the shared memory segment from byte 0 to byte <i>size</i>-1 starting at the returned address.</p>
<dt>int <code>mm_core_permission</code>(void *<i>core</i>, mode_t <i>mode</i>, uid_t <i>owner</i>, gid_t <i>group</i>);</p>
<dd>This sets the filesystem <i>mode</i>, <i>owner</i> and <i>group</i> for the shared memory segment <i>code</i> (has effects only when the underlying shared memory segment implementation is actually based on external auxiliary files). The arguments are directly passed through to <i><a href="/docs/linux/man/2-chmod/">chmod</a></i>(2) and <i><a href="/docs/linux/man/2-chown/">chown</a></i>(2).</p>
<dt>void <code>mm_core_delete</code>(void *<i>core</i>);</p>
<dd>This deletes a shared memory segment <i>core</i> (as previously returned by a <i><a href="/docs/linux/man/3-mm_core_create/">mm_core_create</a></i>(3) call). After this operation, accessing the segment starting at <i>core</i> is no longer allowed and will usually lead to a segmentation fault.</p>
<dt>int <code>mm_core_lock</code>(const void *<i>core</i>, mm_lock_mode <i>mode</i>);</p>
<dd>This function acquires an advisory lock for the current process on the shared memory segment <i>core</i> for either shared/read-only (<i>mode</i> is <tt>&quot;MM_LOCK_RD&quot;</tt>) or exclusive/read-write (<i>mode</i> is <tt>&quot;MM_LOCK_RW&quot;</tt>) critical operations between <i><a href="/docs/linux/man/2-fork/">fork</a></i>(2)&#8217;ed child processes.</p>
<dt>int <code>mm_core_unlock</code>(const void *<i>core</i>);</p>
<dd>This function releases a previously acquired advisory lock for the current process on the shared memory segment <i>core</i>.</p>
<dt>size_t <code>mm_core_size</code>(const void *<i>core</i>);</p>
<dd>This returns the size in bytes of <i>core</i>. This size is exactly the size which was used for creating the shared memory area via <i><a href="/docs/linux/man/3-mm_core_create/">mm_core_create</a></i>(3). The function is provided just for convenience reasons to not require the application to remember the memory size behind <i>core</i> itself.</p>
<dt>size_t <code>mm_core_maxsegsize</code>(void);</p>
<dd>This returns the number of bytes of a maximum-size shared memory segment which is allowed to allocate via the <font SIZE="-1">MM</font> library. It is between a few <font SIZE="-1">KB</font> and the soft limit of 64MB.</p>
<dt>size_t <code>mm_core_align2page</code>(size_t <i>size</i>);</p>
<dd>This is just a utility function which can be used to align the number <i>size</i> to the next virtual memory <i>page</i> boundary used by the underlying platform. The memory page boundary under Unix platforms is usually somewhere between 2048 and 16384 bytes. You do not have to align the <i>size</i> arguments of other <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library functions yourself, because this is already done internally. This function is exported by the <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library just for convenience reasons in case an application wants to perform similar calculations for other purposes.</p>
<dt>size_t <code>mm_core_align2word</code>(size_t <i>size</i>);</p>
<dd>This is another utility function which can be used to align the number <i>size</i> to the next virtual memory <i>word</i> boundary used by the underlying platform. The memory word boundary under Unix platforms is usually somewhere between 4 and 16 bytes. You do not have to align the <i>size</i> arguments of other <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library functions yourself, because this is already done internally. This function is exported by the <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library just for convenience reasons in case an application wants to perform similar calculations for other purposes.</dl>
<h2>Low-Level Shared Memory <font SIZE="-1">API</font></h2>
<dl COMPACT>
<dt>void <code>mm_lib_error_set</code>(unsigned int, const char *str);</p>
<dd>This is a function which is used internally by the various <font SIZE="-1">MM</font> function to set an error string. It&#8217;s usually not called directly from applications.</p>
<dt>char *<code>mm_lib_error_get</code>(void);</p>
<dd>This is a function which is used internally by <i><a href="/docs/linux/man/3-mm_error/">MM_error</a></i>(3) and <i><a href="/docs/linux/man/3-mm_error/">mm_error</a></i>(3) functions to get the current error string. It is usually not called directly from applications.</p>
<dt>int <code>mm_lib_version</code>(void);</p>
<dd>This function returns a hex-value &#8220;0x<i>V</i><i></i><font SIZE="-1"><i>RR</i></font><i></i><i>T</i><i></i><font SIZE="-1"><i>LL</i></font><i></i>&#8221; which describes the current <font SIZE="-1"><code>OSSP</code></font><code> mm</code> library version. <i>V</i> is the version, <i></i><font SIZE="-1"><i>RR</i></font><i></i> the revisions, <i></i><font SIZE="-1"><i>LL</i></font><i></i> the level and <i>T</i> the type of the level (alphalevel=0, betalevel=1, patchlevel=2, etc). For instance <font SIZE="-1"><code>OSSP</code></font><code> mm</code> version 1.0.4 is encoded as 0x100204. The reason for this unusual mapping is that this way the version number is steadily <i>increasing</i>.</dl>
<h2>Restrictions</h2>
<p>The maximum size of a continuous shared memory segment one can allocate depends on the underlying platform. This cannot be changed, of course. But currently the high-level <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3)-style <font SIZE="-1">API</font> just uses a single shared memory segment as the underlying data structure for an <tt>&quot;MM&quot;</tt> object which means that the maximum amount of memory an <tt>&quot;MM&quot;</tt> object represents also depends on the platform. </p>
<p> This could be changed in later versions by allowing at least the high-level <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3)-style <font SIZE="-1">API</font> to internally use multiple shared memory segments to form the <tt>&quot;MM&quot;</tt> object. This way <tt>&quot;MM&quot;</tt> objects could have arbitrary sizes, although the maximum size of an allocatable continuous chunk still is bounded by the maximum size of a shared memory segment.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-mm-config/">mm-config</a></i>(1). </p>
<p> <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3), <i><a href="/docs/linux/man/3-calloc/">calloc</a></i>(3), <i><a href="/docs/linux/man/3-realloc/">realloc</a></i>(3), <i><a href="/docs/linux/man/3-strdup/">strdup</a></i>(3), <i><a href="/docs/linux/man/3-free/">free</a></i>(3), <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2), <i><a href="/docs/linux/man/2-shmget/">shmget</a></i>(2), <i><a href="/docs/linux/man/2-shmctl/">shmctl</a></i>(2), <i><a href="/docs/linux/man/2-flock/">flock</a></i>(2), <i><a href="/docs/linux/man/2-fcntl/">fcntl</a></i>(2), <i><a href="/docs/linux/man/2-semget/">semget</a></i>(2), <i><a href="/docs/linux/man/2-semctl/">semctl</a></i>(2), <i><a href="/docs/linux/man/2-semop/">semop</a></i>(2).</p>
<h2>Home</h2>
<p><a rel="nofollow" href="http://www.ossp.org/pkg/lib/mm/">http://www.ossp.org/pkg/lib/mm/</a></p>
<h2>History</h2>
<p>This library was originally written in January 1999 by <i>Ralf S. Engelschall</i> &lt;rse [at] engelschall.com&gt; for use in the <code>Extended </code><font SIZE="-1"><code>API</code></font> (<font SIZE="-1">EAPI</font>) of the <code>Apache</code> <font SIZE="-1">HTTP</font> server project (see <a rel="nofollow" href="http://www.apache.org/">http://www.apache.org/</a>), which was originally invented for <code>mod_ssl</code> (see <a rel="nofollow" href="http://www.modssl.org/">http://www.modssl.org/</a>). </p>
<p> Its base idea (a malloc-style <font SIZE="-1">API</font> for handling shared memory) was originally derived from the non-publically available <i>mm_malloc</i> library written in October 1997 by <i>Charles Randall</i> &lt;crandall [at] matchlogic.com&gt; for MatchLogic, Inc. </p>
<p> In 2000 this library joined the <font SIZE="-1"><code>OSSP</code></font> project where all other software development projects of <i>Ralf S. Engelschall</i> are located.</p>
<h2>Author</h2>
<pre> Ralf S. Engelschall
 rse [at] engelschall.com
 <a rel="nofollow" href="http://www.engelschall.com">www.engelschall.com</a></pre>
