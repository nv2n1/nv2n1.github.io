---
title: "stdexperimentalswapstdexperimentalpropagate_const(3)"
name: "stdexperimentalswapstdexperimentalpropagate_const"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalswapstdexperimentalpropagate_const/"
---

std::experimental::swap(std::experimental::propagate_const) - std::experimental::swap(std::experimental::propagate_const)

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;

constexpr void swap(std::experimental::propagate_const&lt;T&gt; &amp;lhs, (library fundamentals TS v2)

                                                                    std::experimental::propagate_const&lt;T&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the swap algorithm for std::experimental::propagate_const. Swaps the pointers of lhs and rhs. Equivalent to lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - propagate_consts whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(lhs.swap(rhs)))

<h2>Complexity</h2>

Constant

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the wrapped pointer 
swap <i>(public member function)</i> 
