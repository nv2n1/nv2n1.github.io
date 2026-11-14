---
title: "stdauto_ptroperator(3)"
name: "stdauto_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdauto_ptroperator/"
---

std::auto_ptr&lt;T&gt;::operator= - std::auto_ptr&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>auto_ptr&amp; operator=( auto_ptr&amp; r ) throw();    (1) (deprecated in C++11)
(removed in C++17)

template&lt; class Y &gt;                            (2) (deprecated in C++11)

auto_ptr&amp; operator=( auto_ptr&lt;Y&gt;&amp; r ) throw();     (removed in C++17)

auto_ptr&amp; operator=( auto_ptr_ref m ) throw(); (3) (deprecated in C++11)
(removed in C++17)</code></pre> 
Replaces the managed object with the one managed by r. 
1) Effectively calls reset(r.release()). 
2) Effectively calls reset(r.release()). Y* must be implicitly convertible to T*. 
3) Effectively calls reset(m.release()). auto_ptr_ref is an implementation-defined type that holds a reference to auto_ptr. std::auto_ptr is implicitly convertible_to and from this type. The implementation is allowed to provide the template with a different name or implement equivalent functionality in other ways. 

<h2>Parameters</h2>

r - another auto_ptr to transfer the ownership of the object from 
m - an implementation-defined type that holds a reference to auto_ptr

<h2>Return value</h2>

*this. 

<h2>Notes</h2>

The constructor and the copy assignment operator from auto_ptr_ref is provided to allow copy-constructing and assigning std::auto_ptr from nameless temporaries. Since its copy constructor and copy assignment operator take the argument as non-const reference, they cannot bind rvalue arguments directly. However, a user-defined_conversion can be executed (which releases the original auto_ptr), followed by a call to the constructor or copy-assignment operator that take auto_ptr_ref by value. This is an early implementation of move_semantics. 
