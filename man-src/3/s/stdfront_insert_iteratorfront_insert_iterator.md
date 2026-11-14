---
title: "stdfront_insert_iteratorfront_insert_iterator(3)"
name: "stdfront_insert_iteratorfront_insert_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfront_insert_iteratorfront_insert_iterator/"
---

std::front_insert_iterator&lt;Container&gt;::front_insert_iterator - std::front_insert_iterator&lt;Container&gt;::front_insert_iterator

<h2>Synopsis</h2>

<pre><code>constexpr front_insert_iterator() noexcept = default;     (1) (since C++20)

explicit front_insert_iterator( Container&amp; c );           (2)               (until C++20)

constexpr explicit front_insert_iterator( Container&amp; c );                   (since C++20)
</code></pre> 
1) Initializes the underlying pointer to container with nullptr. <i>(since C++20)</i> 
2) Initializes the underlying pointer to the container to std::addressof(c). 

<h2>Parameters</h2>

c - container to initialize the inserter with
