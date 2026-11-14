---
title: "stdfree(3)"
name: "stdfree"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfree/"
---

std::free - std::free

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    void free(void *ptr);</code></pre> 
Deallocates the space previously allocated by std::malloc, std::calloc 
, std::aligned_alloc 
<i>(since C++17)</i>, or std::realloc. 
If ptr is a null pointer, the function does nothing. 
The behavior is undefined if the value of ptr does not equal a value returned earlier by std::malloc, std::calloc 
, std::aligned_alloc 
<i>(since C++17)</i>, or std::realloc. 
The behavior is undefined if the memory area referred to by ptr has already been deallocated, that is, std::free or std::realloc has already been called with ptr as the argument and no calls to std::malloc, std::calloc 
, std::aligned_alloc 
<i>(since C++17)</i>, or std::realloc resulted in a pointer equal to ptr afterwards. 
The behavior is undefined if after std::free returns, an access is made through the pointer ptr (unless another allocation function happened to result in a pointer value equal to ptr) 
The following functions are required to be thread-safe: 
* The library versions of operator_new and operator_delete 
* User replacement versions of global operator_new and operator_delete 
* std::calloc, std::malloc, std::realloc <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;, std::aligned_alloc 
&nbsp;<wbr>&nbsp;<i>(since C++17)</i>, std::free 
Calls to these functions that allocate or deallocate a particular unit of storage occur in a single total order, and each such deallocation call happens-before the next allocation (if any) in this order. 

<h2>Parameters</h2>

ptr - pointer to the memory to deallocate

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

The function accepts (and does nothing with) the null pointer to reduce the amount of special-casing. Whether allocation succeeds or not, the pointer returned by an allocation function can be passed to std::free. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdlib&gt;
int main()

{
    int *p1 = (int *)std::malloc(10 * sizeof *p1);
    std::free(p1); // every allocated pointer must be freed
    int *p2 = (int *)std::calloc(10, sizeof *p2);
    int *p3 = (int *)std::realloc(p2, 1000 * sizeof *p3);
    if (p3) // p3 not null means p2 was freed by std::realloc
        std::free(p3);
    else // p3 null means p2 was not freed
        std::free(p2);
}
</code></pre>

<h2>See also</h2>


