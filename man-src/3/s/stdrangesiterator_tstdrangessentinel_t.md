---
title: "stdrangesiterator_tstdrangessentinel_t(3)"
name: "stdrangesiterator_tstdrangessentinel_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesiterator_tstdrangessentinel_t/"
---

std::ranges::iterator_t,std::ranges::sentinel_t - std::ranges::iterator_t,std::ranges::sentinel_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template &lt;class T&gt;                                         (1) (since C++20)

using iterator_t = decltype(ranges::begin(declval&lt;T&amp;&gt;()));

template &lt;class T&gt;                                         (2) (since C++20)

using sentinel_t = decltype(ranges::end(declval&lt;T&amp;&gt;()));</code></pre> 
1) Used to obtain the iterator type of the type T. 
2) Used to obtain the sentinel type of the type T. 
