---
title: "mmap64(3)"
name: "mmap64"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mmap64/"
description: "mmap, munmap – map or unmap files or devices into memory"
---

<p>mmap, munmap &#8211; map or unmap files or devices into memory </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/mman.h&gt;</code>
<code>void *mmap(void *</code><i>addr</i><code>, size_t </code><i>length</i><code>, int </code><i>prot</i><code>, int </code><i>flags</i><code>,</code>
<code> int </code><i>fd</i><code>, off_t </code><i>offset</i><code>);</code>
<code>int munmap(void *</code><i>addr</i><code>, size_t </code><i>length</i><code>);</code></pre>
<p>See NOTES for information on feature test macro requirements.</p>
<h2>Description</h2>
<p><code>mmap</code>() creates a new mapping in the virtual address space of the calling process. The starting address for the new mapping is specified in <i>addr</i>. The <i>length</i> argument specifies the length of the mapping (which must be greater than 0). </p>
<p> If <i>addr</i> is NULL, then the kernel chooses the (page-aligned) address at which to create the mapping; this is the most portable method of creating a new mapping. If <i>addr</i> is not NULL, then the kernel takes it as a hint about where to place the mapping; on Linux, the kernel will pick a nearby page boundary (but always above or equal to the value specified by <i>/proc/sys/vm/mmap_min_addr</i>) and attempt to create the mapping there. If another mapping already exists there, the kernel picks a new address that may or may not depend on the hint. The address of the new mapping is returned as the result of the call. </p>
<p> The contents of a file mapping (as opposed to an anonymous mapping; see <code>MAP_ANONYMOUS</code> below), are initialized using <i>length</i> bytes starting at offset <i>offset</i> in the file (or other object) referred to by the file descriptor <i>fd</i>. <i>offset</i> must be a multiple of the page size as returned by <i>sysconf(_SC_PAGE_SIZE)</i>. </p>
<p> After the <code>mmap</code>() call has returned, the file descriptor, <i>fd</i>, can be closed immediately without invalidating the mapping. </p>
<p> The <i>prot</i> argument describes the desired memory protection of the mapping (and must not conflict with the open mode of the file). It is either <code>PROT_NONE</code> or the bitwise OR of one or more of the following flags:</p>
<dl COMPACT>
<dt><code>PROT_EXEC</code></p>
<dd>Pages may be executed.</p>
<dt><code>PROT_READ</code></p>
<dd>Pages may be read.</p>
<dt><code>PROT_WRITE</code></p>
<dd>Pages may be written.</p>
<dt><code>PROT_NONE</code></p>
<dd>Pages may not be accessed.</dl>
<h3>The flags argument</h3>
<p>The <i>flags</i> argument determines whether updates to the mapping are visible to other processes mapping the same region, and whether updates are carried through to the underlying file. This behavior is determined by including exactly one of the following values in <i>flags</i>:</p>
<dl COMPACT>
<dt><code>MAP_SHARED</code></p>
<dd>Share this mapping. Updates to the mapping are visible to other processes mapping the same region, and (in the case of file-backed mappings) are carried through to the underlying file. (To precisely control when updates are carried through to the underlying file requires the use of <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2).)</p>
<dt><code>MAP_SHARED_VALIDATE</code> (since Linux 4.15)</p>
<dd>This flag provides the same behavior as <code>MAP_SHARED</code> except that <code>MAP_SHARED</code> mappings ignore unknown flags in <i>flags</i>. By contrast, when creating a mapping using <code>MAP_SHARED_VALIDATE</code>, the kernel verifies all passed flags are known and fails the mapping with the error <code>EOPNOTSUPP</code> for unknown flags. This mapping type is also required to be able to use some mapping flags (e.g., <code>MAP_SYNC</code>).</p>
<dt><code>MAP_PRIVATE</code></p>
<dd>Create a private copy-on-write mapping. Updates to the mapping are not visible to other processes mapping the same file, and are not carried through to the underlying file. It is unspecified whether changes made to the file after the <code>mmap</code>() call are visible in the mapped region.</dl>
<p> Both <code>MAP_SHARED</code> and <code>MAP_PRIVATE</code> are described in POSIX.1-2001 and POSIX.1-2008. <code>MAP_SHARED_VALIDATE</code> is a Linux extension. </p>
<p> In addition, zero or more of the following values can be ORed in <i>flags</i>:</p>
<dl COMPACT>
<dt><code>MAP_32BIT</code> (since Linux 2.4.20, 2.6)</p>
<dd>Put the mapping into the first 2 Gigabytes of the process address space. This flag is supported only on x86-64, for 64-bit programs. It was added to allow thread stacks to be allocated somewhere in the first 2 GB of memory, so as to improve context-switch performance on some early 64-bit processors. Modern x86-64 processors no longer have this performance problem, so use of this flag is not required on those systems. The <code>MAP_32BIT</code> flag is ignored when <code>MAP_FIXED</code> is set.</p>
<dt><code>MAP_ANON</code></p>
<dd>Synonym for <code>MAP_ANONYMOUS</code>; provided for compatibility with other implementations.</p>
<dt><code>MAP_ANONYMOUS</code></p>
<dd>The mapping is not backed by any file; its contents are initialized to zero. The <i>fd</i> argument is ignored; however, some implementations require <i>fd</i> to be -1 if <code>MAP_ANONYMOUS</code> (or <code>MAP_ANON</code>) is specified, and portable applications should ensure this. The <i>offset</i> argument should be zero. The use of <code>MAP_ANONYMOUS</code> in conjunction with <code>MAP_SHARED</code> is supported on Linux only since kernel 2.4.</p>
<dt><code>MAP_DENYWRITE</code></p>
<dd>This flag is ignored. (Long ago&#8212;Linux 2.0 and earlier&#8212;it signaled that attempts to write to the underlying file should fail with <code>ETXTBSY</code>. But this was a source of denial-of-service attacks.)</p>
<dt><code>MAP_EXECUTABLE</code></p>
<dd>This flag is ignored.</p>
<dt><code>MAP_FILE</code></p>
<dd>Compatibility flag. Ignored.</p>
<dt><code>MAP_FIXED</code></p>
<dd>Don&#8217;t interpret <i>addr</i> as a hint: place the mapping at exactly that address. <i>addr</i> must be suitably aligned: for most architectures a multiple of the page size is sufficient; however, some architectures may impose additional restrictions. If the memory region specified by <i>addr</i> and <i>len</i> overlaps pages of any existing mapping(s), then the overlapped part of the existing mapping(s) will be discarded. If the specified address cannot be used, <code>mmap</code>() will fail.</p>
<dd>Software that aspires to be portable should use the <code>MAP_FIXED</code> flag with care, keeping in mind that the exact layout of a process&#8217;s memory mappings is allowed to change significantly between kernel versions, C library versions, and operating system releases. <i>Carefully read the discussion of this flag in NOTES!</i></p>
<dt><code>MAP_FIXED_NOREPLACE</code> (since Linux 4.17)</p>
<dd>This flag provides behavior that is similar to <code>MAP_FIXED</code> with respect to the <i>addr</i> enforcement, but differs in that <code>MAP_FIXED_NOREPLACE</code> never clobbers a preexisting mapped range. If the requested range would collide with an existing mapping, then this call fails with the error <code>EEXIST.</code> This flag can therefore be used as a way to atomically (with respect to other threads) attempt to map an address range: one thread will succeed; all others will report failure.</p>
<dd>Note that older kernels which do not recognize the <code>MAP_FIXED_NOREPLACE</code> flag will typically (upon detecting a collision with a preexisting mapping) fall back to a &quot;non-<code>MAP_FIXED</code>&quot; type of behavior: they will return an address that is different from the requested address. Therefore, backward-compatible software should check the returned address against the requested address.</p>
<dt><code>MAP_GROWSDOWN</code></p>
<dd>This flag is used for stacks. It indicates to the kernel virtual memory system that the mapping should extend downward in memory. The return address is one page lower than the memory area that is actually created in the process&#8217;s virtual address space. Touching an address in the &quot;guard&quot; page below the mapping will cause the mapping to grow by a page. This growth can be repeated until the mapping grows to within a page of the high end of the next lower mapping, at which point touching the &quot;guard&quot; page will result in a <code>SIGSEGV</code> signal.</p>
<dt><code>MAP_HUGETLB</code> (since Linux 2.6.32)</p>
<dd>Allocate the mapping using &quot;huge pages.&quot; See the Linux kernel source file <i>Documentation/admin-guide/mm/hugetlbpage.rst</i> for further information, as well as NOTES, below.</p>
<dt><code>MAP_HUGE_2MB</code>, <code>MAP_HUGE_1GB</code> (since Linux 3.8)</p>
<dd>Used in conjunction with <code>MAP_HUGETLB</code> to select alternative hugetlb page sizes (respectively, 2 MB and 1 GB) on systems that support multiple hugetlb page sizes.</p>
<dd>More generally, the desired huge page size can be configured by encoding the base-2 logarithm of the desired page size in the six bits at the offset <code>MAP_HUGE_SHIFT</code>. (A value of zero in this bit field provides the default huge page size; the default huge page size can be discovered via the <i>Hugepagesize</i> field exposed by <i>/proc/meminfo</i>.) Thus, the above two constants are defined as:</p>
<dd>#define MAP_HUGE_2MB (21 &lt;&lt; MAP_HUGE_SHIFT) #define MAP_HUGE_1GB (30 &lt;&lt; MAP_HUGE_SHIFT)</p>
<dd>The range of huge page sizes that are supported by the system can be discovered by listing the subdirectories in <i>/sys/kernel/mm/hugepages</i>.</p>
<dt><code>MAP_LOCKED</code> (since Linux 2.5.37)</p>
<dd>Mark the mapped region to be locked in the same way as <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2). This implementation will try to populate (prefault) the whole range but the <code>mmap</code>() call doesn&#8217;t fail with <code>ENOMEM</code> if this fails. Therefore major faults might happen later on. So the semantic is not as strong as <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2). One should use <code>mmap</code>() plus <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2) when major faults are not acceptable after the initialization of the mapping. The <code>MAP_LOCKED</code> flag is ignored in older kernels.</p>
<dt><code>MAP_NONBLOCK</code> (since Linux 2.5.46)</p>
<dd>This flag is meaningful only in conjunction with <code>MAP_POPULATE</code>. Don&#8217;t perform read-ahead: create page tables entries only for pages that are already present in RAM. Since Linux 2.6.23, this flag causes <code>MAP_POPULATE</code> to do nothing. One day, the combination of <code>MAP_POPULATE</code> and <code>MAP_NONBLOCK</code> may be reimplemented.</p>
<dt><code>MAP_NORESERVE</code></p>
<dd>Do not reserve swap space for this mapping. When swap space is reserved, one has the guarantee that it is possible to modify the mapping. When swap space is not reserved one might get <code>SIGSEGV</code> upon a write if no physical memory is available. See also the discussion of the file <i>/proc/sys/vm/overcommit_memory</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5). In kernels before 2.6, this flag had effect only for private writable mappings.</p>
<dt><code>MAP_POPULATE</code> (since Linux 2.5.46)</p>
<dd>Populate (prefault) page tables for a mapping. For a file mapping, this causes read-ahead on the file. This will help to reduce blocking on page faults later. <code>MAP_POPULATE</code> is supported for private mappings only since Linux 2.6.23.</p>
<dt><code>MAP_STACK</code> (since Linux 2.6.27)</p>
<dd>Allocate the mapping at an address suitable for a process or thread stack.</p>
<dd>This flag is currently a no-op on Linux. However, by employing this flag, applications can ensure that they transparently obtain support if the flag is implemented in the future. Thus, it is used in the glibc threading implementation to allow for the fact that some architectures may (later) require special treatment for stack allocations. A further reason to employ this flag is portability: <code>MAP_STACK</code> exists (and has an effect) on some other systems (e.g., some of the BSDs).</p>
<dt><code>MAP_SYNC</code> (since Linux 4.15)</p>
<dd>This flag is available only with the <code>MAP_SHARED_VALIDATE</code> mapping type; mappings of type <code>MAP_SHARED</code> will silently ignore this flag. This flag is supported only for files supporting DAX (direct mapping of persistent memory). For other files, creating a mapping with this flag results in an <code>EOPNOTSUPP</code> error.</p>
<dd>Shared file mappings with this flag provide the guarantee that while some memory is mapped writable in the address space of the process, it will be visible in the same file at the same offset even after the system crashes or is rebooted. In conjunction with the use of appropriate CPU instructions, this provides users of such mappings with a more efficient way of making data modifications persistent.</p>
<dt><code>MAP_UNINITIALIZED</code> (since Linux 2.6.33)</p>
<dd>Don&#8217;t clear anonymous pages. This flag is intended to improve performance on embedded devices. This flag is honored only if the kernel was configured with the <code>CONFIG_MMAP_ALLOW_UNINITIALIZED</code> option. Because of the security implications, that option is normally enabled only on embedded devices (i.e., devices where one has complete control of the contents of user memory).</dl>
<p> Of the above flags, only <code>MAP_FIXED</code> is specified in POSIX.1-2001 and POSIX.1-2008. However, most systems also support <code>MAP_ANONYMOUS</code> (or its synonym <code>MAP_ANON</code>).</p>
<h3>munmap()</h3>
<p>The <code>munmap</code>() system call deletes the mappings for the specified address range, and causes further references to addresses within the range to generate invalid memory references. The region is also automatically unmapped when the process is terminated. On the other hand, closing the file descriptor does not unmap the region. </p>
<p> The address <i>addr</i> must be a multiple of the page size (but <i>length</i> need not be). All pages containing a part of the indicated range are unmapped, and subsequent references to these pages will generate <code>SIGSEGV</code>. It is not an error if the indicated range does not contain any mapped pages.</p>
<h2>Return Value</h2>
<p>On success, <code>mmap</code>() returns a pointer to the mapped area. On error, the value <code>MAP_FAILED</code> (that is, <i>(void&nbsp;*)&nbsp;-1</i>) is returned, and <i>errno</i> is set to indicate the cause of the error. </p>
<p> On success, <code>munmap</code>() returns 0. On failure, it returns -1, and <i>errno</i> is set to indicate the cause of the error (probably to <code>EINVAL</code>).</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EACCES</code></p>
<dd>A file descriptor refers to a non-regular file. Or a file mapping was requested, but <i>fd</i> is not open for reading. Or <code>MAP_SHARED</code> was requested and <code>PROT_WRITE</code> is set, but <i>fd</i> is not open in read/write (<code>O_RDWR</code>) mode. Or <code>PROT_WRITE</code> is set, but the file is append-only.</p>
<dt><code>EAGAIN</code></p>
<dd>The file has been locked, or too much memory has been locked (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)).</p>
<dt><code>EBADF</code></p>
<dd><i>fd</i> is not a valid file descriptor (and <code>MAP_ANONYMOUS</code> was not set).</p>
<dt><code>EEXIST</code></p>
<dd><code>MAP_FIXED_NOREPLACE</code> was specified in <i>flags</i>, and the range covered by <i>addr</i> and <i>length</i> clashes with an existing mapping.</p>
<dt><code>EINVAL</code></p>
<dd>We don&#8217;t like <i>addr</i>, <i>length</i>, or <i>offset</i> (e.g., they are too large, or not aligned on a page boundary).</p>
<dt><code>EINVAL</code></p>
<dd>(since Linux 2.6.12) <i>length</i> was 0.</p>
<dt><code>EINVAL</code></p>
<dd><i>flags</i> contained none of <code>MAP_PRIVATE</code>, <code>MAP_SHARED</code> or <code>MAP_SHARED_VALIDATE</code>.</p>
<dt><code>ENFILE</code></p>
<dd>The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd>The underlying filesystem of the specified file does not support memory mapping.</p>
<dt><code>ENOMEM</code></p>
<dd>No memory is available.</p>
<dt><code>ENOMEM</code></p>
<dd>The process&#8217;s maximum number of mappings would have been exceeded. This error can also occur for <code>munmap</code>(), when unmapping a region in the middle of an existing mapping, since this results in two smaller mappings on either side of the region being unmapped.</p>
<dt><code>ENOMEM</code></p>
<dd>(since Linux 4.7) The process&#8217;s <code>RLIMIT_DATA</code> limit, described in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), would have been exceeded.</p>
<dt><code>EOVERFLOW</code></p>
<dd>On 32-bit architecture together with the large file extension (i.e., using 64-bit <i>off_t</i>): the number of pages used for <i>length</i> plus number of pages used for <i>offset</i> would overflow <i>unsigned long</i> (32 bits).</p>
<dt><code>EPERM</code></p>
<dd>The <i>prot</i> argument asks for <code>PROT_EXEC</code> but the mapped area belongs to a file on a filesystem that was mounted no-exec.</p>
<dt><code>EPERM</code></p>
<dd>The operation was prevented by a file seal; see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).</p>
<dt><code>ETXTBSY</code></p>
<dd><code>MAP_DENYWRITE</code> was set but the object specified by <i>fd</i> is open for writing.</dl>
<p> Use of a mapped region can result in these signals:</p>
<dl COMPACT>
<dt><code>SIGSEGV</code></p>
<dd>Attempted write into a region mapped as read-only.</p>
<dt><code>SIGBUS</code></p>
<dd>Attempted access to a page of the buffer that lies beyond the end of the mapped file. For an explanation of the treatment of the bytes in the page that corresponds to the end of a mapped file that is not a multiple of the page size, see NOTES.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mmap</code>(), <code>munmap</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD. </p>
<p> On POSIX systems on which <code>mmap</code>(), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), and <code>munmap</code>() are available, <code>_POSIX_MAPPED_FILES</code> is defined in <i>&lt;unistd.h&gt;</i> to a value greater than 0. (See also <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3).)</p>
<h2>Notes</h2>
<p>Memory mapped by <code>mmap</code>() is preserved across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), with the same attributes. </p>
<p> A file is mapped in multiples of the page size. For a file that is not a multiple of the page size, the remaining bytes in the partial page at the end of the mapping are zeroed when mapped, and modifications to that region are not written out to the file. The effect of changing the size of the underlying file of a mapping on the pages that correspond to added or removed regions of the file is unspecified. </p>
<p> On some hardware architectures (e.g., i386), <code>PROT_WRITE</code> implies <code>PROT_READ</code>. It is architecture dependent whether <code>PROT_READ</code> implies <code>PROT_EXEC</code> or not. Portable programs should always set <code>PROT_EXEC</code> if they intend to execute code in the new mapping. </p>
<p> The portable way to create a mapping is to specify <i>addr</i> as 0 (NULL), and omit <code>MAP_FIXED</code> from <i>flags</i>. In this case, the system chooses the address for the mapping; the address is chosen so as not to conflict with any existing mapping, and will not be 0. If the <code>MAP_FIXED</code> flag is specified, and <i>addr</i> is 0 (NULL), then the mapped address will be 0 (NULL). </p>
<p> Certain <i>flags</i> constants are defined only if suitable feature test macros are defined (possibly by default): <code>_DEFAULT_SOURCE</code> with glibc 2.19 or later; or <code>_BSD_SOURCE</code> or <code>_SVID_SOURCE</code> in glibc 2.19 and earlier. (Employing <code>_GNU_SOURCE</code> also suffices, and requiring that macro specifically would have been more logical, since these flags are all Linux-specific.) The relevant flags are: <code>MAP_32BIT</code>, <code>MAP_ANONYMOUS</code> (and the synonym <code>MAP_ANON</code>), <code>MAP_DENYWRITE</code>, <code>MAP_EXECUTABLE</code>, <code>MAP_FILE</code>, <code>MAP_GROWSDOWN</code>, <code>MAP_HUGETLB</code>, <code>MAP_LOCKED</code>, <code>MAP_NONBLOCK</code>, <code>MAP_NORESERVE</code>, <code>MAP_POPULATE</code>, and <code>MAP_STACK</code>. </p>
<p> An application can determine which pages of a mapping are currently resident in the buffer/page cache using <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2).</p>
<h3>Using MAP_FIXED safely</h3>
<p>The only safe use for <code>MAP_FIXED</code> is where the address range specified by <i>addr</i> and <i>length</i> was previously reserved using another mapping; otherwise, the use of <code>MAP_FIXED</code> is hazardous because it forcibly removes preexisting mappings, making it easy for a multithreaded process to corrupt its own address space. </p>
<p> For example, suppose that thread A looks through <i>/proc/&lt;pid&gt;/maps</i> in order to locate an unused address range that it can map using <code>MAP_FIXED</code>, while thread B simultaneously acquires part or all of that same address range. When thread A subsequently employs <code>mmap(MAP_FIXED)</code>, it will effectively clobber the mapping that thread B created. In this scenario, thread B need not create a mapping directly; simply making a library call that, internally, uses <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) to load some other shared library, will suffice. The <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3) call will map the library into the process&#8217;s address space. Furthermore, almost any library call may be implemented in a way that adds memory mappings to the address space, either with this technique, or by simply allocating memory. Examples include <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), and the PAM libraries </p>
<p> Since Linux 4.17, a multithreaded program can use the <code>MAP_FIXED_NOREPLACE</code> flag to avoid the hazard described above when attempting to create a mapping at a fixed address that has not been reserved by a preexisting mapping.</p>
<h3>Timestamps changes for file-backed mappings</h3>
<p>For file-backed mappings, the <i>st_atime</i> field for the mapped file may be updated at any time between the <code>mmap</code>() and the corresponding unmapping; the first reference to a mapped page will update the field if it has not been already. </p>
<p> The <i>st_ctime</i> and <i>st_mtime</i> field for a file mapped with <code>PROT_WRITE</code> and <code>MAP_SHARED</code> will be updated after a write to the mapped region, and before a subsequent <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2) with the <code>MS_SYNC</code> or <code>MS_ASYNC</code> flag, if one occurs.</p>
<h3>Huge page (Huge TLB) mappings</h3>
<p>For mappings that employ huge pages, the requirements for the arguments of <code>mmap</code>() and <code>munmap</code>() differ somewhat from the requirements for mappings that use the native system page size. </p>
<p> For <code>mmap</code>(), <i>offset</i> must be a multiple of the underlying huge page size. The system automatically aligns <i>length</i> to be a multiple of the underlying huge page size. </p>
<p> For <code>munmap</code>(), <i>addr</i>, and <i>length</i> must both be a multiple of the underlying huge page size.</p>
<h3>C library/kernel differences</h3>
<p>This page describes the interface provided by the glibc <code>mmap</code>() wrapper function. Originally, this function invoked a system call of the same name. Since kernel 2.4, that system call has been superseded by <code><a href="/docs/linux/man/2-mmap2/">mmap2</a></code>(2), and nowadays the glibc <code>mmap</code>() wrapper function invokes <code><a href="/docs/linux/man/2-mmap2/">mmap2</a></code>(2) with a suitably adjusted value for <i>offset</i>.</p>
<h2>Bugs</h2>
<p>On Linux, there are no guarantees like those suggested above under <code>MAP_NORESERVE</code>. By default, any process can be killed at any moment when the system runs out of memory. </p>
<p> In kernels before 2.6.7, the <code>MAP_POPULATE</code> flag has effect only if <i>prot</i> is specified as <code>PROT_NONE</code>. </p>
<p> SUSv3 specifies that <code>mmap</code>() should fail if <i>length</i> is 0. However, in kernels before 2.6.12, <code>mmap</code>() succeeded in this case: no mapping was created and the call returned <i>addr</i>. Since kernel 2.6.12, <code>mmap</code>() fails with the error <code>EINVAL</code> for this case. </p>
<p> POSIX specifies that the system shall always zero fill any partial page at the end of the object and that system will never write any modification of the object beyond its end. On Linux, when you write data to such partial page after the end of the object, the data stays in the page cache even after the file is closed and unmapped and even though the data is never written to the file itself, subsequent mappings may see the modified content. In some cases, this could be fixed by calling <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2) before the unmap takes place; however, this doesn&#8217;t work on <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) (for example, when using the POSIX shared memory interface documented in <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7)).</p>
<h2>Examples</h2>
<p>The following program prints part of the file specified in its first command-line argument to standard output. The range of bytes to be printed is specified via offset and length values in the second and third command-line arguments. The program creates a memory mapping of the required pages of the file and then uses <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to output the desired bytes.</p>
<h3>Program source</h3>
<p>#include &lt;sys/mman.h&gt; #include &lt;sys/stat.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stat sb;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_t offset, pa_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t length;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;3 || argc&nbsp;&gt;&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;%s file offset&nbsp;[length]
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fstat(fd,&nbsp;&amp;sb)&nbsp;==&nbsp;-1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;To obtain file size&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;fstat&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;offset&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pa_offset&nbsp;=&nbsp;offset&nbsp;&amp;&nbsp;~(sysconf(_SC_PAGE_SIZE)&nbsp;&#8211; 1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;offset for mmap()&nbsp;must be page aligned&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(offset&nbsp;&gt;=&nbsp;sb.st_size)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;offset is past end of file
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;==&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;length&nbsp;=&nbsp;atoi(argv[3]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(offset&nbsp;+&nbsp;length&nbsp;&gt;&nbsp;sb.st_size)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;length&nbsp;=&nbsp;sb.st_size &#8211; offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Can&#8217;t display bytes past end of file&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;No length arg&nbsp;==&gt;&nbsp;display to end of file&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;length&nbsp;=&nbsp;sb.st_size &#8211; offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr&nbsp;=&nbsp;mmap(NULL, length&nbsp;+&nbsp;offset &#8211; pa_offset, PROT_READ,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MAP_PRIVATE, fd, pa_offset);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(addr&nbsp;==&nbsp;MAP_FAILED)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;mmap&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;write(STDOUT_FILENO, addr&nbsp;+&nbsp;offset &#8211; pa_offset, length);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;length)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;write&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;partial write&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;munmap(addr, length&nbsp;+&nbsp;offset &#8211; pa_offset);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a></code>(2), <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/2-memfd_create/">memfd_create</a></code>(2), <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2), <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mmap2/">mmap2</a></code>(2), <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/2-mremap/">mremap</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), <code><a href="/docs/linux/man/2-remap_file_pages/">remap_file_pages</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2), <code><a href="/docs/linux/man/3-shm_open/">shm_open</a></code>(3), <code><a href="/docs/linux/man/7-shm_overview/">shm_overview</a></code>(7) </p>
<p> The descriptions of the following files in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5): <i>/proc/[pid]/maps</i>, <i>/proc/[pid]/map_files</i>, and <i>/proc/[pid]/smaps</i>. </p>
<p> B.O. Gallmeister, POSIX.4, O&#8217;Reilly, pp. 128-129 and 389-391.</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
