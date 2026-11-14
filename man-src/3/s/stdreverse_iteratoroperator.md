---
title: "stdreverse_iteratoroperator(3)"
name: "stdreverse_iteratoroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreverse_iteratoroperator/"
---

std::reverse_iterator&lt;Iter&gt;::operator[] - std::reverse_iterator&lt;Iter&gt;::operator[]

<h2>Synopsis</h2>

/*unspecified*/ operator[]( difference_type n ) const; <i>(until C++17)</i> 
constexpr /*unspecified*/ operator[]( difference_type n ) const; <i>(since C++17)</i> 
Returns a reference to the element at specified relative location. 

<h2>Parameters</h2>

n - position relative to current location.

<h2>Return value</h2>

A reference to the element at relative location, that is, base()[-n-1]. 

<h2>Examples</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the pointed-to element 
operator* <i>(public member function)</i> 
operator-&gt; 
