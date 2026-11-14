---
title: "malloc_trim(3)"
name: "malloc_trim"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc_trim/"
description: "malloc_trim – release free memory from the heap"
---

<h2 class="name">NAME</h2>
<p> malloc_trim &#8211; release free memory from the heap </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;malloc.h&gt;</code> </p>
<p> <code>int malloc_trim(size_t </code><i>pad</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>malloc_trim</code>() function attempts to release free memory from the heap (by calling <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) or <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) with suitable arguments). </p>
<p> The <i>pad</i> argument specifies the amount of free space to leave untrimmed at the top of the heap. If this argument is 0, only the minimum amount of memory is maintained at the top of the heap (i.e., one page or less). A nonzero argument can be used to maintain some trailing space at the top of the heap in order to allow future allocations to be made without having to extend the heap with <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> The <code>malloc_trim</code>() function returns 1 if memory was actually released back to the system, or 0 if it was not possible to release any memory.</p>
<h2>ERRORS</h2>
<p> No errors are defined.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>malloc_trim</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>NOTES</h2>
<p> This function is automatically called by <code><a href="/docs/linux/man/3-free/">free</a></code>(3) in certain circumstances; see the discussion of <code>M_TOP_PAD</code> and <code>M_TRIM_THRESHOLD</code> in <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3). </p>
<p> Only the main heap (using <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)) honors the <i>pad</i> argument; thread heaps do not. </p>
<p> Since glibc 2.8 this function frees memory in all arenas and in all chunks with whole free pages. </p>
<p> Before glibc 2.8 this function only freed memory at the top of the heap in the main arena.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
