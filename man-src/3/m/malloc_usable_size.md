---
title: "malloc_usable_size(3)"
name: "malloc_usable_size"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc_usable_size/"
description: "malloc_usable_size – obtain size of block of memory allocated from heap"
---

<h2 class="name">NAME</h2>
<p> malloc_usable_size &#8211; obtain size of block of memory allocated from heap </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;malloc.h&gt;</code> </p>
<p> <code>size_t malloc_usable_size (void *</code><i>ptr</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>malloc_usable_size</code>() function returns the number of usable bytes in the block pointed to by <i>ptr</i>, a pointer to a block of memory allocated by <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) or a related function.</p>
<h2>RETURN VALUE</h2>
<p> <code>malloc_usable_size</code>() returns the number of usable bytes in the block of allocated memory pointed to by <i>ptr</i>. If <i>ptr</i> is NULL, 0 is returned.</p>
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
<td> <code>malloc_usable_size</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>NOTES</h2>
<p> The value returned by <code>malloc_usable_size</code>() may be greater than the requested size of the allocation because of alignment and minimum size constraints. Although the excess bytes can be overwritten by the application without ill effects, this is not good programming practice: the number of excess bytes in an allocation depends on the underlying implementation. </p>
<p> The main use of this function is for debugging and introspection.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
