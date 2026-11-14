---
title: "stdrealloc(3)"
name: "stdrealloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrealloc/"
---

std::realloc - std::realloc

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdlib&gt;

    void *realloc(void *ptr, std::size_t new_size);</code></pre> 
Reallocates the given area of memory. It must be previously allocated by std::malloc(), std::calloc() or std::realloc() and not yet freed with std::free(), otherwise, the results are undefined. 
The reallocation is done by either: 
a) expanding or contracting the existing area pointed to by ptr, if possible. The contents of the area remain unchanged up to the lesser of the new and old sizes. If the area is expanded, the contents of the new part of the array are undefined. 
b) allocating a new memory block of size new_size bytes, copying memory area with size equal the lesser of the new and the old sizes, and freeing the old block. 
If there is not enough memory, the old memory block is not freed and null pointer is returned. 
If ptr is a null pointer, the behavior is the same as calling std::malloc(new_size). 
If new_size is zero, the behavior is implementation defined: null pointer may be returned (in which case the old memory block may or may not be freed) or some non-null pointer may be returned that may not be used to access storage. 
The following functions are required to be thread-safe: 
* The library versions of operator_new and operator_delete 
* User replacement versions of global operator_new and operator_delete 
* std::calloc, std::malloc, std::realloc <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;, std::aligned_alloc 
&nbsp;<wbr>&nbsp;<i>(since C++17)</i>, std::free 
Calls to these functions that allocate or deallocate a particular unit of storage occur in a single total order, and each such deallocation call happens-before the next allocation (if any) in this order. 

<h2>Parameters</h2>

ptr - pointer to the memory area to be reallocated 
new_size - new size of the array

<h2>Return value</h2>

On success, returns a pointer to the beginning of newly allocated memory. To avoid a memory leak, the returned pointer must be deallocated with std::free(), the original pointer ptr is invalidated and any access to it is undefined_behavior (even if reallocation was in-place). 
On failure, returns a null pointer. The original pointer ptr remains valid and may need to be deallocated with std::free() 

<h2>Notes</h2>

Because reallocation may involve bytewise copying (regardless of whether it's to expand or to contract), only the objects of TriviallyCopyable types are safe to access in the preserved part of the memory block after a call to realloc. 
Some non-standard libraries define a type trait &quot;BitwiseMovable&quot; or &quot;Relocatable&quot;, which describes a type that doesn't have: 
* external references (e.g. nodes of a list or a tree that holds reference to another element), and 
* internal references (e.g. member pointer which might hold the address of another member). 
Objects of such type can be accessed after their storage is reallocated even if their copy constructors are not trivial. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdlib&gt;

#include &lt;new&gt;

#include &lt;cassert&gt;
class MallocDynamicBuffer

{
    char *p;

  public:
    explicit MallocDynamicBuffer(std::size_t initial = 0)
        : p(nullptr)
    {
        resize(initial);
    }
    ~MallocDynamicBuffer()
    {
        std::free(p);
    }
    void resize(std::size_t newSize)
    {
        if (newSize == 0) { // this check is not strictly needed,
            std::free(p);   // but zero-size realloc is deprecated in C
            p = nullptr;
        } else {
            if (void *mem = std::realloc(p, newSize))
                p = static_cast&lt;char *&gt;(mem);
            else
                throw std::bad_alloc();
        }
    }
    char &amp;operator[](size_t n)
    {
        return p[n];
    }
    char operator[](size_t n) const
    {
        return p[n];
    }
};
int main()

{
    MallocDynamicBuffer buf1(1024);
    buf1[5] = 'f';
    buf1.resize(10); // shrink
    assert(buf1[5] == 'f');
    buf1.resize(1024); // grow
    assert(buf1[5] == 'f');
}
</code></pre>

<h2>See also</h2>


