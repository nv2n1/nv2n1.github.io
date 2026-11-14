---
title: "stdexperimentalobserver_ptroperatorbool(3)"
name: "stdexperimentalobserver_ptroperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalobserver_ptroperatorbool/"
---

std::experimental::observer_ptr&lt;W&gt;::operatorbool - std::experimental::observer_ptr&lt;W&gt;::operatorbool

<h2>Synopsis</h2>

constexpr explicit operator bool() const noexcept; (library fundamentals TS v2) 
Checks whether *this has an associated watched object, i.e. whether get() != nullptr. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if *this has an associated watched object, false otherwise. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the watched object 
get <i>(public member function)</i> 
