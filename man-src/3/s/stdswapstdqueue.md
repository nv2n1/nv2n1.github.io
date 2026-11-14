---
title: "stdswapstdqueue(3)"
name: "stdswapstdqueue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdqueue/"
---

std::swap(std::queue) - std::swap(std::queue)

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class Container&gt;

void swap(queue&lt;T, Container&gt; &amp;lhs, (until C++ 17)

                                        queue&lt;T, Container&gt; &amp;rhs);

template &lt;class T, class Container&gt;

void swap(queue&lt;T, Container&gt; &amp;lhs, (since C++ 17)

                                        queue&lt;T, Container&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::queue. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 
This overload only participates in overload resolution if std::is_swappable&lt;Container&gt;::value is true. <i>(since C++17)</i> 

<h2>Parameters</h2>

lhs, rhs - containers whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Same as swapping the underlying container.

<h2>Exceptions</h2>

noexcept specification: <i>(since C++17)</i> 
noexcept(noexcept(lhs.swap(rhs)))

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
