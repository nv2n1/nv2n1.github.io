---
title: "stdshared_futureoperator(3)"
name: "stdshared_futureoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_futureoperator/"
---

std::shared_future&lt;T&gt;::operator= - std::shared_future&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>shared_future &amp;operator=(const shared_future &amp;other);
(since C++ 11)(1)(until C++ 17)

    shared_future &amp;
    operator=(const shared_future &amp;other) noexcept;
(since C++ 17)

    shared_future &amp;
    operator=(shared_future &amp;&amp;other) noexcept;
(2)(since C++ 11)</code></pre> 
Assigns the contents of another shared_future. 
1) Releases any shared state and assigns the contents of other to *this. After the assignment, this-&gt;valid() == other.valid(). 
2) Releases any shared state and move-assigns the contents of other to *this. After the assignment, other.valid() == false and this-&gt;valid() will yield the same value as other.valid() before the assignment. 

<h2>Parameters</h2>

other - a std::shared_future that will transfer state to *this

<h2>Return value</h2>

*this 
