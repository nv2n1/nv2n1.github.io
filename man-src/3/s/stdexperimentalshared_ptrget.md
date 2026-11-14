---
title: "stdexperimentalshared_ptrget(3)"
name: "stdexperimentalshared_ptrget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshared_ptrget/"
---

std::experimental::shared_ptr&lt;T&gt;::get - std::experimental::shared_ptr&lt;T&gt;::get

<h2>Synopsis</h2>

element_type* get() const noexcept; (library fundamentals TS) 
Returns the stored pointer. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The stored pointer. 

<h2>Notes</h2>

A shared_ptr may share ownership of an object while storing a pointer to another object. get() returns the stored pointer, not the managed pointer. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dereferences the stored pointer 
operator* <i>(public member function)</i> 
operator-&gt; 
