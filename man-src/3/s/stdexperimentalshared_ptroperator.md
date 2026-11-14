---
title: "stdexperimentalshared_ptroperator(3)"
name: "stdexperimentalshared_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshared_ptroperator/"
---

std::experimental::shared_ptr&lt;T&gt;::operator[] - std::experimental::shared_ptr&lt;T&gt;::operator[]

<h2>Synopsis</h2>

element_type&amp; operator[](std::ptrdiff_t i) const noexcept; (library fundamentals TS) 
Index into the array pointed to by the stored pointer. 
The behavior is undefined if the stored pointer is null or if i is negative. 
If T (the template parameter of shared_ptr) is an array type U[N], i shall be less than N, or the behavior is undefined. 

<h2>Parameters</h2>

i - the array index

<h2>Return value</h2>

A reference to the i-th element of the array , i.e., get()[i] 
Remarks 
When T is not an array type, it is unspecified whether this function is declared. If the function is declared, it is unspecified what its return type is, except that the declaration (although not necessarily the definition) of the function is guaranteed to be legal. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stored pointer 
get <i>(public member function)</i> 
