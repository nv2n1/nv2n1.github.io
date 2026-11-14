---
title: "stdpartition(3)"
name: "stdpartition"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartition/"
description: "std::partition – std::partition"
---

<p>std::partition &#8211; std::partition</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class BidirIt, class UnaryPredicate &gt;                                             (until C++11)

BidirIt partition( BidirIt first, BidirIt last, UnaryPredicate p );

template&lt; class ForwardIt, class UnaryPredicate &gt;                                           (since C++11)

ForwardIt partition( ForwardIt first, ForwardIt last, UnaryPredicate p );                   (until C++20)

template&lt; class ForwardIt, class UnaryPredicate &gt;                                   (1)     (since C++20)

constexpr ForwardIt partition( ForwardIt first, ForwardIt last, UnaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt, class UnaryPredicate &gt;

ForwardIt partition( ExecutionPolicy&amp;&amp; policy,                                          (2) (since C++17)

ForwardIt first, ForwardIt last, UnaryPredicate p );</code></pre>
<p>1) Reorders the elements in the range [first, last) in such a way that all elements for which the predicate p returns true precede the elements for which predicate p returns false. Relative order of the elements is not preserved.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to reorder<br />
policy &#8211; the execution policy to use. See execution_policy for details.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element should be ordered before other elements.<br />
p &#8211; The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of ForwardIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
BidirIt must meet the requirements of LegacyBidirectionalIterator.<br />
&#8211;<br />
ForwardIt must meet the requirements of ValueSwappable and LegacyForwardIterator. However, the operation is more efficient if ForwardIt also satisfies the requirements of LegacyBidirectionalIterator<br />
&#8211;<br />
UnaryPredicate must meet the requirements of Predicate.</p>
<h2>Return value</h2>
<p>Iterator to the first element of the second group. </p>
<h2>Complexity</h2>
<p>Given N = std::distance(first,last),<br />
1) Exactly N applications of the predicate. At most N/2 swaps if ForwardIt meets the requirements of LegacyBidirectionalIterator, and at most N swaps otherwise.<br />
2) O(N log N) swaps and O(N) applications of the predicate.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class UnaryPredicate&gt;<br />
&nbsp;<wbr>&nbsp;ForwardIt partition(ForwardIt first, ForwardIt last, UnaryPredicate p)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = std::find_if_not(first, last, p);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) return first; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (ForwardIt i = std::next(first); i != last; ++i) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (p(*i)) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::iter_swap(i, first);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;

#include &lt;forward_list&gt;
template &lt;class ForwardIt&gt;
void quicksort(ForwardIt first, ForwardIt last)
{
    if (first == last)
        return;
    auto pivot = *std::next(first, std::distance(first, last) / 2);
    ForwardIt middle1 = std::partition(first, last,
                                       [pivot](const auto &amp;em) { return em &lt; pivot; });
    ForwardIt middle2 = std::partition(middle1, last,
                                       [pivot](const auto &amp;em) { return !(pivot &lt; em); });
    quicksort(first, middle1);
    quicksort(middle2, last);
}
int main()

{
    std::vector&lt;int&gt; v = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    std::cout &lt;&lt; &quot;Original vector:
    &quot;;
    for (int elem : v)
        std::cout &lt;&lt; elem &lt;&lt; ' ';
    auto it = std::partition(v.begin(), v.end(), [](int i) { return i % 2 == 0; });
    std::cout &lt;&lt; &quot;
Partitioned vector:
    &quot;;
    std::copy(std::begin(v), it, std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; &quot; * &quot;;
    std::copy(it, std::end(v), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::forward_list&lt;int&gt; fl = {1, 30, -4, 3, 5, -4, 1, 6, -8, 2, -5, 64, 1, 92};
    std::cout &lt;&lt; &quot;
Unsorted list:
    &quot;;
    for (int n : fl)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
    quicksort(std::begin(fl), std::end(fl));
    std::cout &lt;&lt; &quot;Sorted using quicksort:
    &quot;;
    for (int fi : fl)
        std::cout &lt;&lt; fi &lt;&lt; ' ';
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Original vector:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 1 2 3 4 5 6 7 8 9<br />
&nbsp;<wbr>&nbsp;Partitioned vector:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0 8 2 6 4 * 5 3 7 1 9<br />
&nbsp;<wbr>&nbsp;Unsorted list:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1 30 -4 3 5 -4 1 6 -8 2 -5 64 1 92<br />
&nbsp;<wbr>&nbsp;Sorted using quicksort:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-8 -5 -4 -4 1 1 1 2 3 5 6 30 64 92</p>
<h2>See also</h2>
<p>is_partitioned determines if the range is partitioned by the given predicate<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides elements into two groups while preserving their relative order<br />
stable_partition <i>(function template)</i> </p>
