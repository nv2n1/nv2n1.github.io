---
title: "stdshared_ptroperator(3)"
name: "stdshared_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptroperator/"
---

std::shared_ptr&lt;T&gt;::operator[] - std::shared_ptr&lt;T&gt;::operator[]

<h2>Synopsis</h2>

element_type&amp; operator[]( std::ptrdiff_t idx ) const; <i>(since C++17)</i> 
Index into the array pointed to by the stored pointer. 
The behavior is undefined if the stored pointer is null or if idx is negative. 
If T (the template parameter of shared_ptr) is an array type U[N], idx must be less than N, otherwise the behavior is undefined. 

<h2>Parameters</h2>

idx - the array index

<h2>Return value</h2>

A reference to the idx-th element of the array, i.e., get()[idx] 

<h2>Exceptions</h2>

<i>(none)</i> 

 
Remarks 

 
When T is not an array type, it is unspecified whether this function is declared. If the function is declared, it is unspecified what its return type is, except that the declaration (although not necessarily the definition) of the function is guaranteed to be legal.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stored pointer 
get <i>(public member function)</i> 
