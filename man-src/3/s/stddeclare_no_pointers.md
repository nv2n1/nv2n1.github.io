---
title: "stddeclare_no_pointers(3)"
name: "stddeclare_no_pointers"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddeclare_no_pointers/"
---

std::declare_no_pointers - std::declare_no_pointers

<h2>Synopsis</h2>

Defined in header &lt;memory&gt; 
void declare_no_pointers( char *p, std::size_t n ); <i>(since C++11)</i> 
Informs the garbage collector or leak detector that the specified memory region (n bytes beginning at the byte pointed to by p) contains no traceable pointers. If any part of the region is within an allocated object, the entire region must be contained in the same object. 

<h2>Parameters</h2>

p - pointer to the beginning of the range 
n - the number of bytes in the range

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

None

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

undeclare_no_pointers cancels the effect of std::declare_no_pointers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
