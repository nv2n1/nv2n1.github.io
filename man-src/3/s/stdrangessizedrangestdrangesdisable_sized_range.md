---
title: "stdrangessizedrangestdrangesdisable_sized_range(3)"
name: "stdrangessizedrangestdrangesdisable_sized_range"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangessizedrangestdrangesdisable_sized_range/"
---

std::ranges::SizedRange,std::ranges::disable_sized_range - std::ranges::SizedRange,std::ranges::disable_sized_range

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ranges&gt;

template&lt; class T &gt;

concept SizedRange = Range&lt;T&gt; &amp;&amp;

! disable_sized_range&lt;std::remove_cvref_t&lt;T&gt;&gt; &amp;&amp;   (1)

requires(T&amp; t) {

    ranges::size(t);

};

template&lt;class&gt;                                    (2)

inline constexpr bool disable_sized_range = false;</code></pre> 
1) The SizedRange concept specifies the requirements of a Range type that knows its size in constant time with the size function. 
Formally, given an lvalue t of type std::remove_reference_t&lt;T&gt;, T models SizedRange only if 
* ranges::size(t) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* has non-amortized constant-time complexity, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* does not modify t, and 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* is equal to ranges::distance(t), and 
* if iterator_t&lt;T&gt; models ForwardIterator, ranges::size(t) is well-defined regardless of the evaluation of ranges::begin(t) (in other words, a single-pass sized range may support a call to size only before the first call to begin, but a forward range must support size at all times) 
2) disable_sized_range exists to allows use of range types that satisfy but do not in fact model SizedRange. 
