---
title: "stdfutureoperator(3)"
name: "stdfutureoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfutureoperator/"
---

std::future&lt;T&gt;::operator= - std::future&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>future &amp;operator=(future &amp;&amp;other) noexcept;
(1)(since C++ 11)

    future &amp;
    operator=(const future &amp;other) = delete;
(2)(since C++ 11)</code></pre> 
Assigns the contents of another future object. 
1) Releases any shared state and move-assigns the contents of other to *this. After the assignment, other.valid() == false and this-&gt;valid() will yield the same value as other.valid() before the assignment. 
2) std::future is not CopyAssignable. 

<h2>Parameters</h2>

other - a std::future that will transfer state to *this

<h2>Return value</h2>

*this 
