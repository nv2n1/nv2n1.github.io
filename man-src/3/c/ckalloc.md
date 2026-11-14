---
title: "ckalloc(3)"
name: "ckalloc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ckalloc/"
description: "Tcl_Alloc, Tcl_Free, Tcl_Realloc, Tcl_AttemptAlloc, Tcl_AttemptRealloc, ckalloc, ckfree, ckrealloc, attemptckalloc, attemptckrealloc – allocate or free heap memory"
---

<h2 class="name">NAME</h2>
<p> Tcl_Alloc, Tcl_Free, Tcl_Realloc, Tcl_AttemptAlloc, Tcl_AttemptRealloc, ckalloc, ckfree, ckrealloc, attemptckalloc, attemptckrealloc &#8211; allocate or free heap memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;tcl.h&gt;
char *
Tcl_Alloc(size) void Tcl_Free(ptr) char *Tcl_Realloc(ptr, size)
char *
Tcl_AttemptAlloc(size)
char *
Tcl_AttemptRealloc(ptr, size)
char *
ckalloc(size) void ckfree(ptr) char *ckrealloc(ptr, size)
char *
attemptckalloc(size)
char *
attemptckrealloc(ptr, size)
</code></pre>
<h2>ARGUMENTS</h2>
<dl>
<dt>
<dd> unsigned int <i>size</i> (in) Size in bytes of the memory block to allocate.</p>
<dt>
<dd> char <i>*ptr</i> (in) Pointer to memory block to free or realloc. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> These procedures provide a platform and compiler independent interface for memory allocation. Programs that need to transfer ownership of memory blocks between Tcl and other modules should use these routines rather than the native <code>malloc()</code> and <code>free()</code> routines provided by the C run-time library. </p>
<p> <code>Tcl_Alloc</code> returns a pointer to a block of at least <i>size</i> bytes suitably aligned for any use. </p>
<p> <code>Tcl_Free</code> makes the space referred to by <i>ptr</i> available for further allocation. </p>
<p> <code>Tcl_Realloc</code> changes the size of the block pointed to by <i>ptr</i> to <i>size</i> bytes and returns a pointer to the new block. The contents will be unchanged up to the lesser of the new and old sizes. The returned location may be different from <i>ptr</i>. If <i>ptr</i> is NULL, this is equivalent to calling <code>Tcl_Alloc</code> with just the <i>size</i> argument. </p>
<p> <code>Tcl_AttemptAlloc</code> and <code>Tcl_AttemptRealloc</code> are identical in function to <code>Tcl_Alloc</code> and <code>Tcl_Realloc</code>, except that <code>Tcl_AttemptAlloc</code> and <code>Tcl_AttemptRealloc</code> will not cause the Tcl interpreter to <code>panic</code> if the memory allocation fails. If the allocation fails, these functions will return NULL. Note that on some platforms, but not all, attempting to allocate a zero-sized block of memory will also cause these functions to return NULL. </p>
<p> The procedures <code>ckalloc</code>, <code>ckfree</code>, <code>ckrealloc</code>, <code>attemptckalloc</code>, and <code>attemptckrealloc</code> are implemented as macros. Normally, they are synonyms for the corresponding procedures documented on this page. When Tcl and all modules calling Tcl are compiled with <code>TCL_MEM_DEBUG</code> defined, however, these macros are redefined to be special debugging versions of these procedures. To support Tcl&#8217;s memory debugging within a module, use the macros rather than direct calls to <code>Tcl_Alloc</code>, etc. </p>
<h2>KEYWORDS</h2>
<p> alloc, allocation, free, malloc, memory, realloc, TCL_MEM_DEBUG </p>
<h2>Index</h2>
