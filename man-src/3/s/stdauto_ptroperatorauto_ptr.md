---
title: "stdauto_ptroperatorauto_ptr(3)"
name: "stdauto_ptroperatorauto_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdauto_ptroperatorauto_ptr/"
description: "std::auto_ptr<T>::operatorauto_ptr<Y> – std::auto_ptr<T>::operatorauto_ptr<Y>"
---

<p>std::auto_ptr&lt;T&gt;::operatorauto_ptr&lt;Y&gt; &#8211; std::auto_ptr&lt;T&gt;::operatorauto_ptr&lt;Y&gt;</p>
<h2>Synopsis</h2>
<p>template&lt; class Y &gt; <code>(1)</code> (deprecated in C++11)<br />
operator auto_ptr_ref&lt;Y&gt;() throw(); (removed in C++17)<br />
template&lt; class Y &gt; <code>(2)</code> (deprecated in C++11)<br />
operator auto_ptr&lt;Y&gt;() throw(); (removed in C++17)<br />
Converts *this to an auto_ptr for a different type Y.<br />
1) Returns an implementation-defined type that holds a reference to *this. std::auto_ptr is convertible and assignable from this template. The implementation is allowed to provide the template with a different name or implement equivalent functionality in other ways.<br />
2) Constructs a new auto_ptr with a pointer obtained by calling release(). </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) An implementation-defined type that holds a reference to *this<br />
2) A auto_ptr with a pointer obtained by calling release(). </p>
<h2>Notes</h2>
<p>The constructor and the copy assignment operator from auto_ptr_ref is provided to allow copy-constructing and assigning std::auto_ptr from nameless temporaries. Since its copy constructor and copy assignment operator take the argument as non-const reference, they cannot bind rvalue arguments directly. However, a user-defined conversion can be executed (which releases the original auto_ptr), followed by a call to the constructor or copy-assignment operator that take auto_ptr_ref by value. This is an early implementation of move_semantics. </p>
