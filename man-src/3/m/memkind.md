---
title: "memkind(3)"
name: "memkind"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind/"
description: "memkind – Heap manager that enables allocations to memory with different properties. This header expose EXPERIMENTAL API in except of STANDARD API placed in section LIBRARY VERSION. API Standards a..."
---

<h2>NAME</h2>
<p> memkind &#8211; Heap manager that enables allocations to memory with different properties.<br />
 This header expose EXPERIMENTAL API in except of STANDARD API placed in section LIBRARY VERSION. API Standards are described below in this man page.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind.h&gt;
Link with - lmemkind
                ERROR HANDLING : void
                                 memkind_error_message(int err, char *msg, size_t size);
HEAP MANAGEMENT :

    void *
    memkind_malloc(memkind_t kind, size_t size);

void *memkind_calloc(memkind_t kind, size_t num, size_t size);

void *memkind_realloc(memkind_t kind, void *ptr, size_t size);

int memkind_posix_memalign(memkind_t kind, void **memptr, size_t alignment, size_t size);

void memkind_free(memkind_t kind, void *ptr);

ALLOCATOR CALLBACK FUNCTION :

    void *
    memkind_partition_mmap(int partition, void *addr, size_t size);
(DEPRECATED)
    KIND MANAGMENT :

    int memkind_create(const struct memkind_ops *ops, const char *name, memkind_t *kind);
(DEPRECATED)

    int memkind_create_pmem(const char *dir, size_t max_size, memkind_t *kind);

int memkind_finalize(void);
(DEPRECATED)

    int memkind_get_num_kind(int *num_kind);
(DEPRECATED)

    int memkind_get_kind_by_partition(int partition, memkind_t *kind);
(DEPRECATED)

    int memkind_get_kind_by_name(const char *name, memkind_t *kind);
(DEPRECATED)

    int memkind_get_size(memkind_t kind, size_t *total, size_t *free);
(DEPRECATED)

    int memkind_check_available(memkind_t kind);
DECORATORS :

    void
    memkind_malloc_pre(memkind_t *kind, size_t *size);

void memkind_malloc_post(memkind_t kind, size_t size, void **result);

void memkind_calloc_pre(memkind_t *kind, size_t *nmemb, size_t *size);

void memkind_calloc_post(memkind_t kind, size_t nmemb, size_t size, void **result);

void memkind_posix_memalign_pre(memkind_t *kind, void **memptr, size_t *alignment, size_t *size);

void memkind_posix_memalign_post(memkind_t kind, void **memptr, size_t alignment, size_t size, int *err);

void memkind_realloc_pre(memkind_t *kind, void **ptr, size_t *size);

void memkind_realloc_post(memkind_t kind, void *ptr, size_t size, void **result);

void memkind_free_pre(memkind_t *kind, void **ptr);

void memkind_free_post(memkind_t kind, void *ptr);
LIBRARY VERSION : int memkind_get_version();
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>memkind_error_message</code>() converts an error number <i>err</i> returned by a member of the memkind interface to an error message <i>msg</i> where the maximium size of the message is passed by the <i>size</i> parameter. </p>
<p> <code>HEAP MANAGMENT:</code><br />
 The functions described in this section define a heap manager with an interface modeled on the ISO C standard API&#8217;s, except that the user must specify the <i>kind</i> of memory with the first argument to each function. See the <code>KINDS</code> section below for a full description of the implemented kinds. </p>
