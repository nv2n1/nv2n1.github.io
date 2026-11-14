---
title: "stdmalloc(3)"
name: "stdmalloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmalloc/"
---

std::malloc - std::malloc

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    void *malloc(std::size_t size);</code></pre> 
Allocates size bytes of uninitialized storage. 
If allocation succeeds, returns a pointer to the lowest (first) byte in the allocated memory block that is suitably aligned for any scalar type. 
If size is zero, the behavior is implementation defined (null pointer may be returned, or some non-null pointer may be returned that may not be used to access storage, but has to be passed to std::free) 
The following functions are required to be thread-safe: 
* The library versions of operator_new and operator_delete 
* User replacement versions of global operator_new and operator_delete 
* std::calloc, std::malloc, std::realloc <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;, std::aligned_alloc 
&nbsp;<wbr>&nbsp;<i>(since C++17)</i>, std::free 
Calls to these functions that allocate or deallocate a particular unit of storage occur in a single total order, and each such deallocation call happens-before the next allocation (if any) in this order. 

<h2>Parameters</h2>

size - number of bytes to allocate

<h2>Return value</h2>

On success, returns the pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with std::free() or std::realloc(). 
On failure, returns a null pointer. 

<h2>Notes</h2>

This function does not call constructors or initialize memory in any way. There are no ready-to-use smart pointers that could guarantee that the matching deallocation function is called. The preferred method of memory allocation in C++ is using RAII-ready functions std::make_unique, std::make_shared, container constructors, etc, and, in low-level library code, new-expression. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;

#include &lt;string&gt;
int main()

{
    // allocates enough for an array of 4 strings
    if (auto p = (std::string *)std::malloc(4 * sizeof(std::string))) {
        int i = 0;
        try {
            for (; i != 4; ++i) // populate the array
                new (p + i) std::string(5, 'a' + i);
            for (int j = 0; j != 4; ++j) // print it back out
                std::cout &lt;&lt; &quot;p[&quot; &lt;&lt; j &lt;&lt; &quot;] == &quot; &lt;&lt; p[j] &lt;&lt; '\n';
        } catch (...) {
        }
        for (; i != 0; --i) // clean up
            p[i - 1].~basic_string();
        std::free(p);
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;p[0] == aaaaa 
&nbsp;<wbr>&nbsp;p[1] == bbbbb 
&nbsp;<wbr>&nbsp;p[2] == ccccc 
&nbsp;<wbr>&nbsp;p[3] == ddddd

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions 
operator_new <i>(function)</i> 
operator_new[] 
get_temporary_buffer obtains uninitialized storage 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++17) 
(removed in C++20) 
