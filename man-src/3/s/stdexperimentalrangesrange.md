---
title: "stdexperimentalrangesrange(3)"
name: "stdexperimentalrangesrange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesrange/"
---

std::experimental::ranges::Range - std::experimental::ranges::Range

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/range&gt;

template &lt; class T &gt;

concept bool Range =

requires(T&amp;&amp; t) {                                                        (ranges TS)

    ranges::begin(t); /* not necessarily equality-preserving (see below) */

    ranges::end(t);

};</code></pre> 
Given an lvalue t of type std::remove_reference_t&lt;T&gt;, Range&lt;T&gt; is satisfied only if 
* [ranges::begin(t), ranges::end(t)) denotes a range; and 
* both ranges::begin(t) and ranges::end(t) are amortized constant time and non-modifying. 
* If ranges::iterator_t&lt;T&gt; satisfies ForwardIterator, ranges::begin(t) is equality preserving. 
