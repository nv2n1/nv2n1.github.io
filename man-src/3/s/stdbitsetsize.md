---
title: "stdbitsetsize(3)"
name: "stdbitsetsize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbitsetsize/"
---

std::bitset&lt;N&gt;::size - std::bitset&lt;N&gt;::size

<h2>Synopsis</h2>

std::size_t size() const; <i>(until C++11)</i> 
constexpr std::size_t size() const noexcept; <i>(since C++11)</i> 
Returns the number of bits that the bitset can hold. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

number of bits that the bitset can hold, i.e. the template parameter N 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of bits set to true 
count <i>(public member function)</i> 
