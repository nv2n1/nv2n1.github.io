---
title: "stdexperimentalatomic_weak_ptroperatorweak_ptr(3)"
name: "stdexperimentalatomic_weak_ptroperatorweak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_weak_ptroperatorweak_ptr/"
---

std::experimental::atomic_weak_ptr&lt;T&gt;::operatorweak_ptr&lt;T&gt; - std::experimental::atomic_weak_ptr&lt;T&gt;::operatorweak_ptr&lt;T&gt;

<h2>Synopsis</h2>

<pre><code>operator weak_ptr&lt;T&gt;() const noexcept;</code></pre> 
Atomically loads and returns the current value of the atomic_weak_ptr. Equivalent to load(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The current value of the atomic_weak_ptr. 
Remarks 
All associated use_count increments are guaranteed to be performed as part of the atomic operation. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically obtains the value of the atomic object 
load <i>(public member function)</i> 
