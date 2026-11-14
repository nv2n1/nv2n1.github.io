---
title: "stdswapstdpair(3)"
name: "stdswapstdpair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdpair/"
---

std::swap(std::pair) - std::swap(std::pair)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;utility&gt;

    template &lt;class T1, class T2&gt;
    (since C++ 11)

        void swap(pair&lt;T1, T2&gt; &amp;x, pair&lt;T1, T2&gt; &amp;y) noexcept(/* see below */);
(until C++ 20)

    template &lt;class T1, class T2&gt;
    (since C++ 20)

        constexpr void swap(pair&lt;T1, T2&gt; &amp;x, pair&lt;T1, T2&gt; &amp;y) noexcept(/* see below */);</code></pre> 
Swaps the contents of x and y. Equivalent to x.swap(y). 
This function does not participate in overload resolution unless std::is_swappable_v&lt;first_type&gt; &amp;&amp; std::is_swappable_v&lt;second_type&gt; is true. <i>(since C++17)</i> 

<h2>Parameters</h2>

x, y - pairs whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(x.swap(y)))

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
