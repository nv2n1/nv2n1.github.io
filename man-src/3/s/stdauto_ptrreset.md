---
title: "stdauto_ptrreset(3)"
name: "stdauto_ptrreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdauto_ptrreset/"
---

std::auto_ptr&lt;T&gt;::reset - std::auto_ptr&lt;T&gt;::reset

<h2>Synopsis</h2>

<pre><code>void reset(T *p = 0) throw();
(deprecated in C++ 11)(removed in C++ 17)</code></pre> 
Replaces the held pointer by p. If the currently held pointer is not null pointer, delete get() is called. 

<h2>Parameters</h2>

p - a pointer to an object to manage

<h2>Return value</h2>

<i>(none)</i> 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;releases ownership of the managed object 
release <i>(public member function)</i> 
