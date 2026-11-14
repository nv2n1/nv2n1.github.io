---
title: "stdmemcpy(3)"
name: "stdmemcpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmemcpy/"
---

std::memcpy - std::memcpy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    void *memcpy(void *dest, const void *src, std::size_t count);</code></pre> 
Copies count bytes from the object pointed to by src to the object pointed to by dest. Both objects are reinterpreted as arrays of unsigned char. 
If the objects overlap, the behavior is undefined. 
If either dest or src is a null pointer, the behavior is undefined, even if count is zero. 
If the objects are potentially-overlapping or not TriviallyCopyable, the behavior of memcpy is not specified and may_be_undefined. 

<h2>Parameters</h2>

dest - pointer to the memory location to copy to 
src - pointer to the memory location to copy from 
count - number of bytes to copy

<h2>Return value</h2>

dest 

<h2>Notes</h2>

std::memcpy is meant to be the fastest library routine for memory-to-memory copy. It is usually more efficient than std::strcpy, which must scan the data it copies or std::memmove, which must take precautions to handle overlapping inputs. 
Several C++ compilers transform suitable memory-copying loops to std::memcpy calls. 
Where strict_aliasing prohibits examining the same memory as values of two different types, std::memcpy may be used to convert the values. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdint&gt;

#include &lt;cstring&gt;
int main()

{
    // simple usage
    char source[] = &quot;once upon a midnight dreary...&quot;, dest[4];
    std::memcpy(dest, source, sizeof dest);
    for (char c : dest)
        std::cout &lt;&lt; c &lt;&lt; '\n';
    // reinterpreting
    double d = 0.1;

    //  std::int64_t n = *reinterpret_cast&lt;std::int64_t*&gt;(&amp;d); // aliasing violation
    std::int64_t n;
    std::memcpy(&amp;n, &amp;d, sizeof d); // OK
    std::cout &lt;&lt; std::hexfloat &lt;&lt; d &lt;&lt; &quot; is &quot; &lt;&lt; std::hex &lt;&lt; n
              &lt;&lt; &quot; as an std::int64_t\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;o 
&nbsp;<wbr>&nbsp;n 
&nbsp;<wbr>&nbsp;c 
&nbsp;<wbr>&nbsp;e 
&nbsp;<wbr>&nbsp;0x1.999999999999ap-4 is 3fb999999999999a as an std::int64_t

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves one buffer to another 
memmove <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fills a buffer with a character 
memset <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a certain amount of wide characters between two non-overlapping arrays 
wmemcpy <i>(function)</i> 
copy 
copy_if copies a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements in backwards order 
copy_backward <i>(function template)</i> 
is_trivially_copyable checks if a type is trivially copyable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