<p> <code>memkind_malloc</code>() allocates <i>size</i> bytes of uninitialized memory of the specified <i>kind</i>. The allocated space is suitably aligned (after possible pointer coercion) for storage of any type of object. If <i>size</i> is 0, then <code>memkind_malloc</code>() returns NULL. </p>
<p> <code>memkind_calloc</code>() allocates space for <i>num</i> objects each <i>size</i> bytes in length in memory of the specified <i>kind</i>. The result is identical to calling <code>memkind_malloc</code>() with an argument of <i>num</i>*<i>size</i>, with the exception that the allocated memory is explicitly initialized to zero bytes. If <i>num</i> or <i>size</i> is 0, then <code>memkind_calloc</code>() returns NULL. </p>
<p> <code>memkind_realloc</code>() changes the size of the previously allocated memory referenced by <i>ptr</i> to <i>size</i> bytes of the specified <i>kind</i>. The contents of the memory are unchanged up to the lesser of the new and old sizes. If the new size is larger, the contents of the newly allocated portion of the memory are undefined. Upon success, the memory referenced by <i>ptr</i> is freed and a pointer to the newly allocated high bandwidth memory is returned. </p>
<p> <code>Note:</code> <code>memkind_realloc</code>() may move the memory allocation, resulting in a different return value than <i>ptr</i>. </p>
<p> If <i>ptr</i> is NULL, the <code>memkind_realloc</code>() function behaves identically to <code>memkind_malloc</code>() for the specified size. The address <i>ptr</i>, if not NULL, must have been returned by a previous call to <code>memkind_malloc</code>(), <code>memkind_calloc</code>(), <code>memkind_realloc</code>(), or <code>memkind_posix_memalign</code>() with the same <i>kind</i> as specified to the call to <code>memkind_realloc</code>(). Otherwise, if <i>memkind_free(kind, ptr)</i> was called before, undefined behavior occurs. </p>
<p> <code>memkind_posix_memalign</code>() allocates <i>size</i> bytes of memory of a specified <i>kind</i> such that the allocation&#8217;s base address is an even multiple of <i>alignment</i>, and returns the allocation in the value pointed to by <i>memptr</i>. The requested <i>alignment</i> must be a power of 2 at least as large as <i>sizeof(void *)</i>. If <i>size</i> is 0, then <code>memkind_posix_memalign</code>() returns NULL. </p>
<p> <code>memkind_free</code>() causes the allocated memory referenced by <i>ptr</i> to be made available for future allocations. This pointer must have been returned by a previous call to <code>memkind_malloc</code>(), <code>memkind_calloc</code>(), <code>memkind_realloc</code>(), or <code>memkind_posix_memalign</code>(). Otherwise, if <i>memkind_free(kind, ptr)</i> was already called before, undefined behavior occurs. If <i>ptr</i> is NULL, no operation is performed. The value of <code>MEMKIND_DEFAULT</code> can be given as the <i>kind</i> for all buffers allocated by a kind that leverages the jemalloc allocator. This includes all interally defined kinds other than those that use gigabyte pages. In cases where the kind is unknown in the context of the call to <code>memkind_free</code>() <code>0</code> can be given as the <i>kind</i> specified to <code>memkind_free</code>() but this will require a look up that can be bypassed by specifying a non-zero value. </p>
<p> <code>ALLOCATOR CALLBACK FUNCTION:</code><br />
 This section describes the memkind interface which is used internally by the heap manager. For this API the kind is determined by the partition index. This enables the underlying heap manager to call routines with standard type arguments, and allows the heap manager implementation to be independent of the specifics of the <i>memkind_t</i> implementation. Currently there is only one callback function. </p>
<p> <code>memkind_partition_mmap</code>() which is a wrapper around the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call. The hint address <i>addr</i> and the length in bytes of the buffer to be allocated <i>size</i> are passed through to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). The other <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) parameters are determined by the kind operations. </p>
<p> <code>KIND MANAGEMENT:</code><br />
 There are built-in kinds that are always available, and these are enumerated in the <code>KINDS</code> section. The user can also create their own kinds of memory. This section describes the API&#8217;s that enable the tracking of the different kinds of memory and determining their properties. </p>
