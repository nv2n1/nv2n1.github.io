---
title: "stdis_partitioned(3)"
name: "stdis_partitioned"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_partitioned/"
description: "std::is_partitioned – std::is_partitioned"
---

<p>std::is_partitioned &#8211; std::is_partitioned</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class UnaryPredicate &gt;                                                             (since C++11)

bool is_partitioned( InputIt first, InputIt last, UnaryPredicate p );                                       (until C++20)

template&lt; class InputIt, class UnaryPredicate &gt;                                                     (1)     (since C++20)

constexpr bool is_partitioned( InputIt first, InputIt last, UnaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt, class UnaryPredicate &gt;                                (2) (since C++17)

bool is_partitioned( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, UnaryPredicate p );</code></pre>
<p>1) Returns true if all elements in the range [first, last) that satisfy the predicate p appear before all elements that don&#8217;t. Also returns true if [first, last) is empty.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to check<br />
policy &#8211; the execution policy to use. See execution_policy for details.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true for the elements expected to be found in the beginning of the range.<br />
p &#8211; The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
ForwardIt must meet the requirements of LegacyForwardIterator. and its value type must be convertible to UnaryPredicate&#8217;s argument type<br />
&#8211;<br />
UnaryPredicate must meet the requirements of Predicate.</p>
<h2>Return value</h2>
<p>true if the range [first, last) is empty or is partitioned by p. false otherwise. </p>
<h2>Complexity</h2>
<p>At most std::distance(first, last) applications of p.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;template&lt; class InputIt, class UnaryPredicate &gt;<br />
&nbsp;<wbr>&nbsp;bool is_partitioned(InputIt first, InputIt last, UnaryPredicate p)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!p(*first))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (p(*first))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return true;<br />
&nbsp;<wbr>&nbsp;}</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;algorithm&gt;

#include &lt;array&gt;

#include &lt;iostream&gt;
int main()

{
    std::array&lt;int, 9&gt; v = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    auto is_even = [](int i) { return i % 2 == 0; };
    std::cout.setf(std::ios_base::boolalpha);
    std::cout &lt;&lt; std::is_partitioned(v.begin(), v.end(), is_even) &lt;&lt; ' ';
    std::partition(v.begin(), v.end(), is_even);
    std::cout &lt;&lt; std::is_partitioned(v.begin(), v.end(), is_even) &lt;&lt; ' ';
    std::reverse(v.begin(), v.end());
    std::cout &lt;&lt; std::is_partitioned(v.begin(), v.end(), is_even);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;false true false</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides a range of elements into two groups<br />
partition <i>(function template)</i><br />
partition_point locates the partition point of a partitioned range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
