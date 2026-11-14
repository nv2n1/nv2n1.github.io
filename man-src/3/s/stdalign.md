---
title: "stdalign(3)"
name: "stdalign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdalign/"
---

std::align - std::align

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;memory&gt;

    void *align(std::size_t alignment,

                std::size_t size, (since C++ 11)

                                      void *&amp;ptr,

                std::size_t &amp;space);</code></pre> 
Given a pointer ptr to a buffer of size space, returns a pointer aligned by the specified alignment for size number of bytes and decreases space argument by the number of bytes used for alignment. The first aligned address is returned. 
The function modifies the pointer only if it would be possible to fit the wanted number of bytes aligned by the given alignment into the buffer. If the buffer is too small, the function does nothing and returns nullptr. 
The behavior is undefined if alignment is not a power of two. 

<h2>Parameters</h2>

alignment - the desired alignment 
size - the size of the storage to be aligned 
ptr - pointer to contiguous storage of at least space bytes 
space - the size of the buffer in which to operate

<h2>Return value</h2>

The adjusted value of ptr, or null pointer value if the space provided is too small. 

<h2>Example</h2>

demonstrates the use of std::align to place objects of different type in memory 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;memory&gt;
template &lt;std::size_t N&gt;

struct MyAllocator

{
    char data[N];
    void *p;
    std::size_t sz;
    MyAllocator()
        : p(data), sz(N)
    {
    }
    template &lt;typename T&gt;
    T *aligned_alloc(std::size_t a = alignof(T))
    {
        if (std::align(a, sizeof(T), p, sz)) {
            T *result = reinterpret_cast&lt;T *&gt;(p);
            p = (char *)p + sizeof(T);
            sz -= sizeof(T);
            return result;
        }
        return nullptr;
    }
};
int main()

{
    MyAllocator&lt;64&gt; a;
    // allocate a char
    char *p1 = a.aligned_alloc&lt;char&gt;();
    if (p1)
        *p1 = 'a';
    std::cout &lt;&lt; &quot;allocated a char at &quot; &lt;&lt; (void *)p1 &lt;&lt; '\n';
    // allocate an int
    int *p2 = a.aligned_alloc&lt;int&gt;();
    if (p2)
        *p2 = 1;
    std::cout &lt;&lt; &quot;allocated an int at &quot; &lt;&lt; (void *)p2 &lt;&lt; '\n';
    // allocate an int, aligned at 32-byte boundary
    int *p3 = a.aligned_alloc&lt;int&gt;(32);
    if (p3)
        *p3 = 2;
    std::cout &lt;&lt; &quot;allocated an int at &quot; &lt;&lt; (void *)p3 &lt;&lt; &quot; (32 byte alignment)\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;allocated a char at 0x2ff21a08 
&nbsp;<wbr>&nbsp;allocated an int at 0x2ff21a0c 
&nbsp;<wbr>&nbsp;allocated an int at 0x2ff21a20 (32 byte alignment) 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2377 C++11 alignment required to be a fundamental or supported extended alignment value only need to be a power of two

<h2>See also</h2>

alignof_operator queries alignment requirements of a type <i>(since C++11)</i> 
alignas_specifier specifies that the storage for the variable should be aligned by specific amount <i>(C++11)</i> 
aligned_storage defines the type suitable for use as uninitialized storage for types of given size 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
