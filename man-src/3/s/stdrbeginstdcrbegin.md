---
title: "stdrbeginstdcrbegin(3)"
name: "stdrbeginstdcrbegin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrbeginstdcrbegin/"
---

std::rbegin,std::crbegin - std::rbegin,std::crbegin

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (since C++ 14)

        auto rbegin(C &amp;c) -&gt; decltype(c.rbegin());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto rbegin(C &amp;c) -&gt; decltype(c.rbegin());

template &lt;class C&gt;
(since C++ 14)

    auto rbegin(const C &amp;c) -&gt; decltype(c.rbegin());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto rbegin(const C &amp;c) -&gt; decltype(c.rbegin());
(1)

    template &lt;class T, size_t N&gt;
    (since C++ 14)

        reverse_iterator&lt;T *&gt; rbegin(T (&amp;array)[N]);
(1)(until C++ 17)

    template &lt;class T, size_t N&gt;
    (since C++ 17)

        constexpr reverse_iterator&lt;T *&gt; rbegin(T (&amp;array)[N]);
(2)

    template &lt;class C&gt;
    (since C++ 14)

        auto crbegin(const C &amp;c) -&gt; decltype(std::rbegin(c));
(3)(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto crbegin(const C &amp;c) -&gt; decltype(std::rbegin(c));</code></pre> 
Returns an iterator to the reverse-beginning of the given container c or array array. 
1) Returns a possibly const-qualified iterator to the reverse-beginning of the container c. 
2) Returns std::reverse_iterator&lt;T*&gt; to the reverse-beginning of the array array. 
3) Returns a const-qualified iterator to the reverse-beginning of the container c. 
&nbsp;range-rbegin-rend.svg 

<h2>Parameters</h2>

c - a container with a rbegin method 
array - an array of arbitrary type

<h2>Return value</h2>

An iterator to the reverse-beginning of c or array 

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::rbegin and std::crbegin are guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt; 
, &lt;string_view&gt; 
<i>(since C++17)</i>, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 
Overloads 
Custom overloads of rbegin may be provided for classes that do not expose a suitable rbegin() member function, yet can be iterated. The following overload is already provided by the standard library: 
rbegin(std::initializer_list) specializes std::rbegin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++14)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;
int main()

{
    std::vector&lt;int&gt; v = {3, 1, 4};
    auto vi = std::rbegin(v);
    std::cout &lt;&lt; *vi &lt;&lt; '\n';
    int a[] = {-5, 10, 15};
    auto ai = std::rbegin(a);
    std::cout &lt;&lt; *ai &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4 
&nbsp;<wbr>&nbsp;15

<h2>See also</h2>

begin 
cbegin returns an iterator to the beginning of a container or array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++14)</i> 
end 
cend returns an iterator to the end of a container or array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++14)</i> 
rend returns a reverse end iterator for a container or array 
crend <i>(function template)</i> 
<i>(C++14)</i> 
