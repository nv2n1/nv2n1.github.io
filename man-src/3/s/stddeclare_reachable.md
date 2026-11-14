---
title: "stddeclare_reachable(3)"
name: "stddeclare_reachable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddeclare_reachable/"
---

std::declare_reachable - std::declare_reachable

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
void declare_reachable( void* p ); <i>(since C++11)</i> 
Declares the object referenced by the pointer p reachable. Reachable objects will not be deleted by the garbage collector or considered to be a leak by a leak detector even if all pointers to it are destroyed. An object may be declared reachable multiple times, in which case multiple calls to std::undeclare_reachable would be needed to remove this property. For example, a XOR_linked_list needs to declare its nodes reachable if the implementation has garbage collection enabled. 

<h2>Parameters</h2>

p - a safely-derived pointer or a null pointer

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

May throw std::bad_alloc if the system cannot allocate memory required to track reachable objects.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

undeclare_reachable declares that an object can be recycled 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
