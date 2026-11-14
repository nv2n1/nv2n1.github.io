---
title: "stdexperimentalpropagate_constoperatorbool(3)"
name: "stdexperimentalpropagate_constoperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constoperatorbool/"
---

std::experimental::propagate_const&lt;T&gt;::operatorbool - std::experimental::propagate_const&lt;T&gt;::operatorbool

<h2>Synopsis</h2>

constexpr explicit operator bool() const; (library fundamentals TS v2) 
Checks whether the wrapped pointer-like object, t_, is null. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the wrapped object is not null, otherwise false. Equivalent to (bool)t_. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the object pointed to by the wrapped pointer 
get <i>(public member function)</i> 
