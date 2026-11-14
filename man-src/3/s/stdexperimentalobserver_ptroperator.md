---
title: "stdexperimentalobserver_ptroperator(3)"
name: "stdexperimentalobserver_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalobserver_ptroperator/"
description: "std::experimental::observer_ptr<W>::operator*,std::experimental::observer_ptr<W>::operator-> – std::experimental::observer_ptr<W>::operator*,std::experimental::observer_ptr<W>::operator->"
---

<p>std::experimental::observer_ptr&lt;W&gt;::operator*,std::experimental::observer_ptr&lt;W&gt;::operator-&gt; &#8211; std::experimental::observer_ptr&lt;W&gt;::operator*,std::experimental::observer_ptr&lt;W&gt;::operator-&gt;</p>
<h2>Synopsis</h2>
<p>constexpr std::add_lvalue_reference_t&lt;element_type&gt; operator*() const; <code>(1)</code> (library fundamentals TS v2)<br />
constexpr element_type* operator-&gt;() const noexcept; <code>(2)</code> (library fundamentals TS v2)<br />
operator* and operator-&gt; provide access to the object watched by *this.<br />
The behavior of operator* is undefined if get() == nullptr. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) Returns the object watched by *this, equivalent to *get().<br />
2) Returns a pointer to the object watched by *this, i.e. get(). </p>
<h2>Exceptions</h2>
<p>1) Throws nothing.</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the watched object<br />
get <i>(public member function)</i> </p>
