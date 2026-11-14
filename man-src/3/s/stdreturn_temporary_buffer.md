---
title: "stdreturn_temporary_buffer(3)"
name: "stdreturn_temporary_buffer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreturn_temporary_buffer/"
---

std::return_temporary_buffer - std::return_temporary_buffer

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
template&lt; class T &gt; (deprecated in C++17) 
void return_temporary_buffer( T* p ); (removed in C++20) 
Deallocates storage previously allocated with std::get_temporary_buffer. 

<h2>Parameters</h2>

p - the pointer previously returned by std::get_temporary_buffer and not invalidated by an earlier call to return_temporary_buffer

<h2>Return value</h2>

<i>(none)</i> 
Exceptions <i>(since C++17)</i> 
<i>(none)</i> 

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

get_temporary_buffer obtains uninitialized storage 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(deprecated in C++17) 
(removed in C++20) 
