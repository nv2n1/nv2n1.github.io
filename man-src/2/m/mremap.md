---
title: "mremap(2)"
name: "mremap"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mremap/"
description: "mremap – remap a virtual memory address"
---

<h2 class="name">NAME</h2>
<p> mremap &#8211; remap a virtual memory address </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/mman.h&gt;
void *mremap(void *old_address, size_t old_size,
             size_t new_size, int flags, ... /* void *new_address */);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mremap</code>() expands (or shrinks) an existing memory mapping, potentially moving it at the same time (controlled by the <i>flags</i> argument and the available virtual address space). </p>
<p> <i>old_address</i> is the old address of the virtual memory block that you want to expand (or shrink). Note that <i>old_address</i> has to be page aligned. <i>old_size</i> is the old size of the virtual memory block. <i>new_size</i> is the requested size of the virtual memory block after the resize. An optional fifth argument, <i>new_address</i>, may be provided; see the description of <code>MREMAP_FIXED</code> below. </p>
<p> If the value of <i>old_size</i> is zero, and <i>old_address</i> refers to a shareable mapping (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_SHARED</code>), then <code>mremap</code>() will create a new mapping of the same pages. <i>new_size</i> will be the size of the new mapping and the location of the new mapping may be specified with <i>new_address</i>; see the description of <code>MREMAP_FIXED</code> below. If a new mapping is requested via this method, then the <code>MREMAP_MAYMOVE</code> flag must also be specified. </p>
<p> The <i>flags</i> bit-mask argument may be 0, or include the following flags:</p>
<dl>
<dt><code>MREMAP_MAYMOVE</code></p>
<dd> By default, if there is not sufficient space to expand a mapping at its current location, then <code>mremap</code>() fails. If this flag is specified, then the kernel is permitted to relocate the mapping to a new virtual address, if necessary. If the mapping is relocated, then absolute pointers into the old mapping location become invalid (offsets relative to the starting address of the mapping should be employed).</p>
<dt><code>MREMAP_FIXED</code> (since Linux 2.3.31)</p>
<dd> This flag serves a similar purpose to the <code>MAP_FIXED</code> flag of <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). If this flag is specified, then <code>mremap</code>() accepts a fifth argument, <i>void&nbsp;*new_address</i>, which specifies a page-aligned address to which the mapping must be moved. Any previous mapping at the address range specified by <i>new_address</i> and <i>new_size</i> is unmapped.</p>
<dt>
<dd> If <code>MREMAP_FIXED</code> is specified, then <code>MREMAP_MAYMOVE</code> must also be specified.</p>
<dt><code>MREMAP_DONTUNMAP</code> (since Linux 5.7)</p>
<dd> This flag, which must be used in conjunction with <code>MREMAP_MAYMOVE</code>, remaps a mapping to a new address but does not unmap the mapping at <i>old_address</i>.</p>
<dt>
<dd> The <code>MREMAP_DONTUNMAP</code> flag can be used only with private anonymous mappings (see the description of <code>MAP_PRIVATE</code> and <code>MAP_ANONYMOUS</code> in <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)).</p>
<dt>
<dd> After completion, any access to the range specified by <i>old_address</i> and <i>old_size</i> will result in a page fault. The page fault will be handled by a <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2) handler if the address is in a range previously registered with <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2). Otherwise, the kernel allocates a zero-filled page to handle the fault.</p>
<dt>
<dd> The <code>MREMAP_DONTUNMAP</code> flag may be used to atomically move a mapping while leaving the source mapped. See NOTES for some possible applications of <code>MREMAP_DONTUNMAP</code>.</dl>
<p> If the memory segment specified by <i>old_address</i> and <i>old_size</i> is locked (using <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2) or similar), then this lock is maintained when the segment is resized and/or relocated. As a consequence, the amount of memory locked by the process may change.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>mremap</code>() returns a pointer to the new virtual memory area. On error, the value <code>MAP_FAILED</code> (that is, <i>(void&nbsp;*)&nbsp;-1</i>) is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd> The caller tried to expand a memory segment that is locked, but this was not possible without exceeding the <code>RLIMIT_MEMLOCK</code> resource limit.</p>
<dt><code>EFAULT</code></p>
<dd> Some address in the range <i>old_address</i> to <i>old_address</i>+<i>old_size</i> is an invalid virtual memory address for this process. You can also get <code>EFAULT</code> even if there exist mappings that cover the whole address space requested, but those mappings are of different types.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid argument was given. Possible causes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> <i>old_address</i> was not page aligned;</p>
<dt>*</p>
<dd> a value other than <code>MREMAP_MAYMOVE</code> or <code>MREMAP_FIXED</code> or <code>MREMAP_DONTUNMAP</code> was specified in <i>flags</i>;</p>
<dt>*</p>
<dd> <i>new_size</i> was zero;</p>
<dt>*</p>
<dd> <i>new_size</i> or <i>new_address</i> was invalid;</p>
<dt>*</p>
<dd> the new address range specified by <i>new_address</i> and <i>new_size</i> overlapped the old address range specified by <i>old_address</i> and <i>old_size</i>;</p>
<dt>*</p>
<dd> <code>MREMAP_FIXED</code> or <code>MREMAP_DONTUNMAP</code> was specified without also specifying <code>MREMAP_MAYMOVE</code>;</p>
<dt>*</p>
<dd> <code>MREMAP_DONTUNMAP</code> was specified, but one or more pages in the range specified by <i>old_address</i> and <i>old_size</i> were not private anonymous;</p>
<dt>*</p>
<dd> <code>MREMAP_DONTUNMAP</code> was specified and <i>old_size</i> was not equal to <i>new_size</i>;</p>
<dt>*</p>
<dd> <i>old_size</i> was zero and <i>old_address</i> does not refer to a shareable mapping (but see BUGS);</p>
<dt>*</p>
<dd> <i>old_size</i> was zero and the <code>MREMAP_MAYMOVE</code> flag was not specified.</dl>
</dl>
<dt><code>ENOMEM</code></p>
<dd> Not enough memory was available to complete the operation. Possible causes are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The memory area cannot be expanded at the current virtual address, and the <code>MREMAP_MAYMOVE</code> flag is not set in <i>flags</i>. Or, there is not enough (virtual) memory available.</p>
<dt>*</p>
<dd> <code>MREMAP_DONTUNMAP</code> was used causing a new mapping to be created that would exceed the (virtual) memory available. Or, it would exceed the maximum number of allowed mappings.</dl>
</dl>
</dl>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> <code>mremap</code>() changes the mapping between virtual addresses and memory pages. This can be used to implement a very efficient <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3). </p>
<p> In Linux, memory is divided into pages. A process has (one or) several linear virtual memory segments. Each virtual memory segment has one or more mappings to real memory pages (in the page table). Each virtual memory segment has its own protection (access rights), which may cause a segmentation violation (<code>SIGSEGV</code>) if the memory is accessed incorrectly (e.g., writing to a read-only segment). Accessing virtual memory outside of the segments will also cause a segmentation violation. </p>
<p> If <code>mremap</code>() is used to move or expand an area locked with <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2) or equivalent, the <code>mremap</code>() call will make a best effort to populate the new area but will not fail with <code>ENOMEM</code> if the area cannot be populated. </p>
<p> Prior to version 2.4, glibc did not expose the definition of <code>MREMAP_FIXED</code>, and the prototype for <code>mremap</code>() did not allow for the <i>new_address</i> argument.</p>
<h3>MREMAP_DONTUNMAP use cases</h3>
<p> Possible applications for <code>MREMAP_DONTUNMAP</code> include:</p>
<dl>
<dt>*</p>
<dd> Non-cooperative <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2): an application can yank out a virtual address range using <code>MREMAP_DONTUNMAP</code> and then employ a <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2) handler to handle the page faults that subsequently occur as other threads in the process touch pages in the yanked range.</p>
<dt>*</p>
<dd> Garbage collection: <code>MREMAP_DONTUNMAP</code> can be used in conjunction with <code><a href="/docs/linux/man/2-userfaultfd/">userfaultfd</a></code>(2) to implement garbage collection algorithms (e.g., in a Java virtual machine). Such an implementation can be cheaper (and simpler) than conventional garbage collection techniques that involve marking pages with protection <code>PROT_NONE</code> in conjunction with the of a <code>SIGSEGV</code> handler to catch accesses to those pages.</dl>
<h2>BUGS</h2>
<p> Before Linux 4.14, if <i>old_size</i> was zero and the mapping referred to by <i>old_address</i> was a private mapping (<code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) <code>MAP_PRIVATE</code>), <code>mremap</code>() created a new private mapping unrelated to the original mapping. This behavior was unintended and probably unexpected in user-space applications (since the intention of <code>mremap</code>() is to create a new mapping based on the original mapping). Since Linux 4.14, <code>mremap</code>() fails with the error <code>EINVAL</code> in this scenario.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-mlock/">mlock</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3) </p>
<p> Your favorite text book on operating systems for more information on paged memory (e.g., <i>Modern Operating Systems</i> by Andrew S. Tanenbaum, <i>Inside Linux</i> by Randolph Bentson, <i>The Design of the UNIX Operating System</i> by Maurice J. Bach)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
