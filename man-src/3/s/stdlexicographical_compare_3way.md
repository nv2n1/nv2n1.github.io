---
title: "stdlexicographical_compare_3way(3)"
name: "stdlexicographical_compare_3way"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlexicographical_compare_3way/"
---

std::lexicographical_compare_3way - std::lexicographical_compare_3way

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt1, class InputIt2, class Cmp &gt;

constexpr auto lexicographical_compare_3way( InputIt1 first1, InputIt1 last1,

InputIt2 first2, InputIt2 last2,                                                              (1) (since C++20)

Cmp comp)

-&gt; std::common_comparison_category_t&lt;decltype(comp(*first1, *first2)), std::strong_ordering&gt;;

template&lt; class InputIt1, class InputIt2 &gt;

constexpr auto lexicographical_compare_3way( InputIt1 first1, InputIt1 last1,                 (2) (since C++20)

InputIt2 first2, InputIt2 last2);</code></pre> 
Lexicographically compares two ranges [first1, last1) and [first2, last2) using three-way comparison and produces a result of the strongest applicable comparison category type. 
1) Behaves as if defined as follows: for (; first1 != last1 &amp;&amp; first2 != last2; void(++first1), void(++first2))
    if (auto cmp = comp(*first1, *first2); cmp != 0)
        return cmp;
return first1 != last1 ? std::strong_ordering::greater : first2 != last2 ? std::strong_ordering::less
                                                                         : std::strong_ordering::equal; 
2) Behaves as if defined as follows: <pre><code>return std::lexicographical_compare_3way(first1, last1, first2, last2,
                                         [](const auto &amp;t, const auto &amp;u) {
                                             return std::compare_3way(t, u);
                                         });
</code></pre>

<h2>Parameters</h2>

first1, last1 - the first range of elements to examine 
first2, last2 - the second range of elements to examine 
comp - a function object type. The behavior is undefined if its return type is not one of the five comparison category types (strong_equality, weak_equality, strong_ordering, weak_ordering, or partial_ordering)

<h2>Type requirements</h2>

- 
InputIt1, InputIt2 must meet the requirements of LegacyInputIterator.

<h2>Return value</h2>

A comparison category type as defined above. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

compare_3way compares two values using three-way comparison 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
