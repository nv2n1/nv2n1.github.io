---
title: "malloc_hook(3)"
name: "malloc_hook"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc_hook/"
description: "__malloc_hook, __malloc_initialize_hook, __memalign_hook, __free_hook, __realloc_hook, __after_morecore_hook – malloc debugging variables"
---

<h2 class="name">NAME</h2>
<p> __malloc_hook, __malloc_initialize_hook, __memalign_hook, __free_hook, __realloc_hook, __after_morecore_hook &#8211; malloc debugging variables </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;malloc.h&gt;
void *(*__malloc_hook)(size_t size, const void *caller);
void *(*__realloc_hook)(void *ptr, size_t size, const void *caller);
void *(*__memalign_hook)(size_t alignment, size_t size,
                         const void *caller);
void (*__free_hook)(void *ptr, const void *caller);
void (*__malloc_initialize_hook)(void);
void (*__after_morecore_hook)(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The GNU C library lets you modify the behavior of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), and <code><a href="/docs/linux/man/3-free/">free</a></code>(3) by specifying appropriate hook functions. You can use these hooks to help you debug programs that use dynamic memory allocation, for example. </p>
<p> The variable <code>__malloc_initialize_hook</code> points at a function that is called once when the malloc implementation is initialized. This is a weak variable, so it can be overridden in the application with a definition like the following: </p>
<p> void (*__malloc_initialize_hook)(void) = my_init_hook; </p>
<p> Now the function <i>my_init_hook</i>() can do the initialization of all hooks. </p>
<p> The four functions pointed to by <code>__malloc_hook</code>, <code>__realloc_hook</code>, <code>__memalign_hook</code>, <code>__free_hook</code> have a prototype like the functions <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), <code><a href="/docs/linux/man/3-memalign/">memalign</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), respectively, except that they have a final argument <i>caller</i> that gives the address of the caller of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), etc. </p>
<p> The variable <code>__after_morecore_hook</code> points at a function that is called each time after <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) was asked for more memory.</p>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions.</p>
<h2>NOTES</h2>
<p> The use of these hook functions is not safe in multithreaded programs, and they are now deprecated. From glibc 2.24 onwards, the <code>__malloc_initialize_hook</code> variable has been removed from the API. Programmers should instead preempt calls to the relevant functions by defining and exporting functions such as &quot;malloc&quot; and &quot;free&quot;.</p>
<h2>EXAMPLES</h2>
<p> Here is a short example of how to use these variables. </p>
<p> #include &lt;stdio.h&gt; #include &lt;malloc.h&gt; </p>
<p> /* Prototypes for our hooks. */ static void my_init_hook(void); static void *my_malloc_hook(size_t, const void *); </p>
<p> /* Variables to save original hooks. */ static void *(*old_malloc_hook)(size_t, const void *); </p>
<p> /* Override initializing hook from the C library. */ void (*__malloc_initialize_hook) (void) = my_init_hook; </p>
<p> static void my_init_hook(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;old_malloc_hook&nbsp;=&nbsp;__malloc_hook;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__malloc_hook&nbsp;=&nbsp;my_malloc_hook; } </p>
<p> static void * my_malloc_hook(size_t size, const void *caller) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*result; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Restore all old hooks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__malloc_hook&nbsp;=&nbsp;old_malloc_hook; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Call recursively&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;result&nbsp;=&nbsp;malloc(size); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Save underlying hooks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;old_malloc_hook&nbsp;=&nbsp;__malloc_hook; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;printf()&nbsp;might call malloc(), so protect it too.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;malloc(%zu)&nbsp;called from&nbsp;%p returns&nbsp;%p
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size, caller, result); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Restore our own hooks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__malloc_hook&nbsp;=&nbsp;my_malloc_hook; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return result; }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mallinfo/">mallinfo</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-mcheck/">mcheck</a></code>(3), <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
