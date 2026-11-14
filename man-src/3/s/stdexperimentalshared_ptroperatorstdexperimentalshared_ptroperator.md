---
title: "stdexperimentalshared_ptroperatorstdexperimentalshared_ptroperator(3)"
name: "stdexperimentalshared_ptroperatorstdexperimentalshared_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshared_ptroperatorstdexperimentalshared_ptroperator/"
description: "std::experimental::shared_ptr<T>::operator*,std::experimental::shared_ptr<T>::operator-> – std::experimental::shared_ptr<T>::operator*,std::experimental::shared_ptr<T>::operator->"
---

<p>std::experimental::shared_ptr&lt;T&gt;::operator*,std::experimental::shared_ptr&lt;T&gt;::operator-&gt; &#8211; std::experimental::shared_ptr&lt;T&gt;::operator*,std::experimental::shared_ptr&lt;T&gt;::operator-&gt;</p>
<h2>Synopsis</h2>
<p>T&amp; operator*() const noexcept; <code>(1)</code> (library fundamentals TS)<br />
T* operator-&gt;() const noexcept; <code>(2)</code> (library fundamentals TS)<br />
Dereferences the stored pointer. The behavior is undefined if the stored pointer is null. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) The result of dereferencing the stored pointer, i.e., *get()<br />
2) The stored pointer, i.e., get()<br />
Remarks<br />
When T is an array type or (possibly cv-qualified) void, it is unspecified whether function <code>(1)</code> is declared.<br />
When T is an array type, it is unspecified whether function <code>(2)</code> is declared.<br />
In either case, if the function is declared, it is unspecified what its return type is, except that the declaration (although not necessarily the definition) of the function is guaranteed to be legal. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the stored pointer<br />
get <i>(public member function)</i> </p>
