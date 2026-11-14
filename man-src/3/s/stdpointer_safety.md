---
title: "stdpointer_safety(3)"
name: "stdpointer_safety"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpointer_safety/"
---

std::pointer_safety - std::pointer_safety

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;memory&gt;

enum class pointer_safety {

    relaxed,

    preferred,                   (since C++11)

    strict

};</code></pre> 
The scoped enumeration type pointer_safety lists the pointer safety modes supported by C++ 
Enumeration constants 
pointer_safety::strict Only safely-derived pointers (pointers to objects allocated with new or subobjects thereof) may be dereferenced or deallocated. Garbage collector may be active. 
pointer_safety::preferred All pointers are considered valid and may be dereferenced or deallocated. A reachability-based leak detector may be active 
pointer_safety::relaxed All pointers are considered valid and may be dereferenced or deallocated 

<h2>See also</h2>

get_pointer_safety returns the current pointer safety model 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
