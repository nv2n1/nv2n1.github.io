---
title: "stdexperimentalshared_futureoperator(3)"
name: "stdexperimentalshared_futureoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalshared_futureoperator/"
---

std::experimental::shared_future&lt;T&gt;::operator= - std::experimental::shared_future&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>std::experimental::shared_future&lt;T&gt; &amp;operator=(const std::experimental::shared_future&lt;T&gt; &amp;other);
(1)

    std::experimental::shared_future&lt;T&gt; &amp;
    operator=(std::experimental::shared_future&lt;T&gt; &amp;&amp;other) noexcept;
(2)</code></pre> 
Assigns the contents of another std::experimental::shared_future object. 
1) Releases any shared state and assigns the contents of other to *this. After the assignment, this-&gt;valid() == other.valid(). 
2) Releases any shared state and move-assigns the contents of other to *this. After the assignment, other.valid() == false and this-&gt;valid() will yield the same value as other.valid() before the assignment. 

<h2>Parameters</h2>

other - a std::experimental::shared_future object to assign from

<h2>Return value</h2>

*this 
