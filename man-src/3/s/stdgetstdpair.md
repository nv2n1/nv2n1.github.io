---
title: "stdgetstdpair(3)"
name: "stdgetstdpair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetstdpair/"
---

std::get(std::pair) - std::get(std::pair)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    template &lt;size_t I, class T1, class T2&gt;
    (since C++ 11)

        typename std::tuple_element&lt;I, std::pair&lt;T1, T2&gt;&gt;::type &amp;(1)(until C++ 14)

            get(pair&lt;T1, T2&gt; &amp;p) noexcept;

template &lt;size_t I, class T1, class T2&gt;

constexpr std::tuple_element_t&lt;I, std::pair&lt;T1, T2&gt;&gt; &amp;(1)(since C++ 14)

    get(pair&lt;T1, T2&gt; &amp;p) noexcept;

template &lt;size_t I, class T1, class T2&gt;
(since C++ 11)

    const typename std::tuple_element&lt;I, std::pair&lt;T1, T2&gt;&gt;::type &amp;(2)(until C++ 14)

        get(const pair&lt;T1, T2&gt; &amp;p) noexcept;

template &lt;size_t I, class T1, class T2&gt;

constexpr const std::tuple_element_t&lt;I, std::pair&lt;T1, T2&gt;&gt; &amp;(2)(since C++ 14)

    get(const pair&lt;T1, T2&gt; &amp;p) noexcept;

template &lt;size_t I, class T1, class T2&gt;
    (since C++ 11)

        typename std::tuple_element&lt;I, std::pair&lt;T1, T2&gt;&gt;::type
    &amp;&amp; (3)(until C++ 14)

           get(std::pair&lt;T1, T2&gt; &amp;&amp;p) noexcept;

template &lt;size_t I, class T1, class T2&gt;

    constexpr std::tuple_element_t&lt;I, std::pair&lt;T1, T2&gt;&gt; &amp;&amp; (3)(since C++ 14)

                                                                get(std::pair&lt;T1, T2&gt; &amp;&amp;p) noexcept;

template &lt;size_t I, class T1, class T2&gt;
    (1)

        constexpr const std::tuple_element_t&lt;I, std::pair&lt;T1, T2&gt;&gt; &amp;&amp;
    (4)(since C++ 17)

        get(const std::pair&lt;T1, T2&gt; &amp;&amp;p) noexcept;

template &lt;class T, class U&gt;
(2)(5)(since C++ 14)

    constexpr T &amp;get(std::pair&lt;T, U&gt; &amp;p) noexcept;

template &lt;class T, class U&gt;
(6)(since C++ 14)

    constexpr const T &amp;get(const std::pair&lt;T, U&gt; &amp;p) noexcept;
(3)

    template &lt;class T, class U&gt;
    (7)(since C++ 14)

        constexpr T &amp;&amp;get(std::pair&lt;T, U&gt; &amp;&amp;p) noexcept;

template &lt;class T, class U&gt;
(8)(since C++ 17)

    constexpr const T &amp;&amp;get(const std::pair&lt;T, U&gt; &amp;&amp;p) noexcept;

template &lt;class T, class U&gt;
(9)(since C++ 14)

    constexpr T &amp;get(std::pair&lt;U, T&gt; &amp;p) noexcept;

template &lt;class T, class U&gt;
(10)(since C++ 14)

    constexpr const T &amp;get(const std::pair&lt;U, T&gt; &amp;p) noexcept;

template &lt;class T, class U&gt;
(11)(since C++ 14)

    constexpr T &amp;&amp;get(std::pair&lt;U, T&gt; &amp;&amp;p) noexcept;

template &lt;class T, class U&gt;
(12)(since C++ 17)

    constexpr const T &amp;&amp;get(const std::pair&lt;U, T&gt; &amp;&amp;p) noexcept;</code></pre> 
Extracts an element from the pair using tuple-like interface. 
The index-based overloads (1-4) fail to compile if the index I is neither 0 nor 1. 
The type-based overloads (5-12) fail to compile if the types T and U are the same. 

<h2>Parameters</h2>

p - pair whose contents to extract

<h2>Return value</h2>

1-4) Returns a reference to p.first if I==0 and a reference to p.second if I==1. 
5-8) Returns a reference to p.first. 
9-12) Returns a reference to p.second. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;
int main()

{
    auto p = std::make_pair(1, 3.14);
    std::cout &lt;&lt; '(' &lt;&lt; std::get&lt;0&gt;(p) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;1&gt;(p) &lt;&lt; &quot;)\n&quot;;
    std::cout &lt;&lt; '(' &lt;&lt; std::get&lt;int&gt;(p) &lt;&lt; &quot;, &quot; &lt;&lt; std::get&lt;double&gt;(p) &lt;&lt; &quot;)\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(1, 3.14) 
&nbsp;<wbr>&nbsp;(1, 3.14)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tuple accesses specified element 
std::get(std::tuple) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses an element of an array 
std::get(std::array) <i>(function template)</i> 
std::get(std::variant) reads the value of the variant given the index or the type (if the type is unique), throws on error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
