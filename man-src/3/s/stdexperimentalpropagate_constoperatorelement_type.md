---
title: "stdexperimentalpropagate_constoperatorelement_type(3)"
name: "stdexperimentalpropagate_constoperatorelement_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constoperatorelement_type/"
description: "std::experimental::propagate_const<T>::operatorelement_type*,std::experimental::propagate_const<T>::operatorconstelement_type* – std::experimental::propagate_const<T>::operatorelement_type*,std::ex..."
---

<p>std::experimental::propagate_const&lt;T&gt;::operatorelement_type*,std::experimental::propagate_const&lt;T&gt;::operatorconstelement_type* &#8211; std::experimental::propagate_const&lt;T&gt;::operatorelement_type*,std::experimental::propagate_const&lt;T&gt;::operatorconstelement_type*</p>
<h2>Synopsis</h2>
<p>constexpr operator element_type*(); <code>(1)</code> (library fundamentals TS v2)<br />
constexpr operator const element_type*() const; <code>(2)</code> (library fundamentals TS v2)<br />
Provides implicit conversions to element_type* and const element_type*.<br />
1) This function does not participate in overload resolution unless T is an object pointer type or is implicitly convertible to element_type*.<br />
2) This function does not participate in overload resolution unless T is an object pointer type or is implicitly convertible to const element_type*. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>A pointer to the object pointed to by the wrapped pointer-like object, i.e., this-&gt;get() </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the object pointed to by the wrapped pointer<br />
get <i>(public member function)</i> </p>
