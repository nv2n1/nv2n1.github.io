---
title: "stdundeclare_no_pointers(3)"
name: "stdundeclare_no_pointers"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdundeclare_no_pointers/"
---

std::undeclare_no_pointers - std::undeclare_no_pointers

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
void undeclare_no_pointers( char *p, std::size_t n ); <i>(since C++11)</i> 
Unregisters a range earlier registered with std::declare_no_pointers(). 

<h2>Parameters</h2>

p - pointer to the beginning of the range previosly registered with std::declare_no_pointers 
n - the number of bytes in the range, same value as previously used with std::declare_no_pointers

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

None

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

declare_no_pointers declares that a memory area does not contain traceable pointers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
