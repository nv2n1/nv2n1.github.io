---
title: "stdswapstdpriority_queue(3)"
name: "stdswapstdpriority_queue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdpriority_queue/"
---

std::swap(std::priority_queue) - std::swap(std::priority_queue)

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class Container, class Compare&gt;

void swap(priority_queue&lt;T, Container, Compare&gt; &amp;lhs, (until C++ 17)

                                                          priority_queue&lt;T, Container, Compare&gt; &amp;rhs);

template &lt;class T, class Container, class Compare&gt;

void swap(priority_queue&lt;T, Container, Compare&gt; &amp;lhs, (since C++ 17)

                                                          priority_queue&lt;T, Container, Compare&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::priority_queue. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 
This overload only participates in overload resolution if std::is_swappable&lt;Container&gt;::value and std::is_swappable&lt;Compare&gt;::value are both true. <i>(since C++17)</i> 

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
