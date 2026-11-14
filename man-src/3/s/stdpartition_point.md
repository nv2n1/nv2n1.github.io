---
title: "stdpartition_point(3)"
name: "stdpartition_point"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartition_point/"
---

std::partition_point - std::partition_point

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt, class UnaryPredicate &gt;                                              (since C++11)

ForwardIt partition_point( ForwardIt first, ForwardIt last, UnaryPredicate p );           (1)  (until C++20)

template&lt; class ForwardIt, class UnaryPredicate &gt;                                              (since C++20)

constexpr ForwardIt partition_point( ForwardIt first, ForwardIt last, UnaryPredicate p );</code></pre> 
Examines the partitioned (as if by std::partition) range [first, last) and locates the end of the first partition, that is, the first element that does not satisfy p or last if all elements satisfy p. 

<h2>Parameters</h2>

first, last - the partitioned range of elements to examine 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true for the elements found in the beginning of the range. 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of ForwardIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

The iterator past the end of the first partition within [first, last) or last if all elements satisfy p. 

<h2>Complexity</h2>

Given N = std::distance(first, last), performs O(log N) applications of the predicate p. 
However, for non-LegacyRandomAccessIterators, the number of iterator increments is O(N).

<h2>Notes</h2>

This algorithm is a more general form of std::lower_bound, which can be expressed in terms of std::partition_point with the predicate [&amp;](auto const&amp; e) { return e &lt; value; });. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;array&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;
int main()

{
    std::array&lt;int, 9&gt; v = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    auto is_even = [](int i) { return i % 2 == 0; };
    std::partition(v.begin(), v.end(), is_even);
    auto p = std::partition_point(v.begin(), v.end(), is_even);
    std::cout &lt;&lt; &quot;Before partition:\n    &quot;;
    std::copy(v.begin(), p, std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; &quot;\nAfter partition:\n    &quot;;
    std::copy(p, v.end(), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Before partition: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8 2 6 4 
&nbsp;<wbr>&nbsp;After partition: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 3 7 1 9

<h2>See also</h2>

is_sorted checks whether a range is sorted into ascending order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an iterator to the first element not less than the given value 
lower_bound <i>(function template)</i> 
