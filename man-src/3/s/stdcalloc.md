---
title: "stdcalloc(3)"
name: "stdcalloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcalloc/"
---

std::calloc - std::calloc

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    void *calloc(std::size_t num, std::size_t size);</code></pre> 
Allocates memory for an array of num objects of size size and initializes it to all bits zero. 
If allocation succeeds, returns a pointer to the lowest (first) byte in the allocated memory block that is suitably aligned for any object type. 
If size is zero, the behavior is implementation defined (null pointer may be returned, or some non-null pointer may be returned that may not be used to access storage) 
The following functions are required to be thread-safe: 
* The library versions of operator_new and operator_delete 
* User replacement versions of global operator_new and operator_delete 
* std::calloc, std::malloc, std::realloc <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;, std::aligned_alloc 
&nbsp;<wbr>&nbsp;<i>(since C++17)</i>, std::free 
Calls to these functions that allocate or deallocate a particular unit of storage occur in a single total order, and each such deallocation call happens-before the next allocation (if any) in this order. 

<h2>Parameters</h2>

num - number of objects 
size - size of each object

<h2>Return value</h2>

On success, returns the pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with std::free() or std::realloc(). 
On failure, returns a null pointer. 

<h2>Notes</h2>

Due to the alignment requirements, the number of allocated bytes is not necessarily equal to num*size. 
Initialization to all bits zero does not guarantee that a floating-point or a pointer would be initialized to 0.0 and the null pointer value, respectively (although that is true on all common platforms) 
Originally (in C89), support for zero size was added to accommodate code such as OBJ *p = calloc(0, sizeof(OBJ)); // &quot;zero-length&quot; placeholder

...

    while (1)
{
    p = realloc(p, c * sizeof(OBJ)); // reallocations until size settles
    ...                              // code that may change c or break out of loop
}


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdlib&gt;
int main()

{
    int *p1 = (int *)std::calloc(4, sizeof(int));    // allocate and zero out an array of 4 int
    int *p2 = (int *)std::calloc(1, sizeof(int[4])); // same, naming the array type directly
    int *p3 = (int *)std::calloc(4, sizeof *p3);     // same, without repeating the type name
    if (p2)
        for (int n = 0; n &lt; 4; ++n) // print the array
            std::cout &lt;&lt; &quot;p2[&quot; &lt;&lt; n &lt;&lt; &quot;] == &quot; &lt;&lt; p2[n] &lt;&lt; '\n';
    std::free(p1);
    std::free(p2);
    std::free(p3);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;p2[0] == 0 
&nbsp;<wbr>&nbsp;p2[1] == 0 
&nbsp;<wbr>&nbsp;p2[2] == 0 
&nbsp;<wbr>&nbsp;p2[3] == 0

<h2>See also</h2>


