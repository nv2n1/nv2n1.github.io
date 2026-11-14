---
title: "stdstable_partition(3)"
name: "stdstable_partition"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstable_partition/"
description: "std::stable_partition – std::stable_partition"
---

<p>std::stable_partition &#8211; std::stable_partition</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class BidirIt, class UnaryPredicate &gt;                                                      (1)

BidirIt stable_partition( BidirIt first, BidirIt last, UnaryPredicate p );

template&lt; class ExecutionPolicy, class BidirIt, class UnaryPredicate &gt;                               (2) (since C++17)

BidirIt stable_partition( ExecutionPolicy&amp;&amp; policy, BidirIt first, BidirIt last, UnaryPredicate p );</code></pre>
<p>1) Reorders the elements in the range [first, last) in such a way that all elements for which the predicate p returns true precede the elements for which predicate p returns false. Relative order of the elements is preserved.<br />
2) Same as <code>(1)</code>, but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to reorder<br />
policy &#8211; the execution policy to use. See execution_policy for details.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element should be ordered before other elements.<br />
p &#8211; The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of BidirIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
BidirIt must meet the requirements of ValueSwappable and LegacyBidirectionalIterator.<br />
&#8211;<br />
The type of dereferenced BidirIt must meet the requirements of MoveAssignable and MoveConstructible.<br />
&#8211;<br />
UnaryPredicate must meet the requirements of Predicate.</p>
<h2>Return value</h2>
<p>Iterator to the first element of the second group </p>
<h2>Complexity</h2>
<p>Given N = last &#8211; first<br />
1) Exactly N applications of the predicate and O(N) swaps if there is enough extra memory. If memory is insufficient, at most N log N swaps.<br />
2) O(N log N) swaps and O(N) applications of the predicate</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Notes</h2>
<p>This function attempts to allocate a temporary buffer. If the allocation fails, the less efficient algorithm is chosen. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{0, 0, 3, 0, 2, 4, 5, 0, 7};
    std::stable_partition(v.begin(), v.end(), [](int n) { return n &gt; 0; });
    for (int n : v) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;3 2 4 5 7 0 0 0 0</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides a range of elements into two groups<br />
partition <i>(function template)</i> </p>
