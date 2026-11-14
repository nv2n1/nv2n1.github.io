---
title: "stdarray(3)"
name: "stdarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdarray/"
---

std::array&lt;T,N&gt;::swap - std::array&lt;T,N&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(array &amp;other) noexcept(/* see below */);
(since C++ 11)(until C++ 20)

    constexpr void swap(array &amp;other) noexcept(/* see below */);
(since C++ 20)</code></pre> 
Exchanges the contents of the container with those of other. Does not cause iterators and references to associate with the other container. 

<h2>Parameters</h2>

other - container to exchange the contents with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

noexcept specification: 
noexcept(noexcept(swap(std::declval&lt;T&amp;&gt;(), std::declval&lt;T&amp;&gt;()))) <i>(until C++17)</i> 
In the expression above, the identifier swap is looked up in the same manner as the one used by the C++17 std::is_nothrow_swappable trait. 
noexcept specification: <i>(since C++17)</i> 
noexcept(std::is_nothrow_swappable_v&lt;T&gt;) 

 
For zero-sized arrays, 
noexcept specification: 
noexcept

<h2>Complexity</h2>

Linear in size of the container. 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2456 C++11 the noexcept specification is ill-formed made to work

<h2>See also</h2>

std::swap(std::array) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
