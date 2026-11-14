---
title: "stdauto_ptroperatorstdauto_ptroperator(3)"
name: "stdauto_ptroperatorstdauto_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdauto_ptroperatorstdauto_ptroperator/"
description: "std::auto_ptr<T>::operator*,std::auto_ptr<T>::operator-> – std::auto_ptr<T>::operator*,std::auto_ptr<T>::operator->"
---

<p>std::auto_ptr&lt;T&gt;::operator*,std::auto_ptr&lt;T&gt;::operator-&gt; &#8211; std::auto_ptr&lt;T&gt;::operator*,std::auto_ptr&lt;T&gt;::operator-&gt;</p>
<h2>Synopsis</h2>
<p>T&amp; operator*() const throw(); <code>(1)</code> (deprecated in C++11)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++17)<br />
T* operator-&gt;() const throw(); <code>(2)</code> (deprecated in C++11)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++17)<br />
Dereferences a pointer to the managed object. The first version requires get() != 0. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) *get().<br />
2) get(). </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the managed object<br />
get <i>(public member function)</i> </p>
