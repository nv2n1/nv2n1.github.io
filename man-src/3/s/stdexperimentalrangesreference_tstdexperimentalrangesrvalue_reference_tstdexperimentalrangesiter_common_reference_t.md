---
title: "stdexperimentalrangesreference_tstdexperimentalrangesrvalue_reference_tstdexperimentalrangesiter_common_reference_t(3)"
name: "stdexperimentalrangesreference_tstdexperimentalrangesrvalue_reference_tstdexperimentalrangesiter_common_reference_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesreference_tstdexperimentalrangesrvalue_reference_tstdexperimentalrangesiter_common_reference_t/"
---

std::experimental::ranges::reference_t,std::experimental::ranges::rvalue_reference_t,std::experimental::ranges::iter_common_reference_t - std::experimental::ranges::reference_t,std::experimental::ranges::rvalue_reference_t,std::experimental::ranges::iter_common_reference_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class T&gt;

concept bool /*dereferenceable*/ = requires(T&amp; t) { {*t} -&gt; auto&amp;&amp;; }; // exposition only

template&lt; /*dereferenceable*/ T &gt;                                                         (1) (ranges TS)

using reference_t = decltype(*declval&lt;T&amp;&gt;());

template&lt; /*dereferenceable*/ T &gt;

requires requires(T&amp; t) { { ranges::iter_move(t) } -&gt; auto&amp;&amp;; }                           (2) (ranges TS)

using rvalue_reference_t = decltype(ranges::iter_move(declval&lt;T&amp;&gt;()));

template&lt; Readable T &gt;

using iter_common_reference_t = ranges::common_reference_t&lt;ranges::reference_t&lt;T&gt;,        (3) (ranges TS)

ranges::value_type_t&lt;T&gt;&amp;&gt;;</code></pre> 
1) Obtain the reference type of a dereferenceable type T. 
2) Obtain the rvalue reference type of a dereferenceable type T, that is, the return type of ranges::iter_move. 
3) Compute a Readable type's common reference type. This is the common reference type of its reference type and an lvalue reference to its value type. 

<h2>Notes</h2>

The -&gt; auto&amp;&amp; constraint checks that the type of the expression is not void. 
