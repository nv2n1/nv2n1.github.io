---
title: "stdexperimentalrangesiterator_tstdexperimentalrangessentinel_t(3)"
name: "stdexperimentalrangesiterator_tstdexperimentalrangessentinel_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesiterator_tstdexperimentalrangessentinel_t/"
---

std::experimental::ranges::iterator_t,std::experimental::ranges::sentinel_t - std::experimental::ranges::iterator_t,std::experimental::ranges::sentinel_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/range&gt;

template&lt; class T &gt;                                             (1) (ranges TS)

using iterator_t = decltype(ranges::begin(std::declval&lt;T&amp;&gt;()));

template&lt; class T &gt;                                             (2) (ranges TS)

using sentinel_t = decltype(ranges::end(std::declval&lt;T&amp;&gt;()));</code></pre> 
Obtain the iterator and sentinel types of a range T. 
