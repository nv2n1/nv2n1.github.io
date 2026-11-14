---
title: "stdptrdiff_t(3)"
name: "stdptrdiff_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdptrdiff_t/"
---

std::ptrdiff_t - std::ptrdiff_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cstddef&gt;

typedef /*implementation-defined*/ ptrdiff_t;</code></pre> 
std::ptrdiff_t is the signed integer type of the result of subtracting two pointers. 

<h2>Notes</h2>

std::ptrdiff_t is used for pointer_arithmetic and array indexing, if negative values are possible. Programs that use other types, such as int, may fail on, e.g. 64-bit systems when the index exceeds INT_MAX or if it relies on 32-bit modular arithmetic. 
When working with the C++ container library, the proper type for the difference between iterators is the member typedef difference_type, which is often synonymous with std::ptrdiff_t. 
Only pointers to elements of the same array (including the pointer one past the end of the array) may be subtracted from each other. 
If an array is so large (greater than PTRDIFF_MAX elements, but less than SIZE_MAX bytes), that the difference between two pointers may not be representable as std::ptrdiff_t, the result of subtracting two such pointers is undefined. 
For char arrays shorter than PTRDIFF_MAX, std::ptrdiff_t acts as the signed counterpart of std::size_t: it can store the size of the array of any type and is, on most platforms, synonymous with std::intptr_t. 

<h2>Example</h2>

// Run this code #include &lt;cstddef&gt;

#include &lt;iostream&gt;

int main()

{
    const std::size_t N = 100;
    int *a = new int[N];
    int *end = a + N;
    for (std::ptrdiff_t i = N; i &gt; 0; --i)
        std::cout &lt;&lt; (*(end - i) = i) &lt;&lt; ' ';
    delete[] a;
}


<h2>See also</h2>

<pre><code>unsigned integer type returned by the sizeof operator

size_t   (typedef)
byte offset from the beginning of a standard-layout type to specified member

offsetof (function macro)




</code></pre>
