---
title: "reallocf(3)"
name: "reallocf"
section: "3"
letter: "r"
url: "/docs/linux/man/3-reallocf/"
description: "reallocf – general purpose memory allocation functions"
---

<p><code>reallocf</code> &#8211; general purpose memory allocation functions</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/stdlib.h Ft void * Fn reallocf void *ptr size_t size</p>
<h2>Description</h2>
<p>The Fn reallocf function changes the size of the previously allocated memory referenced by Fa ptr to Fa size bytes. The contents of the memory are unchanged up to the lesser of the new and old sizes. If the new size is larger, the contents of the newly allocated portion of the memory are undefined. Upon success, the memory referenced by Fa ptr is freed and a pointer to the newly allocated memory is returned. Note that Fn reallocf may move the memory allocation, resulting in a different return value than Fa ptr . If Fa ptr is <code>NULL</code> the Fn reallocf function behaves identically to Fn malloc for the specified size. Upon failure, when the requested memory cannot be allocated, the passed pointer is freed to ease the problems with traditional coding styles for Fn reallocf causing memory leaks in libraries.</p>
<h2>Return Values</h2>
<p>The Fn reallocf function returns a pointer, possibly identical to Fa ptr , to the allocated memory if successful; otherwise a <code>NULL</code> pointer is returned, and <i>errno</i> is set to Er ENOMEM if the error was the result of an allocation failure. The buffer is deallocated in this case.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/2-brk/">brk</a>(2), <a href="/docs/linux/man/2-mmap/">mmap</a>(2), <a href="/docs/linux/man/3-alloca/">alloca</a>(3), <a href="/docs/linux/man/3-calloc/">calloc</a>(3), <a href="/docs/linux/man/3-free/">free</a>(3), <a href="/docs/linux/man/3-malloc/">malloc</a>(3), posix_memalign3, <a href="/docs/linux/man/3-realloc/">realloc</a>(3),</p>
<h2>History</h2>
<p>The Fn reallocf function first appeared in Fx 3.0 .</p>
