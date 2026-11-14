---
title: "stdswapstdarray(3)"
name: "stdswapstdarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdarray/"
---

std::swap(std::array) - std::swap(std::array)

<h2>Synopsis</h2>

<pre><code>template &lt;class T, std::size_t N&gt;
(since C++ 11)

    void swap(array&lt;T, N&gt; &amp;lhs, (until C++ 17)

                                    array&lt;T, N&gt; &amp;rhs);

template &lt;class T, std::size_t N&gt;
(since C++ 17)

    void swap(array&lt;T, N&gt; &amp;lhs, (until C++ 20)

                                    array&lt;T, N&gt; &amp;rhs) noexcept(/* see below */);

template &lt;class T, std::size_t N&gt;

constexpr void swap(array&lt;T, N&gt; &amp;lhs, (since C++ 20)

                                          array&lt;T, N&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::array. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 
This overload only participates in overload resolution if N == 0 or std::is_swappable&lt;T&gt;::value is true. <i>(since C++17)</i> 

<h2>Parameters</h2>

lhs, rhs - containers whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Linear in size of the container.

<h2>Exceptions</h2>

noexcept specification: <i>(since C++17)</i> 
noexcept(noexcept(lhs.swap(rhs)))

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
