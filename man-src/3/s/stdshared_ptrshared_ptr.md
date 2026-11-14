---
title: "stdshared_ptrshared_ptr(3)"
name: "stdshared_ptrshared_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_ptrshared_ptr/"
---

std::shared_ptr&lt;T&gt;::~shared_ptr - std::shared_ptr&lt;T&gt;::~shared_ptr

<h2>Synopsis</h2>

<pre><code>~shared_ptr();</code></pre> 
If *this owns an object and it is the last shared_ptr owning it, the object is destroyed through the owned deleter. 
After the destruction, the smart pointers that shared ownership with *this, if any, will report a use_count() that is one less than its previous value. 

<h2>Notes</h2>

Unlike std::unique_ptr, the deleter of std::shared_ptr is invoked even if the managed pointer is null. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a weak_ptr 
destructor <i>(public member function of std::weak_ptr&lt;T&gt;)</i> 
