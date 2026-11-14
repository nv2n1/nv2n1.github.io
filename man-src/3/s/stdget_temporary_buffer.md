---
title: "stdget_temporary_buffer(3)"
name: "stdget_temporary_buffer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_temporary_buffer/"
---

std::get_temporary_buffer - std::get_temporary_buffer

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T &gt; (deprecated in C++17) 
std::pair&lt; T*, std::ptrdiff_t &gt; get_temporary_buffer( std::ptrdiff_t count ); (removed in C++20) 
Allocates uninitialized contiguous storage, which should be sufficient to store up to count adjacent objects of type T. The request is non-binding and the implementation may allocate less or more than necessary to store count adjacent objects. 

<h2>Parameters</h2>

count - the desired number of objects

<h2>Return value</h2>

An std::pair holding a pointer to the beginning of the allocated storage and the number of objects that fit in the storage that was actually allocated. 
If no memory could be allocated, or allocated storage is not enough to store a single element of type T, the first element of the result is a null pointer and the second element is zero. 

<h2>Exceptions</h2>

<i>(none)</i> <i>(until C++11)</i> 
noexcept specification: <i>(since C++11)</i> 
noexcept

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;memory&gt;

#include &lt;string&gt;

#include &lt;iterator&gt;
int main()

{
    const std::string s[] = {&quot;string&quot;, &quot;1&quot;, &quot;test&quot;, &quot;...&quot;};
    const auto p = std::get_temporary_buffer&lt;std::string&gt;(4);
    // requires that p.first is passed to return_temporary_buffer
    // (beware of early exit points and exceptions)
    std::copy(s, s + p.second,
              std::raw_storage_iterator&lt;std::string *, std::string&gt;(p.first));
    // requires that each string in p is individually destroyed
    // (beware of early exit points and exceptions)
    std::copy(p.first, p.first + p.second,
              std::ostream_iterator&lt;std::string&gt;{std::cout, &quot;\n&quot;});
    std::for_each(p.first, p.first + p.second, [](std::string &amp;e) {
        e.~basic_string&lt;char&gt;();
    });
    std::return_temporary_buffer(p.first);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;string 
&nbsp;<wbr>&nbsp;1 
&nbsp;<wbr>&nbsp;test 
&nbsp;<wbr>&nbsp;...

<h2>See also</h2>

return_temporary_buffer frees uninitialized storage 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++17) 
(removed in C++20) 
