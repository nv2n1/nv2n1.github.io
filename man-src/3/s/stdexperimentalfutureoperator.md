---
title: "stdexperimentalfutureoperator(3)"
name: "stdexperimentalfutureoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfutureoperator/"
---

std::experimental::future&lt;T&gt;::operator= - std::experimental::future&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>std::experimental::future&lt;T&gt; &amp;operator=(std::experimental::future&lt;T&gt; &amp;&amp;other) noexcept;
(1)

    std::experimental::future&lt;T&gt; &amp;
    operator=(const std::experimental::future&lt;T&gt; &amp;other) = delete;
(2)</code></pre> 
Assigns the contents of another future object. 
1) Releases any shared state and move-assigns the contents of other to *this. After the assignment, other.valid() == false and this-&gt;valid() will yield the same value as other.valid() before the assignment. 
2) std::experimental::future is not CopyAssignable. 

<h2>Parameters</h2>

other - a std::experimental::future that will transfer state to *this

<h2>Return value</h2>

*this 
