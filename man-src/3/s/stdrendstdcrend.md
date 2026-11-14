---
title: "stdrendstdcrend(3)"
name: "stdrendstdcrend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrendstdcrend/"
---

std::rend,std::crend - std::rend,std::crend

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class C&gt;
    (since C++ 14)

        auto rend(C &amp;c) -&gt; decltype(c.rend());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto rend(C &amp;c) -&gt; decltype(c.rend());

template &lt;class C&gt;
(since C++ 14)

    auto rend(const C &amp;c) -&gt; decltype(c.rend());
(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto rend(const C &amp;c) -&gt; decltype(c.rend());
(1)

    template &lt;class T, size_t N&gt;
    (since C++ 14)

        reverse_iterator&lt;T *&gt; rend(T (&amp;array)[N]);
(1)(until C++ 17)

    template &lt;class T, size_t N&gt;
    (since C++ 17)

        constexpr reverse_iterator&lt;T *&gt; rend(T (&amp;array)[N]);
(2)

    template &lt;class C&gt;
    (since C++ 14)

        auto crend(const C &amp;c) -&gt; decltype(std::rend(c));
(3)(until C++ 17)

    template &lt;class C&gt;
    (since C++ 17)

        constexpr auto crend(const C &amp;c) -&gt; decltype(std::rend(c));</code></pre> 
Returns an iterator to the reverse-end of the given container c or array array. 
1) Returns a possibly const-qualified iterator to the reverse-end of the container c. 
2) Returns std::reverse_iterator&lt;T*&gt; to the reverse-end of the array array. 
3) Returns a const-qualified iterator to the reverse-end of the container c. 
&nbsp;range-rbegin-rend.svg 

<h2>Parameters</h2>

c - a container with a rend method 
array - an array of arbitrary type

<h2>Return value</h2>

An iterator to the reverse-end of c or array 

<h2>Notes</h2>

In addition to being included in &lt;iterator&gt;, std::rend and std::crend are guaranteed to become available if any of the following headers are included: &lt;array&gt;, &lt;deque&gt;, &lt;forward_list&gt;, &lt;list&gt;, &lt;map&gt;, &lt;regex&gt;, &lt;set&gt; 
, &lt;span&gt; 
<i>(since C++20)</i>, &lt;string&gt; 
, &lt;string_view&gt; 
<i>(since C++17)</i>, &lt;unordered_map&gt;, &lt;unordered_set&gt;, and &lt;vector&gt;. 
Overloads 
Custom overloads of rend may be provided for classes that do not expose a suitable rend() member function, yet can be iterated. The following overload is already provided by the standard library: 
rend(std::initializer_list) specializes std::rend 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++14)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;
int main()

{
    int a[] = {4, 6, -3, 9, 10};
    std::cout &lt;&lt; &quot;Array backwards: &quot;;
    std::copy(std::rbegin(a), std::rend(a), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; &quot;\nVector backwards: &quot;;
    std::vector&lt;int&gt; v = {4, 6, -3, 9, 10};
    std::copy(std::rbegin(v), std::rend(v), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Array backwards: 10 9 -3 6 4 
&nbsp;<wbr>&nbsp;Vector backwards: 10 9 -3 6 4

<h2>See also</h2>

end 
cend returns an iterator to the end of a container or array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++14)</i> 
rbegin returns a reverse iterator to a container or array 
crbegin <i>(function template)</i> 
<i>(C++14)</i> 
begin 
cbegin returns an iterator to the beginning of a container or array 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++14)</i> 
