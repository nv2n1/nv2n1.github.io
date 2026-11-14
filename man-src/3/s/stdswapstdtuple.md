---
title: "stdswapstdtuple(3)"
name: "stdswapstdtuple"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdtuple/"
---

std::swap(std::tuple) - std::swap(std::tuple)

<h2>Synopsis</h2>

<pre><code>template &lt;class... Types&gt;
(since C++ 11)

    void swap(tuple&lt;Types...&gt; &amp;lhs, tuple&lt;Types...&gt; &amp;rhs) noexcept(/* see below */);
(until C++ 20)

    template &lt;class... Types&gt;

    constexpr void(since C++ 20)

        swap(tuple&lt;Types...&gt; &amp;lhs, tuple&lt;Types...&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Swaps the contents of lhs and rhs. Equivalent to lhs.swap(rhs). 
This function does not participate in overload resolution unless std::is_swappable_v&lt;Ti&gt; is true for all i from 0 to sizeof...(Types). <i>(since C++17)</i> 

<h2>Parameters</h2>

lhs, rhs - tuples whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(lhs.swap(rhs)))

<h2>See also</h2>


