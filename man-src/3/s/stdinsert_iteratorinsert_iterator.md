---
title: "stdinsert_iteratorinsert_iterator(3)"
name: "stdinsert_iteratorinsert_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinsert_iteratorinsert_iterator/"
---

std::insert_iterator&lt;Container&gt;::insert_iterator - std::insert_iterator&lt;Container&gt;::insert_iterator

<h2>Synopsis</h2>

<pre><code>insert_iterator() = default;                                                (1) (since C++20)

insert_iterator( Container&amp; c, typename Container::iterator i );            (2)               (until C++20)

constexpr insert_iterator( Container&amp; c, ranges::iterator_t&lt;Container&gt; i );                   (since C++20)
</code></pre> 
1) Initializes the underlying pointer to container with nullptr and value-initializes the underlying iterator. <i>(since C++20)</i> 
2) Initializes the underlying pointer to the container to std::addressof(c) and the underlying iterator to i. 

<h2>Parameters</h2>

c - container to initialize the inserter with 
i - iterator to initialize the inserter with
