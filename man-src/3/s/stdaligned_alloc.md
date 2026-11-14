---
title: "stdaligned_alloc(3)"
name: "stdaligned_alloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdaligned_alloc/"
---

std::aligned_alloc - std::aligned_alloc

<h2>Synopsis</h2>

Defined in header &lt;cstdlib&gt; 
void* aligned_alloc( std::size_t alignment, std::size_t size ); <i>(since C++17)</i> 
Allocate size bytes of uninitialized storage whose alignment is specified by alignment. The size parameter must be an integral multiple of alignment. 
The following functions are required to be thread-safe: 
* The library versions of operator_new and operator_delete 
* User replacement versions of global operator_new and operator_delete 
* std::calloc, std::malloc, std::realloc <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;, std::aligned_alloc 
&nbsp;<wbr>&nbsp;<i>(since C++17)</i>, std::free 
Calls to these functions that allocate or deallocate a particular unit of storage occur in a single total order, and each such deallocation call happens-before the next allocation (if any) in this order. 

<h2>Parameters</h2>

alignment - specifies the alignment. Must be a valid alignment supported by the implementation. 
size - number of bytes to allocate. An integral multiple of alignment

<h2>Return value</h2>

On success, returns the pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with std::free() or std::realloc(). 
On failure, returns a null pointer. 

<h2>Notes</h2>

<pre><code>Passing a size which is not an integral multiple of alignment or an alignment which is not valid or not supported by the implementation causes the function to fail and return a null pointer (C11, as published, specified undefined behavior in this case, this was corrected by DR 460).

As an example of the &quot;supported by the implementation&quot; requirement, POSIX function posix_memalign accepts any alignment that is a power of two and a multiple of sizeof(void*), and POSIX-based implementations of aligned_alloc inherit this requirements.

Regular std::malloc aligns memory suitable for any object type (which, in practice, means that it is aligned to alignof(std::max_align_t)). This function is useful for over-aligned allocations, such as to SSE, cache line, or VM page boundary.
</code></pre>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;cstdlib&gt;
int main()

{
    int *p1 = static_cast&lt;int *&gt;(std::malloc(10 * sizeof *p1));
    std::printf(&quot;default-aligned address:   %p\n&quot;, static_cast&lt;void *&gt;(p1));
    std::free(p1);
    int *p2 = static_cast&lt;int *&gt;(std::aligned_alloc(1024, 1024));
    std::printf(&quot;1024-byte aligned address: %p\n&quot;, static_cast&lt;void *&gt;(p2));
    std::free(p2);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;default-aligned address: 0x2221c20 
&nbsp;<wbr>&nbsp;1024-byte aligned address: 0x2222400

<h2>See also</h2>

aligned_storage defines the type suitable for use as uninitialized storage for types of given size 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
