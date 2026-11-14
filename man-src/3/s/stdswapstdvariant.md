---
title: "stdswapstdvariant(3)"
name: "stdswapstdvariant"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdvariant/"
---

std::swap(std::variant) - std::swap(std::variant)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;variant&gt;

    template &lt;class... Types&gt;
    (since C++ 17)

        void swap(variant&lt;Types...&gt; &amp;lhs, variant&lt;Types...&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Overloads the std::swap algorithm for std::variant. Effectively calls lhs.swap(rhs). 
This overload only participates in overload resolution if is_move_constructible_v&lt;T_i&gt; and is_swappable_v&lt;T_i&gt; are both true for all T_i in Types... 

<h2>Parameters</h2>

lhs, rhs - variant objects whose values to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(lhs.swap(rhs)))

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps with another variant 
swap <i>(public member function)</i> 
