---
title: "stdweak_ptruse_count(3)"
name: "stdweak_ptruse_count"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweak_ptruse_count/"
---

std::weak_ptr&lt;T&gt;::use_count - std::weak_ptr&lt;T&gt;::use_count

<h2>Synopsis</h2>

<pre><code>long use_count() const noexcept;
(since C++ 11)</code></pre> 
Returns the number of shared_ptr instances that share ownership of the managed object, or 0 if the managed object has already been deleted, i.e. *this is empty. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The number of shared_ptr instances sharing the ownership of the managed object at the instant of the call. 

<h2>Notes</h2>

expired() may be faster than use_count(). This function is inherently racy, if the managed object is shared among threads that might be creating and destroying copies of the shared_ptr: then, the result is reliable only if it matches the number of copies uniquely owned by the calling thread, or zero; any other value may become stale before it can be used. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the referenced object was already deleted 
expired <i>(public member function)</i> 