<p> <code>memkind_create</code>()<code>(DEPRECATED)</code> is used to create a new kind of memory. It takes as input a pointer to a vtable called <i>ops</i> that determines the operations that define the kind of memory. These operations can be taken from one of the memkind built-in implementations defined in the memkind headers, or it can be user implemented. The requirements for each operation is defined in the <code>MEMKIND OPERATIONS</code> section. See the <code>SEE ALSO</code> section for the list of memkind header files that implement the built-in operations: each header has a man page. </p>
<p> <code>memkind_create_pmem</code>() is a convenience function used to create a file-backed kind of memory. It allocates a temporary file in the given directory <i>dir</i>. The file is created in a fashion similar to <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3), so that the file name does not appear when the directory is listed and the space is automatically freed when the program terminates. The file is truncated to a size of <i>max_size</i> bytes and the resulting space is memory-mapped. Then, the actual pmem <i>kind</i> is created by calling <code>memkind_create</code>() with a unique <i>name</i> string (&quot;pmemXXXXXXXX&quot;), and the pointer to <code>MEMKIND_PMEM_OPS</code> as <i>ops</i> argument.<br />
 Note that the actual file system space is not allocated immediately, but only on a call to <code>memkind_pmem_mmap</code>() (see <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3)). This allows to create a pmem memkind of a pretty large size without the need to reserve in advance the corresponding file system space for the entire heap. The minimum <i>max_size</i> value allowed by the library is defined in <code>&lt;memkind_pmem.h&gt;</code> as <code>MEMKIND_PMEM_MIN_SIZE</code>. Calling <code>memkind_create_pmem</code>() with a size smaller than that will return an error. The maximum allowed size is not limited by <code>memkind</code>, but by the file system specified by the <i>dir</i> argument. The <i>max_size</i> passed in is the raw size of the memory pool and <code>jemalloc</code> will use some of that space for its own metadata. </p>
