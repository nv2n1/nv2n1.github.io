---
title: "malloc_stats(3)"
name: "malloc_stats"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc_stats/"
description: "malloc_stats – print memory allocation statistics"
---

<h2 class="name">NAME</h2>
<p> malloc_stats &#8211; print memory allocation statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;malloc.h&gt;</code> </p>
<p> <code>void malloc_stats(void);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>malloc_stats</code>() function prints (on standard error) statistics about memory allocated by <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and related functions. For each arena (allocation area), this function prints the total amount of memory allocated and the total number of bytes consumed by in-use allocations. (These two values correspond to the <i>arena</i> and <i>uordblks</i> fields retrieved by <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3).) In addition, the function prints the sum of these two statistics for all arenas, and the maximum number of blocks and bytes that were ever simultaneously allocated using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
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
<td> <code>malloc_stats</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>NOTES</h2>
<p> More detailed information about memory allocations in the main arena can be obtained using <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-malloc_info/">malloc_info</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
