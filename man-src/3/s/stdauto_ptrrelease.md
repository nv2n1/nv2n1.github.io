---
title: "stdauto_ptrrelease(3)"
name: "stdauto_ptrrelease"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdauto_ptrrelease/"
---

std::auto_ptr&lt;T&gt;::release - std::auto_ptr&lt;T&gt;::release

<h2>Synopsis</h2>

T* release() throw(); (deprecated in C++11) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++17) 
Releases the held pointer. After the call *this holds the null pointer. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

get(). 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the managed object 
reset <i>(public member function)</i> 
