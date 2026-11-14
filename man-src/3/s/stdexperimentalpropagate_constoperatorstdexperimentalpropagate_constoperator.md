---
title: "stdexperimentalpropagate_constoperatorstdexperimentalpropagate_constoperator(3)"
name: "stdexperimentalpropagate_constoperatorstdexperimentalpropagate_constoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalpropagate_constoperatorstdexperimentalpropagate_constoperator/"
description: "std::experimental::propagate_const<T>::operator*,std::experimental::propagate_const<T>::operator-> – std::experimental::propagate_const<T>::operator*,std::experimental::propagate_const<T>::operator->"
---

<p>std::experimental::propagate_const&lt;T&gt;::operator*,std::experimental::propagate_const&lt;T&gt;::operator-&gt; &#8211; std::experimental::propagate_const&lt;T&gt;::operator*,std::experimental::propagate_const&lt;T&gt;::operator-&gt;</p>
<h2>Synopsis</h2>
<p>constexpr element_type&amp; operator*(); <code>(1)</code> (library fundamentals TS v2)<br />
constexpr const element_type&amp; operator*() const; <code>(2)</code> (library fundamentals TS v2)<br />
constexpr element_type* operator-&gt;(); <code>(3)</code> (library fundamentals TS v2)<br />
constexpr const element_type* operator-&gt;() const; <code>(4)</code> (library fundamentals TS v2)<br />
Provides access to the object pointed to by the pointer-like object *this wraps.<br />
The behavior of these functions is undefined if get() == nullptr. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1-2) The object pointed to by the wrapped pointer-like object, i.e., *get()<br />
3-4) A pointer to the object pointed to by the wrapped pointer-like object, i.e., get() </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the object pointed to by the wrapped pointer<br />
get <i>(public member function)</i> </p>
