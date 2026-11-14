---
title: "stdatomic_refis_always_lock_free(3)"
name: "stdatomic_refis_always_lock_free"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refis_always_lock_free/"
---

std::atomic_ref&lt;T&gt;::is_always_lock_free - std::atomic_ref&lt;T&gt;::is_always_lock_free

<h2>Synopsis</h2>

<pre><code>static constexpr bool is_always_lock_free = /*implementation-defined*/;  (since C++20)</code></pre> 
Equals true if this operations on this atomic_ref type is always lock-free and false if it is never or sometimes lock-free. 
The value of this constant is consistent with the result of member function is_lock_free. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the atomic_ref object is lock-free 
is_lock_free <i>(public member function)</i> 
