---
title: "stdtransform_exclusive_scan(3)"
name: "stdtransform_exclusive_scan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtransform_exclusive_scan/"
description: "std::transform_exclusive_scan – std::transform_exclusive_scan"
---

<p>std::transform_exclusive_scan &#8211; std::transform_exclusive_scan</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;numeric&gt;

template&lt; class InputIt, class OutputIt, class T,

class BinaryOperation, class UnaryOperation&gt;                                              (1) (since C++17)

OutputIt transform_exclusive_scan( InputIt first, InputIt last, OutputIt d_first, T init,

BinaryOperation binary_op, UnaryOperation unary_op);

template&lt; class ExecutionPolicy,

class ForwardIt1, class ForwardIt2,

class T, class BinaryOperation, class UnaryOperation &gt;

ForwardIt2 transform_exclusive_scan( ExecutionPolicy&amp;&amp; policy,                            (2) (since C++17)

ForwardIt1 first, ForwardIt1 last,

ForwardIt2 d_first, T init,

BinaryOperation binary_op, UnaryOperation unary_op );</code></pre>
<p>Transforms each element in the range [first, last) with unary_op, then computes an exclusive prefix sum operation using binary_op over the resulting range, with init as the initial value, and writes the results to the range beginning at d_first. &quot;exclusive&quot; means that the i-th input element is not included in the i-th sum.<br />
Formally, assigns through each iterator i in [d_first, d_first + (last &#8211; first)) the value of the generalized noncommutative sum of init, unary_op(*j)&#8230; for every j in [first, first + (i &#8211; d_first)) over binary_op,<br />
where generalized noncommutative sum GNSUM(op, a<br />
1, &#8230;, a<br />
N) is defined as follows: * if N=1, a</p>
<p>1</p>
<p>* if N &gt; 1, op(GNSUM(op, a</p>
<p>1, &#8230;, a</p>
<p>K), GNSUM(op, a</p>
<p>M, &#8230;, a</p>
<p>N)) for any K where 1 &lt; K+1 = M ≤ N<br />
In other words, the summation operations may be performed in arbitrary order, and the behavior is nondeterministic if binary_op is not associative.<br />
Overload <code>(2)</code> is executed according to policy, and does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true.<br />
unary_op and binary_op shall not invalidate iterators (including the end iterators) or subranges, nor modify elements in the ranges [first, last) or [d_first, d_first + (last &#8211; first)). Otherwise, the behavior is undefined. </p>
<h2>Parameters</h2>
<p>first, last &#8211; the range of elements to sum<br />
d_first &#8211; the beginning of the destination range, may be equal to first<br />
policy &#8211; the execution policy to use. See execution_policy for details.<br />
init &#8211; the initial value<br />
unary_op &#8211; unary FunctionObject that will be applied to each element of the input range. The return type must be acceptable as input to binary_op.<br />
binary_op &#8211; binary FunctionObject that will be applied in to the result of unary_op, the results of other binary_op, and init.</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
OutputIt must meet the requirements of LegacyOutputIterator.<br />
&#8211;<br />
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.<br />
&#8211;<br />
T must meet the requirements of MoveConstructible. All of binary_op(init, unary_op(*first)), binary_op(init, init), and binary_op(unary_op(*first), unary_op(*first)) must be convertible to T.</p>
<h2>Return value</h2>
<p>Iterator to the element past the last element written. </p>
<h2>Complexity</h2>
<p>O(last &#8211; first) applications of each of binary_op and unary_op.</p>
<h2>Exceptions</h2>
<p>The overload with a template parameter named ExecutionPolicy reports errors as follows: </p>
<p>* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined.<br />
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.</p>
<h2>Notes</h2>
<p>unary_op is not applied to init. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;numeric&gt;

#include &lt;vector&gt;
int times_10(int x)

{
    return x * 10;
}
int main()

{
    std::vector data{3, 1, 4, 1, 5, 9, 2, 6};
    std::cout &lt;&lt; &quot;10 times exclusive sum: &quot;;
    std::transform_exclusive_scan(data.begin(), data.end(),

                                  std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),

                                  0, std::plus&lt;int&gt;{}, times_10);
    std::cout &lt;&lt; &quot;
10 times inclusive sum: &quot;;
    std::transform_inclusive_scan(data.begin(), data.end(),

                                  std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),

                                  std::plus&lt;int&gt;{}, times_10);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;10 times exclusive sum: 0 30 40 80 90 140 230 250<br />
&nbsp;<wbr>&nbsp;10 times inclusive sum: 30 40 80 90 140 230 250 310</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the partial sum of a range of elements<br />
partial_sum <i>(function template)</i><br />
exclusive_scan similar to std::partial_sum, excludes the ith input element from the ith sum<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
transform_inclusive_scan applies a functor, then calculates inclusive scan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i> </p>
