---
title: "stdexperimentalobserver_ptrrelease(3)"
name: "stdexperimentalobserver_ptrrelease"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalobserver_ptrrelease/"
---

std::experimental::observer_ptr&lt;W&gt;::release - std::experimental::observer_ptr&lt;W&gt;::release

<h2>Synopsis</h2>

constexpr element_type* release() noexcept; (library fundamentals TS v2) 
Stop watching the watched object, if any. get() returns nullptr after the call. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A pointer to the previously watched object, or nullptr if there was no watched object, i.e. the value which would be returned by get() before the call. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a pointer to the watched object 
get <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the watched object 
reset <i>(public member function)</i> 