<p> <code>memkind_finalize</code>() releases all resources associated with the memkind library including the resouces used by all of the kinds that were created, but it does not free memory allocated with the <code>HEAP MANAGEMENT</code> interface. This must be the last call to the memkind library before application termination, but it can be called more than once. </p>
<p> <code>memkind_get_num_kind</code>() sets <i>num_kind</i> to the number of available kinds of memory. This accounts for the built-in static kinds and any dynamically created kinds. Since there is a one-to-one mapping between partitions and kinds, this is also the number of partitions. </p>
<p> <code>memkind_get_kind_by_partition</code>() sets <i>kind</i> to the memory kind associated with the <i>partition</i> index which must be in the range [0, <i>num_kind</i> &#8211; 1] where num_kind can be retrieved with the <code>memkind_get_num_kind</code>() function. </p>
<p> <code>memkind_get_kind_by_name</code>() sets <i>kind</i> to the memory kind associated with the <i>name</i> string specified. All of the built-in kinds have name strings that are the lower-case version of name given in the <code>KINDS</code> section (for example: MEMKIND_DEFAULT has <i>name</i> &quot;memkind_default&quot;) </p>
<p> <code>memkind_get_size</code>()<code>(DEPRECATED)</code> sets <i>total</i> to the number of bytes on the system which can be allocated with the specified <i>kind</i>, and sets <i>free</i> to the number of unallocated bytes available of memory with the specified <i>kind.</i> </p>
<p> <code>Note:</code> These numbers may be specific to the CPU of the calling thread if the <i>kind</i> binds memory to NUMA nodes associated with the CPU. </p>
<p> <code>memkind_check_available</code>() Returns a zero if the specified <i>kind</i> is available or an error code from the <code>ERRORS</code> section if it is not. </p>
<p> <code>DECORATORS:</code><br />
 The memkind library enables the user to define decorator functions that can be called before and after each memkind heap management API. The decorators that are called at the beginning of the function end are named after that function with <i>_pre</i> appended to the name, and those that are called at the end of the function are named after that function with <i>_post</i> appended to the name. These are weak symbols, and if they are not present at link time they are not called. The memkind library does not define these symbols which are reserved for user definition. These decorators can be used to track calls to the heap management interface or to modify parameters. The decorators that are called at the beginning of the allocator pass all inputs by reference, and the decorators that are called at the end of the allocator pass the output by reference. This enables the modification of the input and output of each heap management function by the decorators. </p>
<p> <code>LIBRARY VERSION</code><br />
 The memkind library version scheme consist major, minor and patch numbers separated by dot. Combining those numbers, we got the following representation:<br />
 major.minor.patch, where:<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-major number is incremented whenever API is changed (loss of backward compatibility),</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-minor number is incremented whenever additional extensions are introduced, or behavior has been changed,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-patch number is incremented whenever small bug fixes are added.</p>
<p> memkind library provide numeric representation of the version by exposing the following API:<br />
 int memkind_get_version() return version number represented by a single integer number, obtained from the formula:<br />
 major * 1000000 + minor * 1000 + patch </p>
<p> Note: major &lt; 1 means unstable API. </p>
<p> API standards:<br />
 -STANDARD API, API is considered as stable<br />
 -NON-STANDARD API, API is considered as stable, however this is not a standard way to use memkind<br />
 -EXPERIMENTAL API, API is considered as unstable and the subject to change </p>
<p> <code>MEMKIND OPERATIONS:</code><br />
 The <i>memkind_ops</i> structure is a vtable that defines the operations which determine the kind of memory. This design pattern is modeled after the &quot;mix-in&quot; pattern used in the Linux kernel to enable some of the features of an object oriented language in C. This section defines the inputs, outputs and responsiblities of each function pointer enumerated in the <i>memkind_ops</i> structure. Each of these methods takes a <code>memkind_t</code> argument as its first parameter which shall be self referencing. In this documentation the function pointers in the <i>memkind_ops</i> structure will be prepended with &quot;<code>ops.</code>&quot; and should be considered the operation associated with the <i>kind</i>. </p>
<p> <code>int ops.create(memkind_t </code><i>kind</i><code>, const struct memkind_ops </code><i>*ops</i><code>, const char </code><i>*name</i><code>);</code><br />
 shall instantiate all of the dynamic resources associated with the <i>kind</i>. It takes a pointer to the vtable structure <i>ops</i> which has a function pointer for each of methods defined in this section of the man page. If any methods are unnessary to the implementation of the <i>kind</i> these function pointers shall be set to <code>NULL</code>. The <i>name</i> string is an input parameter that identifies the kind of memory so that it can be fetched with the <code>memkind_get_kind_by_name</code>() function. Typically this method is either a pointer to the function <code>memkind_default_create</code>() defined in <i>&lt;memkind_default.h&gt;</i>, or a function that calls <code>memkind_default_create</code>() before performing other setup. </p>
<p> <code>int ops.destroy(memkind_t </code><i>kind</i><code>);</code><br />
 shall free all of the dynamic resources reserved by the <code>ops.create</code>() method. If no dynamic resources were explicitly allocated in the <i>ops.create</i>() method, this pointer can be set to <code>NULL</code>. </p>
<p> <code>void *ops.malloc(memkind_t </code><i>kind</i><code>, size_t </code><i>size</i><code>);</code><br />
 shall implement <code>memkind_malloc</code>(), as described above. </p>
<p> <code>void *ops.calloc(memkind_t </code><i>kind</i><code>, size_t </code><i>num</i><code>, size_t </code><i>size</i><code>);</code><br />
 shall implement <code>memkind_calloc</code>(), as described above. </p>
<p> <code>int ops.posix_memalign(memkind_t </code><i>kind</i><code>, void </code><i>**memptr</i><code>, size_t </code><i>alignment</i><code>, size_t </code><i>size</i><code>);</code><br />
 shall implement <code>memkind_posix_memalign</code>(), as described above. </p>
<p> <code>void *ops.realloc(memkind_t </code><i>kind</i><code>, void </code><i>*ptr</i><code>, size_t </code><i>size</i><code>);</code><br />
 shall implement <code>memkind_realloc</code>(), as described above. </p>
<p> <code>void ops.free(memkind_t </code><i>kind</i><code>, void </code><i>*ptr</i><code>);</code><br />
 shall implement <code>memkind_free</code>(), as described above. </p>
<p> <code>void *ops.mmap(memkind_t </code><i>kind</i><code>, void </code><i>*addr</i><code>, size_t </code><i>size</i><code>);</code> shall wrap the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) and <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) system calls while passing <i>addr</i> and <i>size</i> through and determining all other parameters for <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) and <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) by calling other functions resolved by the <code>kind.ops</code> vtable. This function shall return a virtual address to the memory mapped, or <code>MAP_FAILED</code> as defined in <i>&lt;sys/mman.h&gt;</i> which is <i>(void *) -1</i>. </p>
<p> <code>int ops.mbind(memkind_t </code><i>kind</i><code>, void </code><i>*ptr</i><code>, size_t </code><i>size</i><code>);</code><br />
 shall wrap the <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) system call and pass through the start address <i>ptr</i> to be bound, and the number of bytes <i>size</i> from that address to be bound. The other parmeters to <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) shall be determined by calling other functions resolved by the <code>kind.ops</code> vtable. </p>
