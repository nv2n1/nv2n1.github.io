---
title: "stdatomicis_always_lock_free(3)"
name: "stdatomicis_always_lock_free"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicis_always_lock_free/"
---

std::atomic&lt;T&gt;::is_always_lock_free - std::atomic&lt;T&gt;::is_always_lock_free

<h2>Synopsis</h2>

<pre><code>static constexpr bool is_always_lock_free = /*implementation-defined*/;  (since C++17)</code></pre> 
Equals true if this atomic type is always lock-free and false if it is never or sometimes lock-free. 
The value of this constant is consistent with both the macro ATOMIC_xxx_LOCK_FREE, where defined, with the member function is_lock_free and non-member function std::atomic_is_lock_free. 

<h2>Notes</h2>

There is no non-member function equivalent of this static member constant because non-member functions take pointers to atomic types, and therefore aren't as useful in constant_expressions. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the atomic object is lock-free 
is_lock_free <i>(public member function)</i> 
atomic_is_lock_free checks if the atomic type's operations are lock-free 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
