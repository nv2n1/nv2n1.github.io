---
title: "stdexperimentalpropagate_constget(3)"
name: "stdexperimentalpropagate_constget"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constget/"
---

std::experimental::propagate_const&lt;T&gt;::get - std::experimental::propagate_const&lt;T&gt;::get

<h2>Synopsis</h2>

constexpr element_type* get(); (library fundamentals TS v2) 
constexpr const element_type* get() const; (library fundamentals TS v2) 
Returns a pointer to the object pointed to by the wrapped pointer-like object, t_. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

If T is an object pointer type, then t_. Otherwise, t_.get(). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
