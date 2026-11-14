---
title: "stdsize_t(3)"
name: "stdsize_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsize_t/"
---

std::size_t - std::size_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cstddef&gt;

Defined in header &lt;cstdio&gt;

Defined in header &lt;cstdlib&gt;

Defined in header &lt;cstring&gt;

Defined in header &lt;ctime&gt;

Defined in header &lt;cwchar&gt;

typedef /*implementation-defined*/ size_t;</code></pre> 
std::size_t is the unsigned integer type of the result of the sizeof operator 
as well as the sizeof... operator and the alignof operator 
<i>(since C++11)</i>. 

<h2>Notes</h2>

std::size_t can store the maximum size of a theoretically possible object of any type (including array). 
A type whose size cannot be represented by std::size_t is ill-formed 
<i>(since C++14)</i> On many platforms (an exception is systems with segmented addressing) std::size_t can safely store the value of any non-member pointer, in which case it is synonymous with std::uintptr_t. 
std::size_t is commonly used for array indexing and loop counting. Programs that use other types, such as unsigned int, for array indexing may fail on, e.g. 64-bit systems when the index exceeds UINT_MAX or if it relies on 32-bit modular arithmetic. 
When indexing C++ containers, such as std::string, std::vector, etc, the appropriate type is the member typedef size_type provided by such containers. It is usually defined as a synonym for std::size_t. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstddef&gt;

#include &lt;iostream&gt;

#include &lt;array&gt;
int main()

{
    std::array&lt;std::size_t, 10&gt; a;
    for (std::size_t i = 0; i != a.size(); ++i)
        a[i] = i;
    for (std::size_t i = a.size() - 1; i &lt; a.size(); --i)
        std::cout &lt;&lt; a[i] &lt;&lt; &quot; &quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;9 8 7 6 5 4 3 2 1 0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;signed integer type returned when subtracting two pointers 
ptrdiff_t <i>(typedef)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;byte offset from the beginning of a standard-layout type to specified member 
offsetof <i>(function macro)</i> 
