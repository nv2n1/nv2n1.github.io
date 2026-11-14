---
title: "stdreference_wrapperoperator(3)"
name: "stdreference_wrapperoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreference_wrapperoperator/"
---

std::reference_wrapper&lt;T&gt;::operator= - std::reference_wrapper&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>reference_wrapper &amp;operator=(const reference_wrapper&lt;T&gt; &amp;other) noexcept;
(since C++ 11)</code></pre> 
Copy assignment operator. Drops the current reference and stores a reference to other.get(). 

<h2>Parameters</h2>

other - reference wrapper to copy

<h2>Return values</h2>

*this
