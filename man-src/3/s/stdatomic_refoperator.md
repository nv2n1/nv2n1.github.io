---
title: "stdatomic_refoperator(3)"
name: "stdatomic_refoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refoperator/"
---

std::atomic_ref&lt;T&gt;::operator= - std::atomic_ref&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>T operator=(T desired) const noexcept;
(1)

    atomic_ref &amp;
    operator=(const atomic_ref &amp;) = delete;
(2)</code></pre> 
1) Atomically assigns a value desired to the referenced object. Equivalent to store(desired). 
2) atomic_ref is not CopyAssignable. 

<h2>Parameters</h2>

desired - value to assign

<h2>Return value</h2>

desired. 

<h2>Notes</h2>

Unlike most assignment operators, the assignment operator for atomic_ref does not return a reference to its left-hand argument. It returns a copy of the stored value instead. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic_ref object 
constructor <i>(public member function)</i> 
