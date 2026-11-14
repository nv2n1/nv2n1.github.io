---
title: "stdinitializer_listsize(3)"
name: "stdinitializer_listsize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinitializer_listsize/"
---

std::initializer_list&lt;T&gt;::size - std::initializer_list&lt;T&gt;::size

<h2>Synopsis</h2>

size_type size() const noexcept; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++14)</i> 
constexpr size_type size() const noexcept; <i>(since C++14)</i> 
Returns the number of elements in the initializer list, i.e. std::distance(begin(), end()). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

the number of elements in the initializer list 

<h2>Complexity</h2>

Constant