<p> <code>int ops.madvise(memkind_t </code><i>kind</i><code>, void </code><i>*addr</i><code>, size_t </code><i>size</i><code>);</code><br />
 shall wrap the <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) system call and pass through the start address <i>addr</i> to be advised, and the number of bytes <i>size</i> from that address to be advised. This may call <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) multiple times with different advice. </p>
<p> <code>int ops.get_mmap_flags(memkind_t </code><i>kind</i><code>, int </code><i>*flags</i><code>);</code><br />
 shall set <i>flags</i> to a value appropriate for passing to the <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) system call for the <i>kind</i>. </p>
<p> <code>int ops.get_mbind_mode(memkind_t </code><i>kind</i><code>, int </code><i>*mode</i><code>);</code><br />
 shall set <i>mode</i> to a value appropriate for passing to the <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) system call for the <i>kind</i>. </p>
<p> <code>int ops.get_mbind_nodemask(memkind_t </code><i>kind</i><code>, unsigned long </code><i>*nodemask</i><code>, unsigned long </code><i>maxnode</i><code>);</code><br />
 shall set the <i>nodemask</i> of length <i>maxnode</i> bits to a value appropriate for passing to the <i><a href="/docs/linux/man/2-mbind/">mbind</a></i>(2) system call for the <i>kind</i>. </p>
<p> <code>int ops.get_arena(memkind_t </code><i>kind</i><code>, unsigned int </code><i>*arena, </i><code>size_t</code><i> size );</i><br />
 shall set <i>arena</i> to an index appropriate for the <i>kind,</i> allocation <i>size,</i> and CPU when using the jemalloc arena allocation through the <code>jemk_mallocx</code>() API. Size parameter is not used at the moment, but will be necesary for integration with jemalloc 4.0.x (planned for one of the future releases). </p>
<p> <code>int ops.get_size(memkind_t </code><i>kind</i><code>, size_t </code><i>*total</i><code>, size_t </code><i>*free</i><code>);</code><br />
 shall implement <code>memkind_get_size</code>(), as described above. </p>
<p> <code>int ops.check_available(memkind_t </code><i>kind</i><code>);</code><br />
 shall return 0 if the <i>kind</i> is available on the system, and an error code if not. </p>
<p> <code>int ops.check_addr(memkind_t </code><i>kind</i><code>, void </code><i>*addr</i><code>);</code><br />
 shall return 0 if the <i>addr</i> can be freed with the specified <i>kind</i> and an error code otherwise. If the memory cannot be freed with <code>jemk_free</code>(), then at least one of the instantiated kinds must return 0 to enable freeing. </p>
<p> <code>void ops.init_once(void);</code><br />
 this function pointer shall be set to NULL for any kind that is not built-in. The method is used to allocate dynamic resources for built-in kinds without requiring and initialization routine.</p>
