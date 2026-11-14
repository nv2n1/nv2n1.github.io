---
title: "stdundeclare_reachable(3)"
name: "stdundeclare_reachable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdundeclare_reachable/"
---

std::undeclare_reachable - std::undeclare_reachable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;memory&gt;

template&lt; class T &gt;              (since C++11)

T* undeclare_reachable( T* p );</code></pre> 
Removes the reachable status of the object, referenced by the pointer p, if it was previously set by std::declare_reachable. If the object was declared reachable multiple times, equal number of calls to undeclare_reachable would be needed to remove this status. Once the object is not declared reachable and has no pointers referencing it, it may be reclaimed by garbage collector or reported as a leak by a leak detector. 

<h2>Parameters</h2>

p - a pointer to an object previously declared reachable and not destructed since then

<h2>Return value</h2>

A safely-derived copy of p. 

<h2>Exceptions</h2>

None

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

declare_reachable declares that an object can not be recycled 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
