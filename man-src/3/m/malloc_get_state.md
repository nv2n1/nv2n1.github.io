---
title: "malloc_get_state(3)"
name: "malloc_get_state"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc_get_state/"
description: "malloc_get_state, malloc_set_state – record and restore state of malloc implementation"
---

<h2 class="name">NAME</h2>
<p> malloc_get_state, malloc_set_state &#8211; record and restore state of malloc implementation </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;malloc.h&gt;
void *malloc_get_state(void);
int malloc_set_state(void *state);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: these function are removed in glibc version 2.25. </p>
<p> The <code>malloc_get_state</code>() function records the current state of all <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) internal bookkeeping variables (but not the actual contents of the heap or the state of <code><a href="/docs/linux/man/3-malloc_hook/">malloc_hook</a></code>(3) functions pointers). The state is recorded in a system-dependent opaque data structure dynamically allocated via <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and a pointer to that data structure is returned as the function result. (It is the caller&#8217;s responsibility to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) this memory.) </p>
<p> The <code>malloc_set_state</code>() function restores the state of all <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) internal bookkeeping variables to the values recorded in the opaque data structure pointed to by <i>state</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>malloc_get_state</code>() returns a pointer to a newly allocated opaque data structure. On error (for example, memory could not be allocated for the data structure), <code>malloc_get_state</code>() returns NULL. </p>
<p> On success, <code>malloc_set_state</code>() returns 0. If the implementation detects that <i>state</i> does not point to a correctly formed data structure, <code>malloc_set_state</code>() returns -1. If the implementation detects that the version of the data structure referred to by <i>state</i> is a more recent version than this implementation knows about, <code>malloc_set_state</code>() returns -2.</p>
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
<td> <code>malloc_get_state</code>(), <code>malloc_set_state</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> These functions are useful when using this <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) implementation as part of a shared library, and the heap contents are saved/restored via some other method. This technique is used by GNU Emacs to implement its &quot;dumping&quot; function. </p>
<p> Hook function pointers are never saved or restored by these functions, with two exceptions: if malloc checking (see <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)) was in use when <code>malloc_get_state</code>() was called, then <code>malloc_set_state</code>() resets malloc checking hooks if possible; if malloc checking was not in use in the recorded state, but the caller has requested malloc checking, then the hooks are reset to 0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