<h2>RETURN VALUE</h2>
<p> <code>memkind_calloc</code>(), <code>memkind_malloc</code>(), and <code>memkind_realloc</code>(), return the pointer to the allocated memory, or NULL if the request fails. <code>memkind_free</code>() and <code>memkind_error_message</code>() do not have return values. All other memkind API&#8217;s return 0 upon success, and an error code defined in the ERRORS section upon failure. The memkind library avoids setting <i>errno</i> directly, but calls to underlying libraries and system calls may set <i>errno</i>.</p>
<h2>KINDS</h2>
<p> The available kinds of memory</p>
<dl>
<dt><code>MEMKIND_DEFAULT</code></p>
<dd> Default allocation using standard memory and default page size.</p>
<dt><code>MEMKIND_HUGETLB</code></p>
<dd> Allocate from standard memory using huge pages. Note: This kind requires huge pages configuration described in SYSTEM CONFIGURATION section.</p>
<dt><code>MEMKIND_GBTLB</code></p>
<dd> Allocate from standard memory using giga byte huge pages. Note: This kind requires gigabyte pages configuration described in SYSTEM CONFIGURATION section.</p>
<dt><code>MEMKIND_INTERLEAVE</code></p>
<dd> Allocate pages interleaved across all NUMA nodes with transparent huge pages disabled.</p>
<dt><code>MEMKIND_HBW</code></p>
<dd> Allocate from the closest high bandwidth memory NUMA node at time of allocation. If there is not enough high bandwidth memory to satisfy the request <i>errno</i> is set to ENOMEM and the allocated poitner is set to NULL.</p>
<dt><code>MEMKIND_HBW_HUGETLB</code></p>
<dd> Same as <code>MEMKIND_HBW</code> except the allocation is backed by huge pages. Note: This kind requires huge pages configuration described in SYSTEM CONFIGURATION section.</p>
<dt><code>MEMKIND_HBW_PREFERRED</code></p>
<dd> Same as <code>MEMKIND_HBW</code> except that if there is not enough high bandwidth memory to satisfy the request, the allocation will fall back on standard memory.</p>
<dt><code>MEMKIND_HBW_PREFERRED_HUGETLB</code></p>
<dd> Same as <code>MEMKIND_HBW_PREFERRED</code> except the allocation is backed by huge pages. Note: This kind requires huge pages configuration described in SYSTEM CONFIGURATION section.</p>
<dt><code>MEMKIND_HBW_GBTLB</code></p>
<dd> Same as <code>MEMKIND_HBW</code> except the allocation is backed by one gigabyte huge pages. Note that <i>size</i> can take on any value, but full gigabyte pages will allocated for each request, so remainder of the last page will be wasted. A good use case scenario is to grow a buffer in the course of an application with reallocs. In this case, if there is enough memory available within in already allocated gigabyte page, newer pages are not fetched. This is demonstrated in the examples directory with gb_realloc_example.c This kind requires gigabyte pages configuration described in SYSTEM CONFIGURATION section.</p>
<dt><code>MEMKIND_HBW_PREFERRED_GBTLB</code></p>
<dd> Same as <code>MEMKIND_HBW_GBTLB</code> except that if there is not enough high bandwidth memory to satisfy the request, the allocation will fall back on standard memory. Note: This kind requires gigabyte pages configuration described in SYSTEM CONFIGURATION section.</p>
<dt><code>MEMKIND_HBW_INTERLEAVE</code></p>
<dd> Same as <code>MEMKIND_HBW</code> except that the pages that support the allocation are interleaved across all high bandwidth nodes and transparent huge pages are disabled.</dl>
<h2>ERRORS</h2>
<dl>
<dt><code>memkind_posix_memalign</code>()</p>
<dd> returns the one of the POSIX standard error codes <code>EINVAL</code> or <code>ENOMEM</code> as defined in <i>&lt;errno.h&gt;</i> if an error occurs (these have positive values). If the <i>alignment</i> parameter is not a power of two, or is not a multiple of <i>sizoeof(void *)</i>, then <code>EINVAL</code> is returned. If there is insufficient memory to satisfy the request then <code>ENOMEM</code> is returned.</dl>
<p> All functions other than <code>memkind_posix_memalign</code>() which have an integer return type return one of the negative error codes as defined in <i>&lt;memkind.h&gt;</i> and described below.</p>
<dl>
<dt><code>MEMKIND_ERROR_UNAVAILABLE</code></p>
<dd> Requested memory kind is not available</p>
<dt><code>MEMKIND_ERROR_MBIND</code></p>
<dd> Call to <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) failed</p>
<dt><code>MEMKIND_ERROR_MMAP</code></p>
<dd> Call to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) failed</p>
<dt><code>MEMKIND_ERROR_MEMALIGN (DEPRECATED)</code></p>
<dd> Call to <code>jemk_posix_memalign</code>() failed</p>
<dt><code>MEMKIND_ERROR_MALLCTL (DEPRECATED)</code></p>
<dd> Call to <code>jemk_mallctl</code>() failed</p>
<dt><code>MEMKIND_ERROR_MALLOC</code></p>
<dd> Call to <code>jemk_malloc</code>() failed</p>
<dt><code>MEMKIND_ERROR_GETCPU (DEPRECATED)</code></p>
<dd> Call to <code>sched_getcpu</code>() returned out of range</p>
<dt><code>MEMKIND_ERROR_TIEDISTANCE (DEPRECATED)</code></p>
<dd> Two NUMA memory nodes are equidistant from target cpu node</p>
<dt><code>MEMKIND_ERROR_ALIGNMENT (DEPRECATED)</code></p>
<dd> Alignment must be a power of two and larger than sizeof(void *)</p>
<dt><code>MEMKIND_ERROR_ALLOCM</code></p>
<dd> Call to <code>jemk_allocm</code>() failed</p>
<dt><code>MEMKIND_ERROR_ENVIRON</code></p>
<dd> Error parsing environment variable (MEMKIND_*)</p>
<dt><code>MEMKIND_ERROR_INVALID</code></p>
<dd> Invalid input arguments to memkind routine</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/bin/memkind-hbw-nodes</i></p>
<dd> Prints a comma separated list of high bandwidth nodes.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MEMKIND_HBW_NODES</code></p>
<dd> This environment variable is a comma separated list of NUMA nodes that are treated as high bandwidth. Uses the <i>libnuma</i> routine <code>numa_parse_nodestring</code>() for parsing, so the syntax described in the <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3) man page for this routine applies: e.g 1-3,5 is a valid setting.</p>
<dt><code>MEMKIND_ARENA_NUM_PER_KIND</code></p>
<dd> This environment variable allows leveraging internal mechanism of the library for setting number of arenas per kind. Value should be a positive integer (not greater than INT_MAX defined in limits.h). The user should set the value based on the characteristics of application that is using the library. Higher value can provide better performance in extremely multithreaded applications at the cost of memory overhead. See section &quot;IMPLEMENTATION NOTES&quot; of <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3) for more details about arenas.</p>
<dt><code>MEMKIND_DEBUG</code></p>
<dd> Controls logging mechanism in memkind. Setting <code>MEMKIND_DEBUG</code> to &quot;1&quot; enables printing messages like errors and general informations about environment to <i>stderr.</i></dl>
<h2>SYSTEM CONFIGURATION</h2>
<p> Interfaces for obtaining 2MB and 1GB pages (HUGETLB and GBTLB) need allocated huge pages in the kernel&#8217;s huge page pool.</p>
<dl>
<dt><code>HUGETLB (huge pages)</code></p>
<dd> Current number of &quot;persistent&quot; huge pages can be read from /proc/sys/vm/nr_hugepages file. Proposed way of setting hugepages is: &quot;sudo sysctl vm.nr_hugepages=&lt;number_of_hugepages&gt;&quot;. More informations can be found here: <a rel="nofollow" href="https://www.kernel.org/doc/Documentation/vm/hugetlbpage.txt">https://www.kernel.org/doc/Documentation/vm/hugetlbpage.txt</a></p>
<dt><code>GBTLB (gigabyte pages)</code></p>
<dd> Number of preallocated gigabyte pages can be read from /proc/cmdline (hugepagesz=1G nr_hugepages=N). Setting gigabyte hugepages is available by kernel commandline. From 3.16 and later kernels, users can allocate gigabyte pages like its done for 2MB pages.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/3-memkind_default/">memkind_default</a></code>(3), <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hbw/">memkind_hbw</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hugetlb/">memkind_hugetlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_gbtlb/">memkind_gbtlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3) </p>
<h2>Index</h2>
