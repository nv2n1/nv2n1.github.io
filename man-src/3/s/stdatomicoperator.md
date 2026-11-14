---
title: "stdatomicoperator(3)"
name: "stdatomicoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicoperator/"
---

std::atomic&lt;T&gt;::operator= - std::atomic&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>T operator=(T desired) noexcept;

T operator=(T desired) volatile noexcept;
(1)(since C++ 11)(1)(since C++ 11)

    atomic &amp;
    operator=(const atomic &amp;) = delete;
(2)(since C++ 11)

    atomic &amp;
    operator=(const atomic &amp;) volatile = delete;</code></pre> 
1) Atomically assigns a value desired to the atomic variable. Equivalent to store(desired). 
2) Atomic variables are not CopyAssignable. 

<h2>Parameters</h2>

desired - value to assign

<h2>Return value</h2>

desired. 

<h2>Notes</h2>

Unlike most assignment operators, the assignment operators for atomic types do not return a reference to their left-hand arguments. They return a copy of the stored value instead. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic object 
constructor <i>(public member function)</i> 
