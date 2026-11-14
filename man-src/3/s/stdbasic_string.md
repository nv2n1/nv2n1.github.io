---
title: "stdbasic_string(3)"
name: "stdbasic_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_string/"
---

std::basic_string&lt;CharT,Traits,Allocator&gt;::swap - std::basic_string&lt;CharT,Traits,Allocator&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(basic_string &amp;other);
(until C++ 17)

    void swap(basic_string &amp;other) noexcept(/* see below */);
(since C++ 17)</code></pre> 
Exchanges the contents of the string with those of other. All iterators and references may be invalidated. 
The behavior is undefined if Allocator does not propagate on swap and the allocators of *this and other are unequal. <i>(since C++11)</i> 

<h2>Parameters</h2>

other - string to exchange the contents with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++17)</i> 
noexcept specification: 
noexcept(std::allocator_traits&lt;Allocator&gt;::propagate_on_container_swap::value 
|| std::allocator_traits&lt;Allocator&gt;::is_always_equal::value)

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;
int main()

{
    std::string a = &quot;AAA&quot;;
    std::string b = &quot;BBB&quot;;
    std::cout &lt;&lt; &quot;before swap&quot; &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;a: &quot; &lt;&lt; a &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;b: &quot; &lt;&lt; b &lt;&lt; '\n';
    a.swap(b);
    std::cout &lt;&lt; &quot;after swap&quot; &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;a: &quot; &lt;&lt; a &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;b: &quot; &lt;&lt; b &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;before swap 
&nbsp;<wbr>&nbsp;a: AAA 
&nbsp;<wbr>&nbsp;b: BBB 
&nbsp;<wbr>&nbsp;after swap 
&nbsp;<wbr>&nbsp;a: BBB 
&nbsp;<wbr>&nbsp;b: AAA

<h2>Complexity</h2>

Constant.
