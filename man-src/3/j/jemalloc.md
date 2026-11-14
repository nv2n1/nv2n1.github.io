---
title: "jemalloc(3)"
name: "jemalloc"
section: "3"
letter: "j"
url: "/docs/linux/man/3-jemalloc/"
description: "jemalloc – general purpose memory allocation functions"
---

<h2 class="name">NAME</h2>
<p> jemalloc &#8211; general purpose memory allocation functions </p>
<h2>LIBRARY</h2>
<p> This manual describes jemalloc 3.6.0-0-g46c0af68bd248b04df75e4f92d5fb804c3d75340. More information can be found at the m[blue]<code>jemalloc website</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;jemalloc/jemalloc.h&gt;
#include &lt;stdlib.h&gt;
</code></pre>
<h3>Standard API</h3>
<dl>
<dt> <code>void *malloc(size_t&nbsp;<wbr></code><i>size</i><code>);</code></p>
<dt> <code>void *calloc(size_t&nbsp;<wbr></code><i>number</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>);</code></p>
<dt> <code>int posix_memalign(void&nbsp;<wbr>**</code><i>ptr</i><code>, size_t&nbsp;<wbr></code><i>alignment</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>);</code></p>
<dt> <code>void *aligned_alloc(size_t&nbsp;<wbr></code><i>alignment</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>);</code></p>
<dt> <code>void *realloc(void&nbsp;<wbr>*</code><i>ptr</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>);</code></p>
<dt> <code>void free(void&nbsp;<wbr>*</code><i>ptr</i><code>);</code></dl>
<h3>Non-standard API</h3>
<dl>
<dt> <code>void *mallocx(size_t&nbsp;<wbr></code><i>size</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>void *rallocx(void&nbsp;<wbr>*</code><i>ptr</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>size_t xallocx(void&nbsp;<wbr>*</code><i>ptr</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, size_t&nbsp;<wbr></code><i>extra</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>size_t sallocx(void&nbsp;<wbr>*</code><i>ptr</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>void dallocx(void&nbsp;<wbr>*</code><i>ptr</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>size_t nallocx(size_t&nbsp;<wbr></code><i>size</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>int mallctl(const char&nbsp;<wbr>*</code><i>name</i><code>, void&nbsp;<wbr>*</code><i>oldp</i><code>, size_t&nbsp;<wbr>*</code><i>oldlenp</i><code>, void&nbsp;<wbr>*</code><i>newp</i><code>, size_t&nbsp;<wbr></code><i>newlen</i><code>);</code></p>
<dt> <code>int mallctlnametomib(const char&nbsp;<wbr>*</code><i>name</i><code>, size_t&nbsp;<wbr>*</code><i>mibp</i><code>, size_t&nbsp;<wbr>*</code><i>miblenp</i><code>);</code></p>
<dt> <code>int mallctlbymib(const size_t&nbsp;<wbr>*</code><i>mib</i><code>, size_t&nbsp;<wbr></code><i>miblen</i><code>, void&nbsp;<wbr>*</code><i>oldp</i><code>, size_t&nbsp;<wbr>*</code><i>oldlenp</i><code>, void&nbsp;<wbr>*</code><i>newp</i><code>, size_t&nbsp;<wbr></code><i>newlen</i><code>);</code></p>
<dt> <code>void malloc_stats_print(void&nbsp;<wbr></code><i>(*write_cb)</i><code>&nbsp;<wbr>(void&nbsp;<wbr>*, const char&nbsp;<wbr>*), void&nbsp;<wbr>*</code><i>cbopaque</i><code>, const char&nbsp;<wbr>*</code><i>opts</i><code>);</code></p>
<dt> <code>size_t malloc_usable_size(const void&nbsp;<wbr>*</code><i>ptr</i><code>);</code></p>
<dt> <code>void (*malloc_message)(void&nbsp;<wbr>*</code><i>cbopaque</i><code>, const char&nbsp;<wbr>*</code><i>s</i><code>);</code></dl>
<dd>const char *<i>malloc_conf</i>;</p>
<h3>Experimental API</h3>
<dl>
<dt> <code>int allocm(void&nbsp;<wbr>**</code><i>ptr</i><code>, size_t&nbsp;<wbr>*</code><i>rsize</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>int rallocm(void&nbsp;<wbr>**</code><i>ptr</i><code>, size_t&nbsp;<wbr>*</code><i>rsize</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, size_t&nbsp;<wbr></code><i>extra</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>int sallocm(const void&nbsp;<wbr>*</code><i>ptr</i><code>, size_t&nbsp;<wbr>*</code><i>rsize</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>int dallocm(void&nbsp;<wbr>*</code><i>ptr</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></p>
<dt> <code>int nallocm(size_t&nbsp;<wbr>*</code><i>rsize</i><code>, size_t&nbsp;<wbr></code><i>size</i><code>, int&nbsp;<wbr></code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<h3>Standard API</h3>
<dd>The <code>malloc</code> function allocates <i>size</i> bytes of uninitialized memory. The allocated space is suitably aligned (after possible pointer coercion) for storage of any type of object. </p>
<p> The <code>calloc</code> function allocates space for <i>number</i> objects, each <i>size</i> bytes in length. The result is identical to calling <code>malloc</code> with an argument of <i>number</i> * <i>size</i>, with the exception that the allocated memory is explicitly initialized to zero bytes. </p>
<p> The <code>posix_memalign</code> function allocates <i>size</i> bytes of memory such that the allocation&#8217;s base address is an even multiple of <i>alignment</i>, and returns the allocation in the value pointed to by <i>ptr</i>. The requested <i>alignment</i> must be a power of 2 at least as large as sizeof(<code>void *</code>). </p>
<p> The <code>aligned_alloc</code> function allocates <i>size</i> bytes of memory such that the allocation&#8217;s base address is an even multiple of <i>alignment</i>. The requested <i>alignment</i> must be a power of 2. Behavior is undefined if <i>size</i> is not an integral multiple of <i>alignment</i>. </p>
<p> The <code>realloc</code> function changes the size of the previously allocated memory referenced by <i>ptr</i> to <i>size</i> bytes. The contents of the memory are unchanged up to the lesser of the new and old sizes. If the new size is larger, the contents of the newly allocated portion of the memory are undefined. Upon success, the memory referenced by <i>ptr</i> is freed and a pointer to the newly allocated memory is returned. Note that <code>realloc</code> may move the memory allocation, resulting in a different return value than <i>ptr</i>. If <i>ptr</i> is <code>NULL</code>, the <code>realloc</code> function behaves identically to <code>malloc</code> for the specified size. </p>
<p> The <code>free</code> function causes the allocated memory referenced by <i>ptr</i> to be made available for future allocations. If <i>ptr</i> is <code>NULL</code>, no action occurs.</p>
<h3>Non-standard API</h3>
<p> The <code>mallocx</code>, <code>rallocx</code>, <code>xallocx</code>, <code>sallocx</code>, <code>dallocx</code>, and <code>nallocx</code> functions all have a <i>flags</i> argument that can be used to specify options. The functions only check the options that are contextually relevant. Use bitwise or (|) operations to specify one or more of the following: </p>
<p> <code>MALLOCX_LG_ALIGN(</code><i>la</i><code>) </code></p>
<dl>
<dt>
<dd> Align the memory allocation to start at an address that is a multiple of (1 &lt;&lt; <i>la</i>). This macro does not validate that <i>la</i> is within the valid range.</dl>
<p> <code>MALLOCX_ALIGN(</code><i>a</i><code>) </code></p>
<dl>
<dt>
<dd> Align the memory allocation to start at an address that is a multiple of <i>a</i>, where <i>a</i> is a power of two. This macro does not validate that <i>a</i> is a power of 2.</dl>
<p> <code>MALLOCX_ZERO</code></p>
<dl>
<dt>
<dd> Initialize newly allocated memory to contain zero bytes. In the growing reallocation case, the real size prior to reallocation defines the boundary between untouched bytes and those that are initialized to contain zero bytes. If this macro is absent, newly allocated memory is uninitialized.</dl>
<p> <code>MALLOCX_ARENA(</code><i>a</i><code>) </code></p>
<dl>
<dt>
<dd> Use the arena specified by the index <i>a</i> (and by necessity bypass the thread cache). This macro has no effect for huge regions, nor for regions that were allocated via an arena other than the one specified. This macro does not validate that <i>a</i> specifies an arena index in the valid range.</dl>
<p> The <code>mallocx</code> function allocates at least <i>size</i> bytes of memory, and returns a pointer to the base address of the allocation. Behavior is undefined if <i>size</i> is <code>0</code>, or if request size overflows due to size class and/or alignment constraints. </p>
<p> The <code>rallocx</code> function resizes the allocation at <i>ptr</i> to be at least <i>size</i> bytes, and returns a pointer to the base address of the resulting allocation, which may or may not have moved from its original location. Behavior is undefined if <i>size</i> is <code>0</code>, or if request size overflows due to size class and/or alignment constraints. </p>
<p> The <code>xallocx</code> function resizes the allocation at <i>ptr</i> in place to be at least <i>size</i> bytes, and returns the real size of the allocation. If <i>extra</i> is non-zero, an attempt is made to resize the allocation to be at least (<i>size</i> + <i>extra</i>) bytes, though inability to allocate the extra byte(s) will not by itself result in failure to resize. Behavior is undefined if <i>size</i> is <code>0</code>, or if (<i>size</i> + <i>extra</i> &gt; <code>SIZE_T_MAX</code>). </p>
<p> The <code>sallocx</code> function returns the real size of the allocation at <i>ptr</i>. </p>
<p> The <code>dallocx</code> function causes the memory referenced by <i>ptr</i> to be made available for future allocations. </p>
<p> The <code>nallocx</code> function allocates no memory, but it performs the same size computation as the <code>mallocx</code> function, and returns the real size of the allocation that would result from the equivalent <code>mallocx</code> function call. Behavior is undefined if <i>size</i> is <code>0</code>, or if request size overflows due to size class and/or alignment constraints. </p>
<p> The <code>mallctl</code> function provides a general interface for introspecting the memory allocator, as well as setting modifiable parameters and triggering actions. The period-separated <i>name</i> argument specifies a location in a tree-structured namespace; see the MALLCTL NAMESPACE section for documentation on the tree contents. To read a value, pass a pointer via <i>oldp</i> to adequate space to contain the value, and a pointer to its length via <i>oldlenp</i>; otherwise pass <code>NULL</code> and <code>NULL</code>. Similarly, to write a value, pass a pointer to the value via <i>newp</i>, and its length via <i>newlen</i>; otherwise pass <code>NULL</code> and <code>0</code>. </p>
<p> The <code>mallctlnametomib</code> function provides a way to avoid repeated name lookups for applications that repeatedly query the same portion of the namespace, by translating a name to a &#8220;Management Information Base&#8221; (MIB) that can be passed repeatedly to <code>mallctlbymib</code>. Upon successful return from <code>mallctlnametomib</code>, <i>mibp</i> contains an array of <i>*miblenp</i> integers, where <i>*miblenp</i> is the lesser of the number of components in <i>name</i> and the input value of <i>*miblenp</i>. Thus it is possible to pass a <i>*miblenp</i> that is smaller than the number of period-separated name components, which results in a partial MIB that can be used as the basis for constructing a complete MIB. For name components that are integers (e.g. the 2 in &quot;arenas.bin.2.size&quot;), the corresponding MIB component will always be that integer. Therefore, it is legitimate to construct code like the following: </p>
<dl>
<dt>
<dd>
<pre><code>
unsigned nbins, i;
size_t mib[4];
size_t len, miblen;
len = sizeof(nbins);
mallctl("arenas.nbins", &amp;nbins, &amp;len, NULL, 0);
miblen = 4;
mallctlnametomib("arenas.bin.0.size", mib, &amp;miblen);
for (i = 0; i &lt; nbins; i++) {
    size_t bin_size;
    mib[2] = i;
    len = sizeof(bin_size);
    mallctlbymib(mib, miblen, &amp;bin_size, &amp;len, NULL, 0);
    /* Do something with bin_size... */
}
</code></pre>
</dl>
<p> The <code>malloc_stats_print</code> function writes human-readable summary statistics via the <i>write_cb</i> callback function pointer and <i>cbopaque</i> data passed to <i>write_cb</i>, or <code>malloc_message</code> if <i>write_cb</i> is <code>NULL</code>. This function can be called repeatedly. General information that never changes during execution can be omitted by specifying &quot;g&quot; as a character within the <i>opts</i> string. Note that <code>malloc_message</code> uses the <code>mallctl*</code> functions internally, so inconsistent statistics can be reported if multiple threads use these functions simultaneously. If <code>&#8211;enable-stats</code> is specified during configuration, &#8220;m&#8221; and &#8220;a&#8221; can be specified to omit merged arena and per arena statistics, respectively; &#8220;b&#8221; and &#8220;l&#8221; can be specified to omit per size class statistics for bins and large objects, respectively. Unrecognized characters are silently ignored. Note that thread caching may prevent some statistics from being completely up to date, since extra locking would be required to merge counters that track thread cache operations. </p>
<p> The <code>malloc_usable_size</code> function returns the usable size of the allocation pointed to by <i>ptr</i>. The return value may be larger than the size that was requested during allocation. The <code>malloc_usable_size</code> function is not a mechanism for in-place <code>realloc</code>; rather it is provided solely as a tool for introspection purposes. Any discrepancy between the requested allocation size and the size reported by <code>malloc_usable_size</code> should not be depended on, since such behavior is entirely implementation-dependent.</p>
<h3>Experimental API</h3>
<p> The experimental API is subject to change or removal without regard for backward compatibility. If <code>&#8211;disable-experimental</code> is specified during configuration, the experimental API is omitted. </p>
<p> The <code>allocm</code>, <code>rallocm</code>, <code>sallocm</code>, <code>dallocm</code>, and <code>nallocm</code> functions all have a <i>flags</i> argument that can be used to specify options. The functions only check the options that are contextually relevant. Use bitwise or (|) operations to specify one or more of the following: </p>
<p> <code>ALLOCM_LG_ALIGN(</code><i>la</i><code>) </code></p>
<dl>
<dt>
<dd> Align the memory allocation to start at an address that is a multiple of (1 &lt;&lt; <i>la</i>). This macro does not validate that <i>la</i> is within the valid range.</dl>
<p> <code>ALLOCM_ALIGN(</code><i>a</i><code>) </code></p>
<dl>
<dt>
<dd> Align the memory allocation to start at an address that is a multiple of <i>a</i>, where <i>a</i> is a power of two. This macro does not validate that <i>a</i> is a power of 2.</dl>
<p> <code>ALLOCM_ZERO</code></p>
<dl>
<dt>
<dd> Initialize newly allocated memory to contain zero bytes. In the growing reallocation case, the real size prior to reallocation defines the boundary between untouched bytes and those that are initialized to contain zero bytes. If this macro is absent, newly allocated memory is uninitialized.</dl>
<p> <code>ALLOCM_NO_MOVE</code></p>
<dl>
<dt>
<dd> For reallocation, fail rather than moving the object. This constraint can apply to both growth and shrinkage.</dl>
<p> <code>ALLOCM_ARENA(</code><i>a</i><code>) </code></p>
<dl>
<dt>
<dd> Use the arena specified by the index <i>a</i> (and by necessity bypass the thread cache). This macro has no effect for huge regions, nor for regions that were allocated via an arena other than the one specified. This macro does not validate that <i>a</i> specifies an arena index in the valid range.</dl>
<p> The <code>allocm</code> function allocates at least <i>size</i> bytes of memory, sets <i>*ptr</i> to the base address of the allocation, and sets <i>*rsize</i> to the real size of the allocation if <i>rsize</i> is not <code>NULL</code>. Behavior is undefined if <i>size</i> is <code>0</code>, or if request size overflows due to size class and/or alignment constraints. </p>
<p> The <code>rallocm</code> function resizes the allocation at <i>*ptr</i> to be at least <i>size</i> bytes, sets <i>*ptr</i> to the base address of the allocation if it moved, and sets <i>*rsize</i> to the real size of the allocation if <i>rsize</i> is not <code>NULL</code>. If <i>extra</i> is non-zero, an attempt is made to resize the allocation to be at least (<i>size</i> + <i>extra</i>) bytes, though inability to allocate the extra byte(s) will not by itself result in failure. Behavior is undefined if <i>size</i> is <code>0</code>, if request size overflows due to size class and/or alignment constraints, or if (<i>size</i> + <i>extra</i> &gt; <code>SIZE_T_MAX</code>). </p>
<p> The <code>sallocm</code> function sets <i>*rsize</i> to the real size of the allocation. </p>
<p> The <code>dallocm</code> function causes the memory referenced by <i>ptr</i> to be made available for future allocations. </p>
<p> The <code>nallocm</code> function allocates no memory, but it performs the same size computation as the <code>allocm</code> function, and if <i>rsize</i> is not <code>NULL</code> it sets <i>*rsize</i> to the real size of the allocation that would result from the equivalent <code>allocm</code> function call. Behavior is undefined if <i>size</i> is <code>0</code>, or if request size overflows due to size class and/or alignment constraints.</p>
<h2>TUNING</h2>
<p> Once, when the first call is made to one of the memory allocation routines, the allocator initializes its internals based in part on various options that can be specified at compile- or run-time. </p>
<p> The string pointed to by the global variable <i>malloc_conf</i>, the &#8220;name&#8221; of the file referenced by the symbolic link named /etc/malloc.conf, and the value of the environment variable <code>MALLOC_CONF</code>, will be interpreted, in that order, from left to right as options. Note that <i>malloc_conf</i> may be read before <code>main</code> is entered, so the declaration of <i>malloc_conf</i> should specify an initializer that contains the final value to be read by jemalloc. <i>malloc_conf</i> is a compile-time setting, whereas /etc/malloc.conf and <code>MALLOC_CONF</code> can be safely set any time prior to program invocation. </p>
<p> An options string is a comma-separated list of option:value pairs. There is one key corresponding to each &quot;opt.*&quot; mallctl (see the MALLCTL NAMESPACE section for options documentation). For example, abort:true,narenas:1 sets the &quot;opt.abort&quot; and &quot;opt.narenas&quot; options. Some options have boolean values (true/false), others have integer values (base 8, 10, or 16, depending on prefix), and yet others have raw string values.</p>
<h2>IMPLEMENTATION NOTES</h2>
<p> Traditionally, allocators have used <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) to obtain memory, which is suboptimal for several reasons, including race conditions, increased fragmentation, and artificial limitations on maximum usable memory. If <code>&#8211;enable-dss</code> is specified during configuration, this allocator uses both <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) and <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), in that order of preference; otherwise only <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) is used. </p>
<p> This allocator uses multiple arenas in order to reduce lock contention for threaded programs on multi-processor systems. This works well with regard to threading scalability, but incurs some costs. There is a small fixed per-arena overhead, and additionally, arenas manage memory completely independently of each other, which means a small fixed increase in overall memory fragmentation. These overheads are not generally an issue, given the number of arenas normally used. Note that using substantially more arenas than the default is not likely to improve performance, mainly due to reduced cache performance. However, it may make sense to reduce the number of arenas if an application does not make much use of the allocation functions. </p>
<p> In addition to multiple arenas, unless <code>&#8211;disable-tcache</code> is specified during configuration, this allocator supports thread-specific caching for small and large objects, in order to make it possible to completely avoid synchronization for most allocation requests. Such caching allows very fast allocation in the common case, but it increases memory usage and fragmentation, since a bounded number of objects can remain allocated in each thread cache. </p>
<p> Memory is conceptually broken into equal-sized chunks, where the chunk size is a power of two that is greater than the page size. Chunks are always aligned to multiples of the chunk size. This alignment makes it possible to find metadata for user objects very quickly. </p>
<p> User objects are broken into three categories according to size: small, large, and huge. Small objects are smaller than one page. Large objects are smaller than the chunk size. Huge objects are a multiple of the chunk size. Small and large objects are managed by arenas; huge objects are managed separately in a single data structure that is shared by all threads. Huge objects are used by applications infrequently enough that this single data structure is not a scalability issue. </p>
<p> Each chunk that is managed by an arena tracks its contents as runs of contiguous pages (unused, backing a set of small objects, or backing one large object). The combination of chunk alignment and chunk page maps makes it possible to determine all metadata regarding small and large allocations in constant time. </p>
<p> Small objects are managed in groups by page runs. Each run maintains a frontier and free list to track which regions are in use. Allocation requests that are no more than half the quantum (8 or 16, depending on architecture) are rounded up to the nearest power of two that is at least sizeof(<code>double</code>). All other small object size classes are multiples of the quantum, spaced such that internal fragmentation is limited to approximately 25% for all but the smallest size classes. Allocation requests that are larger than the maximum small size class, but small enough to fit in an arena-managed chunk (see the &quot;opt.lg_chunk&quot; option), are rounded up to the nearest run size. Allocation requests that are too large to fit in an arena-managed chunk are rounded up to the nearest multiple of the chunk size. </p>
<p> Allocations are packed tightly together, which can be an issue for multi-threaded applications. If you need to assure that allocations do not suffer from cacheline sharing, round your allocation requests up to the nearest multiple of the cacheline size, or specify cacheline alignment when allocating. </p>
<p> Assuming 4 MiB chunks, 4 KiB pages, and a 16-byte quantum on a 64-bit system, the size classes in each category are as shown in Table 1. </p>
<p> <code>Table 1. Size classes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Category </code></td>
<td ALIGN=right><code> Spacing </code></td>
<td><code> Size </code>
</td>
</tr>
<tr VALIGN=top>
<td VALIGN=center ROWSPAN=2> Small </td>
<td ALIGN=right> lg </td>
<td> [8]
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 16 </td>
<td> [16, 32, 48, &#8230;, 128] </td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 32 </td>
<td> [160, 192, 224, 256] </td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 64 </td>
<td> [320, 384, 448, 512] </td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 128 </td>
<td> [640, 768, 896, 1024] </td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 256 </td>
<td> [1280, 1536, 1792, 2048] </td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 512 </td>
<td> [2560, 3072, 3584] </td>
</tr>
<tr VALIGN=top>
<td> Large </td>
<td ALIGN=right> 4 KiB </td>
<td> [4 KiB, 8 KiB, 12 KiB, &#8230;, 4072 KiB]
</td>
</tr>
<tr VALIGN=top>
<td> Huge </td>
<td ALIGN=right> 4 MiB </td>
<td> [4 MiB, 8 MiB, 12 MiB, &#8230;]
</td>
</tr>
</table>
<h2>MALLCTL NAMESPACE</h2>
<p> The following names are defined in the namespace accessible via the <code>mallctl*</code> functions. Value types are specified in parentheses, their readable/writable statuses are encoded as rw, r-, -w, or &#8211;, and required build configuration flags follow, if any. A name element encoded as &lt;i&gt; or &lt;j&gt; indicates an integer component, where the integer varies from 0 to some upper value that must be determined via introspection. In the case of &quot;stats.arenas.&lt;i&gt;.*&quot;, &lt;i&gt; equal to &quot;arenas.narenas&quot; can be used to access the summation of statistics from all arenas. Take special note of the &quot;epoch&quot; mallctl, which controls refreshing of cached dynamic statistics. </p>
<p> &quot;version&quot; (<code>const char *</code>) r-</p>
<dl>
<dt>
<dd> Return the jemalloc version string.</dl>
<p> &quot;epoch&quot; (<code>uint64_t</code>) rw</p>
<dl>
<dt>
<dd> If a value is passed in, refresh the data from which the <code>mallctl*</code> functions report values, and increment the epoch. Return the current epoch. This is useful for detecting whether another thread caused a refresh.</dl>
<p> &quot;config.debug&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-debug</code> was specified during build configuration.</dl>
<p> &quot;config.dss&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-dss</code> was specified during build configuration.</dl>
<p> &quot;config.fill&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-fill</code> was specified during build configuration.</dl>
<p> &quot;config.lazy_lock&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-lazy-lock</code> was specified during build configuration.</dl>
<p> &quot;config.mremap&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-mremap</code> was specified during build configuration.</dl>
<p> &quot;config.munmap&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-munmap</code> was specified during build configuration.</dl>
<p> &quot;config.prof&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-prof</code> was specified during build configuration.</dl>
<p> &quot;config.prof_libgcc&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;disable-prof-libgcc</code> was not specified during build configuration.</dl>
<p> &quot;config.prof_libunwind&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-prof-libunwind</code> was specified during build configuration.</dl>
<p> &quot;config.stats&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-stats</code> was specified during build configuration.</dl>
<p> &quot;config.tcache&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;disable-tcache</code> was not specified during build configuration.</dl>
<p> &quot;config.tls&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;disable-tls</code> was not specified during build configuration.</dl>
<p> &quot;config.utrace&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-utrace</code> was specified during build configuration.</dl>
<p> &quot;config.valgrind&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-valgrind</code> was specified during build configuration.</dl>
<p> &quot;config.xmalloc&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> <code>&#8211;enable-xmalloc</code> was specified during build configuration.</dl>
<p> &quot;opt.abort&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> Abort-on-warning enabled/disabled. If true, most warnings are fatal. The process will call <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3) in these cases. This option is disabled by default unless <code>&#8211;enable-debug</code> is specified during configuration, in which case it is enabled by default.</dl>
<p> &quot;opt.dss&quot; (<code>const char *</code>) r-</p>
<dl>
<dt>
<dd> dss (<code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)) allocation precedence as related to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) allocation. The following settings are supported: &#8220;disabled&#8221;, &#8220;primary&#8221;, and &#8220;secondary&#8221;. The default is &#8220;secondary&#8221; if &quot;config.dss&quot; is true, &#8220;disabled&#8221; otherwise.</dl>
<p> &quot;opt.lg_chunk&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Virtual memory chunk size (log base 2). If a chunk size outside the supported size range is specified, the size is silently clipped to the minimum/maximum supported size. The default chunk size is 4 MiB (2^22).</dl>
<p> &quot;opt.narenas&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Maximum number of arenas to use for automatic multiplexing of threads and arenas. The default is four times the number of CPUs, or one if there is a single CPU.</dl>
<p> &quot;opt.lg_dirty_mult&quot; (<code>ssize_t</code>) r-</p>
<dl>
<dt>
<dd> Per-arena minimum ratio (log base 2) of active to dirty pages. Some dirty unused pages may be allowed to accumulate, within the limit set by the ratio (or one chunk worth of dirty pages, whichever is greater), before informing the kernel about some of those pages via <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) or a similar system call. This provides the kernel with sufficient information to recycle dirty pages if physical memory becomes scarce and the pages remain unused. The default minimum ratio is 8:1 (2^3:1); an option value of -1 will disable dirty page purging.</dl>
<p> &quot;opt.stats_print&quot; (<code>bool</code>) r-</p>
<dl>
<dt>
<dd> Enable/disable statistics printing at exit. If enabled, the <code>malloc_stats_print</code> function is called at program exit via an <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) function. If <code>&#8211;enable-stats</code> is specified during configuration, this has the potential to cause deadlock for a multi-threaded process that exits while one or more threads are executing in the memory allocation functions. Therefore, this option should only be used with care; it is primarily intended as a performance tuning aid during application development. This option is disabled by default.</dl>
<p> &quot;opt.junk&quot; (<code>bool</code>) r- [<code>&#8211;enable-fill</code>]</p>
<dl>
<dt>
<dd> Junk filling enabled/disabled. If enabled, each byte of uninitialized allocated memory will be initialized to 0xa5. All deallocated memory will be initialized to 0x5a. This is intended for debugging and will impact performance negatively. This option is disabled by default unless <code>&#8211;enable-debug</code> is specified during configuration, in which case it is enabled by default unless running inside m[blue]<code>Valgrind</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> &quot;opt.quarantine&quot; (<code>size_t</code>) r- [<code>&#8211;enable-fill</code>]</p>
<dl>
<dt>
<dd> Per thread quarantine size in bytes. If non-zero, each thread maintains a FIFO object quarantine that stores up to the specified number of bytes of memory. The quarantined memory is not freed until it is released from quarantine, though it is immediately junk-filled if the &quot;opt.junk&quot; option is enabled. This feature is of particular use in combination with m[blue]<code>Valgrind</code>m[]<font SIZE="-2">[2]</font>, which can detect attempts to access quarantined objects. This is intended for debugging and will impact performance negatively. The default quarantine size is 0 unless running inside Valgrind, in which case the default is 16 MiB.</dl>
<p> &quot;opt.redzone&quot; (<code>bool</code>) r- [<code>&#8211;enable-fill</code>]</p>
<dl>
<dt>
<dd> Redzones enabled/disabled. If enabled, small allocations have redzones before and after them. Furthermore, if the &quot;opt.junk&quot; option is enabled, the redzones are checked for corruption during deallocation. However, the primary intended purpose of this feature is to be used in combination with m[blue]<code>Valgrind</code>m[]<font SIZE="-2">[2]</font>, which needs redzones in order to do effective buffer overflow/underflow detection. This option is intended for debugging and will impact performance negatively. This option is disabled by default unless running inside Valgrind.</dl>
<p> &quot;opt.zero&quot; (<code>bool</code>) r- [<code>&#8211;enable-fill</code>]</p>
<dl>
<dt>
<dd> Zero filling enabled/disabled. If enabled, each byte of uninitialized allocated memory will be initialized to 0. Note that this initialization only happens once for each byte, so <code>realloc</code>, <code>rallocx</code> and <code>rallocm</code> calls do not zero memory that was previously allocated. This is intended for debugging and will impact performance negatively. This option is disabled by default.</dl>
<p> &quot;opt.utrace&quot; (<code>bool</code>) r- [<code>&#8211;enable-utrace</code>]</p>
<dl>
<dt>
<dd> Allocation tracing based on <code><a href="/docs/linux/man/2-utrace/">utrace</a></code>(2) enabled/disabled. This option is disabled by default.</dl>
<p> &quot;opt.valgrind&quot; (<code>bool</code>) r- [<code>&#8211;enable-valgrind</code>]</p>
<dl>
<dt>
<dd> m[blue]<code>Valgrind</code>m[]<font SIZE="-2">[2]</font> support enabled/disabled. This option is vestigal because jemalloc auto-detects whether it is running inside Valgrind. This option is disabled by default, unless running inside Valgrind.</dl>
<p> &quot;opt.xmalloc&quot; (<code>bool</code>) r- [<code>&#8211;enable-xmalloc</code>]</p>
<dl>
<dt>
<dd> Abort-on-out-of-memory enabled/disabled. If enabled, rather than returning failure for any allocation function, display a diagnostic message on <code>STDERR_FILENO</code> and cause the program to drop core (using <code><a href="/docs/linux/man/3-abort/">abort</a></code>(3)). If an application is designed to depend on this behavior, set the option at compile time by including the following in the source code: </p>
<dl>
<dt>
<dd>
<pre>
malloc_conf = &quot;xmalloc:true&quot;;
</pre>
</dl>
<p> This option is disabled by default.</dl>
<p> &quot;opt.tcache&quot; (<code>bool</code>) r- [<code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Thread-specific caching enabled/disabled. When there are multiple threads, each thread uses a thread-specific cache for objects up to a certain size. Thread-specific caching allows many allocations to be satisfied without performing any thread synchronization, at the cost of increased memory use. See the &quot;opt.lg_tcache_max&quot; option for related tuning information. This option is enabled by default unless running inside m[blue]<code>Valgrind</code>m[]<font SIZE="-2">[2]</font>.</dl>
<p> &quot;opt.lg_tcache_max&quot; (<code>size_t</code>) r- [<code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Maximum size class (log base 2) to cache in the thread-specific cache. At a minimum, all small size classes are cached, and at a maximum all large size classes are cached. The default maximum is 32 KiB (2^15).</dl>
<p> &quot;opt.prof&quot; (<code>bool</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Memory profiling enabled/disabled. If enabled, profile memory allocation activity. See the &quot;opt.prof_active&quot; option for on-the-fly activation/deactivation. See the &quot;opt.lg_prof_sample&quot; option for probabilistic sampling control. See the &quot;opt.prof_accum&quot; option for control of cumulative sample reporting. See the &quot;opt.lg_prof_interval&quot; option for information on interval-triggered profile dumping, the &quot;opt.prof_gdump&quot; option for information on high-water-triggered profile dumping, and the &quot;opt.prof_final&quot; option for final profile dumping. Profile output is compatible with the included <code>pprof</code> Perl script, which originates from the m[blue]<code>gperftools package</code>m[]<font SIZE="-2">[3]</font>.</dl>
<p> &quot;opt.prof_prefix&quot; (<code>const char *</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Filename prefix for profile dumps. If the prefix is set to the empty string, no automatic dumps will occur; this is primarily useful for disabling the automatic final heap dump (which also disables leak reporting, if enabled). The default prefix is jeprof.</dl>
<p> &quot;opt.prof_active&quot; (<code>bool</code>) rw [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Profiling activated/deactivated. This is a secondary control mechanism that makes it possible to start the application with profiling enabled (see the &quot;opt.prof&quot; option) but inactive, then toggle profiling at any time during program execution with the &quot;prof.active&quot; mallctl. This option is enabled by default.</dl>
<p> &quot;opt.lg_prof_sample&quot; (<code>ssize_t</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Average interval (log base 2) between allocation samples, as measured in bytes of allocation activity. Increasing the sampling interval decreases profile fidelity, but also decreases the computational overhead. The default sample interval is 512 KiB (2^19 B).</dl>
<p> &quot;opt.prof_accum&quot; (<code>bool</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Reporting of cumulative object/byte counts in profile dumps enabled/disabled. If this option is enabled, every unique backtrace must be stored for the duration of execution. Depending on the application, this can impose a large memory overhead, and the cumulative counts are not always of interest. This option is disabled by default.</dl>
<p> &quot;opt.lg_prof_interval&quot; (<code>ssize_t</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Average interval (log base 2) between memory profile dumps, as measured in bytes of allocation activity. The actual interval between dumps may be sporadic because decentralized allocation counters are used to avoid synchronization bottlenecks. Profiles are dumped to files named according to the pattern &lt;prefix&gt;.&lt;pid&gt;.&lt;seq&gt;.i&lt;iseq&gt;.heap, where &lt;prefix&gt; is controlled by the &quot;opt.prof_prefix&quot; option. By default, interval-triggered profile dumping is disabled (encoded as -1).</dl>
<p> &quot;opt.prof_gdump&quot; (<code>bool</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Trigger a memory profile dump every time the total virtual memory exceeds the previous maximum. Profiles are dumped to files named according to the pattern &lt;prefix&gt;.&lt;pid&gt;.&lt;seq&gt;.u&lt;useq&gt;.heap, where &lt;prefix&gt; is controlled by the &quot;opt.prof_prefix&quot; option. This option is disabled by default.</dl>
<p> &quot;opt.prof_final&quot; (<code>bool</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Use an <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) function to dump final memory usage to a file named according to the pattern &lt;prefix&gt;.&lt;pid&gt;.&lt;seq&gt;.f.heap, where &lt;prefix&gt; is controlled by the &quot;opt.prof_prefix&quot; option. This option is enabled by default.</dl>
<p> &quot;opt.prof_leak&quot; (<code>bool</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Leak reporting enabled/disabled. If enabled, use an <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) function to report memory leaks detected by allocation sampling. See the &quot;opt.prof&quot; option for information on analyzing heap profile output. This option is disabled by default.</dl>
<p> &quot;thread.arena&quot; (<code>unsigned</code>) rw</p>
<dl>
<dt>
<dd> Get or set the arena associated with the calling thread. If the specified arena was not initialized beforehand (see the &quot;arenas.initialized&quot; mallctl), it will be automatically initialized as a side effect of calling this interface.</dl>
<p> &quot;thread.allocated&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Get the total number of bytes ever allocated by the calling thread. This counter has the potential to wrap around; it is up to the application to appropriately interpret the counter in such cases.</dl>
<p> &quot;thread.allocatedp&quot; (<code>uint64_t *</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Get a pointer to the the value that is returned by the &quot;thread.allocated&quot; mallctl. This is useful for avoiding the overhead of repeated <code>mallctl*</code> calls.</dl>
<p> &quot;thread.deallocated&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Get the total number of bytes ever deallocated by the calling thread. This counter has the potential to wrap around; it is up to the application to appropriately interpret the counter in such cases.</dl>
<p> &quot;thread.deallocatedp&quot; (<code>uint64_t *</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Get a pointer to the the value that is returned by the &quot;thread.deallocated&quot; mallctl. This is useful for avoiding the overhead of repeated <code>mallctl*</code> calls.</dl>
<p> &quot;thread.tcache.enabled&quot; (<code>bool</code>) rw [<code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Enable/disable calling thread&#8217;s tcache. The tcache is implicitly flushed as a side effect of becoming disabled (see &quot;thread.tcache.flush&quot;).</dl>
<p> &quot;thread.tcache.flush&quot; (<code>void</code>) &#8212; [<code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Flush calling thread&#8217;s tcache. This interface releases all cached objects and internal data structures associated with the calling thread&#8217;s thread-specific cache. Ordinarily, this interface need not be called, since automatic periodic incremental garbage collection occurs, and the thread cache is automatically discarded when a thread exits. However, garbage collection is triggered by allocation activity, so it is possible for a thread that stops allocating/deallocating to retain its cache indefinitely, in which case the developer may find manual flushing useful.</dl>
<p> &quot;arena.&lt;i&gt;.purge&quot; (<code>unsigned</code>) &#8212;</p>
<dl>
<dt>
<dd> Purge unused dirty pages for arena &lt;i&gt;, or for all arenas if &lt;i&gt; equals &quot;arenas.narenas&quot;.</dl>
<p> &quot;arena.&lt;i&gt;.dss&quot; (<code>const char *</code>) rw</p>
<dl>
<dt>
<dd> Set the precedence of dss allocation as related to mmap allocation for arena &lt;i&gt;, or for all arenas if &lt;i&gt; equals &quot;arenas.narenas&quot;. Note that even during huge allocation this setting is read from the arena that would be chosen for small or large allocation so that applications can depend on consistent dss versus mmap allocation regardless of allocation size. See &quot;opt.dss&quot; for supported settings.</dl>
<p> &quot;arenas.narenas&quot; (<code>unsigned</code>) r-</p>
<dl>
<dt>
<dd> Current limit on number of arenas.</dl>
<p> &quot;arenas.initialized&quot; (<code>bool *</code>) r-</p>
<dl>
<dt>
<dd> An array of &quot;arenas.narenas&quot; booleans. Each boolean indicates whether the corresponding arena is initialized.</dl>
<p> &quot;arenas.quantum&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Quantum size.</dl>
<p> &quot;arenas.page&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Page size.</dl>
<p> &quot;arenas.tcache_max&quot; (<code>size_t</code>) r- [<code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Maximum thread-cached size class.</dl>
<p> &quot;arenas.nbins&quot; (<code>unsigned</code>) r-</p>
<dl>
<dt>
<dd> Number of bin size classes.</dl>
<p> &quot;arenas.nhbins&quot; (<code>unsigned</code>) r- [<code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Total number of thread cache bin size classes.</dl>
<p> &quot;arenas.bin.&lt;i&gt;.size&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Maximum size supported by size class.</dl>
<p> &quot;arenas.bin.&lt;i&gt;.nregs&quot; (<code>uint32_t</code>) r-</p>
<dl>
<dt>
<dd> Number of regions per page run.</dl>
<p> &quot;arenas.bin.&lt;i&gt;.run_size&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Number of bytes per page run.</dl>
<p> &quot;arenas.nlruns&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Total number of large size classes.</dl>
<p> &quot;arenas.lrun.&lt;i&gt;.size&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Maximum size supported by this large size class.</dl>
<p> &quot;arenas.purge&quot; (<code>unsigned</code>) -w</p>
<dl>
<dt>
<dd> Purge unused dirty pages for the specified arena, or for all arenas if none is specified.</dl>
<p> &quot;arenas.extend&quot; (<code>unsigned</code>) r-</p>
<dl>
<dt>
<dd> Extend the array of arenas by appending a new arena, and returning the new arena index.</dl>
<p> &quot;prof.active&quot; (<code>bool</code>) rw [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Control whether sampling is currently active. See the &quot;opt.prof_active&quot; option for additional information.</dl>
<p> &quot;prof.dump&quot; (<code>const char *</code>) -w [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Dump a memory profile to the specified file, or if NULL is specified, to a file according to the pattern &lt;prefix&gt;.&lt;pid&gt;.&lt;seq&gt;.m&lt;mseq&gt;.heap, where &lt;prefix&gt; is controlled by the &quot;opt.prof_prefix&quot; option.</dl>
<p> &quot;prof.interval&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-prof</code>]</p>
<dl>
<dt>
<dd> Average number of bytes allocated between inverval-based profile dumps. See the &quot;opt.lg_prof_interval&quot; option for additional information.</dl>
<p> &quot;stats.cactive&quot; (<code>size_t *</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Pointer to a counter that contains an approximate count of the current number of bytes in active pages. The estimate may be high, but never low, because each arena rounds up to the nearest multiple of the chunk size when computing its contribution to the counter. Note that the &quot;epoch&quot; mallctl has no bearing on this counter. Furthermore, counter consistency is maintained via atomic operations, so it is necessary to use an atomic operation in order to guarantee a consistent read when dereferencing the pointer.</dl>
<p> &quot;stats.allocated&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Total number of bytes allocated by the application.</dl>
<p> &quot;stats.active&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Total number of bytes in active pages allocated by the application. This is a multiple of the page size, and greater than or equal to &quot;stats.allocated&quot;. This does not include &quot;stats.arenas.&lt;i&gt;.pdirty&quot; and pages entirely devoted to allocator metadata.</dl>
<p> &quot;stats.mapped&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Total number of bytes in chunks mapped on behalf of the application. This is a multiple of the chunk size, and is at least as large as &quot;stats.active&quot;. This does not include inactive chunks.</dl>
<p> &quot;stats.chunks.current&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Total number of chunks actively mapped on behalf of the application. This does not include inactive chunks.</dl>
<p> &quot;stats.chunks.total&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of chunks allocated.</dl>
<p> &quot;stats.chunks.high&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Maximum number of active chunks at any time thus far.</dl>
<p> &quot;stats.huge.allocated&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of bytes currently allocated by huge objects.</dl>
<p> &quot;stats.huge.nmalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of huge allocation requests.</dl>
<p> &quot;stats.huge.ndalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of huge deallocation requests.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.dss&quot; (<code>const char *</code>) r-</p>
<dl>
<dt>
<dd> dss (<code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)) allocation precedence as related to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) allocation. See &quot;opt.dss&quot; for details.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.nthreads&quot; (<code>unsigned</code>) r-</p>
<dl>
<dt>
<dd> Number of threads currently assigned to arena.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.pactive&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Number of pages in active runs.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.pdirty&quot; (<code>size_t</code>) r-</p>
<dl>
<dt>
<dd> Number of pages within unused runs that are potentially dirty, and for which <code>madvise</code><i>&#8230;</i><i></i><code>MADV_DONTNEED</code> or similar has not been called.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.mapped&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of mapped bytes.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.npurge&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of dirty page purge sweeps performed.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.nmadvise&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of <code>madvise</code><i>&#8230;</i><i></i><code>MADV_DONTNEED</code> or similar calls made to purge dirty pages.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.purged&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of pages purged.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.small.allocated&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of bytes currently allocated by small objects.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.small.nmalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of allocation requests served by small bins.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.small.ndalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of small objects returned to bins.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.small.nrequests&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of small allocation requests.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.large.allocated&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Number of bytes currently allocated by large objects.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.large.nmalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of large allocation requests served directly by the arena.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.large.ndalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of large deallocation requests served directly by the arena.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.large.nrequests&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of large allocation requests.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.allocated&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Current number of bytes allocated by bin.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.nmalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of allocations served by bin.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.ndalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of allocations returned to bin.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.nrequests&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of allocation requests.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.nfills&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code> <code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Cumulative number of tcache fills.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.nflushes&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code> <code>&#8211;enable-tcache</code>]</p>
<dl>
<dt>
<dd> Cumulative number of tcache flushes.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.nruns&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of runs created.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.nreruns&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of times the current run from which to allocate changed.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.bins.&lt;j&gt;.curruns&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Current number of runs.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.lruns.&lt;j&gt;.nmalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of allocation requests for this size class served directly by the arena.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.lruns.&lt;j&gt;.ndalloc&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of deallocation requests for this size class served directly by the arena.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.lruns.&lt;j&gt;.nrequests&quot; (<code>uint64_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Cumulative number of allocation requests for this size class.</dl>
<p> &quot;stats.arenas.&lt;i&gt;.lruns.&lt;j&gt;.curruns&quot; (<code>size_t</code>) r- [<code>&#8211;enable-stats</code>]</p>
<dl>
<dt>
<dd> Current number of runs for this size class.</dl>
<h2>DEBUGGING MALLOC PROBLEMS</h2>
<p> When debugging, it is a good idea to configure/build jemalloc with the <code>&#8211;enable-debug</code> and <code>&#8211;enable-fill</code> options, and recompile the program with suitable options and symbols for debugger support. When so configured, jemalloc incorporates a wide variety of run-time assertions that catch application errors such as double-free, write-after-free, etc. </p>
<p> Programs often accidentally depend on &#8220;uninitialized&#8221; memory actually being filled with zero bytes. Junk filling (see the &quot;opt.junk&quot; option) tends to expose such bugs in the form of obviously incorrect results and/or coredumps. Conversely, zero filling (see the &quot;opt.zero&quot; option) eliminates the symptoms of such bugs. Between these two options, it is usually possible to quickly detect, diagnose, and eliminate such bugs. </p>
<p> This implementation does not provide much detail about the problems it detects, because the performance impact for storing such information would be prohibitive. However, jemalloc does integrate with the most excellent m[blue]<code>Valgrind</code>m[]<font SIZE="-2">[2]</font> tool if the <code>&#8211;enable-valgrind</code> configuration option is enabled.</p>
<h2>DIAGNOSTIC MESSAGES</h2>
<p> If any of the memory allocation/deallocation functions detect an error or warning condition, a message will be printed to file descriptor <code>STDERR_FILENO</code>. Errors will result in the process dumping core. If the &quot;opt.abort&quot; option is set, most warnings are treated as errors. </p>
<p> The <i>malloc_message</i> variable allows the programmer to override the function which emits the text strings forming the errors and warnings if for some reason the <code>STDERR_FILENO</code> file descriptor is not suitable for this. <code>malloc_message</code> takes the <i>cbopaque</i> pointer argument that is <code>NULL</code> unless overridden by the arguments in a call to <code>malloc_stats_print</code>, followed by a string pointer. Please note that doing anything which tries to allocate memory in this function is likely to result in a crash or deadlock. </p>
<p> All messages are prefixed by &#8220;&lt;jemalloc&gt;:&#8221;.</p>
<h2>RETURN VALUES</h2>
<h3>Standard API</h3>
<p> The <code>malloc</code> and <code>calloc</code> functions return a pointer to the allocated memory if successful; otherwise a <code>NULL</code> pointer is returned and <i>errno</i> is set to ENOMEM. </p>
<p> The <code>posix_memalign</code> function returns the value 0 if successful; otherwise it returns an error value. The <code>posix_memalign</code> function will fail if: </p>
<p> EINVAL</p>
<dl>
<dt>
<dd> The <i>alignment</i> parameter is not a power of 2 at least as large as sizeof(<code>void *</code>).</dl>
<p> ENOMEM</p>
<dl>
<dt>
<dd> Memory allocation error.</dl>
<p> The <code>aligned_alloc</code> function returns a pointer to the allocated memory if successful; otherwise a <code>NULL</code> pointer is returned and <i>errno</i> is set. The <code>aligned_alloc</code> function will fail if: </p>
<p> EINVAL</p>
<dl>
<dt>
<dd> The <i>alignment</i> parameter is not a power of 2.</dl>
<p> ENOMEM</p>
<dl>
<dt>
<dd> Memory allocation error.</dl>
<p> The <code>realloc</code> function returns a pointer, possibly identical to <i>ptr</i>, to the allocated memory if successful; otherwise a <code>NULL</code> pointer is returned, and <i>errno</i> is set to ENOMEM if the error was the result of an allocation failure. The <code>realloc</code> function always leaves the original buffer intact when an error occurs. </p>
<p> The <code>free</code> function returns no value.</p>
<h3>Non-standard API</h3>
<p> The <code>mallocx</code> and <code>rallocx</code> functions return a pointer to the allocated memory if successful; otherwise a <code>NULL</code> pointer is returned to indicate insufficient contiguous memory was available to service the allocation request. </p>
<p> The <code>xallocx</code> function returns the real size of the resulting resized allocation pointed to by <i>ptr</i>, which is a value less than <i>size</i> if the allocation could not be adequately grown in place. </p>
<p> The <code>sallocx</code> function returns the real size of the allocation pointed to by <i>ptr</i>. </p>
<p> The <code>nallocx</code> returns the real size that would result from a successful equivalent <code>mallocx</code> function call, or zero if insufficient memory is available to perform the size computation. </p>
<p> The <code>mallctl</code>, <code>mallctlnametomib</code>, and <code>mallctlbymib</code> functions return 0 on success; otherwise they return an error value. The functions will fail if: </p>
<p> EINVAL</p>
<dl>
<dt>
<dd> <i>newp</i> is not <code>NULL</code>, and <i>newlen</i> is too large or too small. Alternatively, <i>*oldlenp</i> is too large or too small; in this case as much data as possible are read despite the error.</dl>
<p> ENOENT</p>
<dl>
<dt>
<dd> <i>name</i> or <i>mib</i> specifies an unknown/invalid value.</dl>
<p> EPERM</p>
<dl>
<dt>
<dd> Attempt to read or write void value, or attempt to write read-only value.</dl>
<p> EAGAIN</p>
<dl>
<dt>
<dd> A memory allocation failure occurred.</dl>
<p> EFAULT</p>
<dl>
<dt>
<dd> An interface with side effects failed in some way not directly related to <code>mallctl*</code> read/write processing.</dl>
<p> The <code>malloc_usable_size</code> function returns the usable size of the allocation pointed to by <i>ptr</i>.</p>
<h3>Experimental API</h3>
<p> The <code>allocm</code>, <code>rallocm</code>, <code>sallocm</code>, <code>dallocm</code>, and <code>nallocm</code> functions return <code>ALLOCM_SUCCESS</code> on success; otherwise they return an error value. The <code>allocm</code>, <code>rallocm</code>, and <code>nallocm</code> functions will fail if: </p>
<p> ALLOCM_ERR_OOM</p>
<dl>
<dt>
<dd> Out of memory. Insufficient contiguous memory was available to service the allocation request. The <code>allocm</code> function additionally sets <i>*ptr</i> to <code>NULL</code>, whereas the <code>rallocm</code> function leaves <code>*ptr</code> unmodified.</dl>
<p> The <code>rallocm</code> function will also fail if: </p>
<p> ALLOCM_ERR_NOT_MOVED</p>
<dl>
<dt>
<dd> <code>ALLOCM_NO_MOVE</code> was specified, but the reallocation request could not be serviced without moving the object.</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variable affects the execution of the allocation functions: </p>
<p> <code>MALLOC_CONF</code></p>
<dl>
<dt>
<dd> If the environment variable <code>MALLOC_CONF</code> is set, the characters it contains will be interpreted as options.</dl>
<h2>EXAMPLES</h2>
<p> To dump core whenever a problem occurs: </p>
<dl>
<dt>
<dd>
<pre>
ln -s 'abort:true' /etc/malloc.conf
</pre>
</dl>
<p> To specify in the source a chunk size that is 16 MiB: </p>
<dl>
<dt>
<dd>
<pre>
malloc_conf = &quot;lg_chunk:24&quot;;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/2-utrace/">utrace</a></code>(2), <code><a href="/docs/linux/man/3-alloca/">alloca</a></code>(3), <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3), <code><a href="/docs/linux/man/3-getpagesize/">getpagesize</a></code>(3)</p>
<h2>STANDARDS</h2>
<p> The <code>malloc</code>, <code>calloc</code>, <code>realloc</code>, and <code>free</code> functions conform to ISO/IEC 9899:1990 (&#8220;ISO C90&#8221;). </p>
<p> The <code>posix_memalign</code> function conforms to IEEE Std 1003.1-2001 (&#8220;POSIX.1&#8221;).</p>
<h2>AUTHOR</h2>
<p> <code>Jason Evans</code></p>
<dl>
<dt>
<dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> jemalloc website</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.canonware.com/jemalloc/">http://www.canonware.com/jemalloc/</a></dl>
<dt> 2.</p>
<dd> Valgrind</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://valgrind.org/">http://valgrind.org/</a></dl>
<dt> 3.</p>
<dd> gperftools package</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://code.google.com/p/gperftools/">http://code.google.com/p/gperftools/</a></dl>
</dl>
<h2>Index</h2>
