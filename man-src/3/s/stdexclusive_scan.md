---
title: "stdexclusive_scan(3)"
name: "stdexclusive_scan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexclusive_scan/"
---

std::exclusive_scan - std::exclusive_scan

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class InputIt, class OutputIt, class T &gt;

OutputIt exclusive_scan( InputIt first, InputIt last,                                   (1) (since C++17)

OutputIt d_first, T init );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class T &gt;

ForwardIt2 exclusive_scan( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last, (2) (since C++17)

ForwardIt2 d_first, T init);

template&lt; class InputIt, class OutputIt,

class T, class BinaryOperation &gt;                                                        (3) (since C++17)

OutputIt exclusive_scan( InputIt first, InputIt last,

OutputIt d_first, T init, BinaryOperation binary_op );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2,

class T, class BinaryOperation &gt;                                                        (4) (since C++17)

ForwardIt2 exclusive_scan( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last,

ForwardIt2 d_first, T init, BinaryOperation binary_op );</code></pre> 
Computes an exclusive prefix sum operation using binary_op (or std::plus&lt;&gt;() for overloads (1-2)) for the range [first, last), using init as the initial value, and writes the results to the range beginning at d_first. &quot;exclusive&quot; means that the i-th input element is not included in the i-th sum. 
Formally, assigns through each iterator i in [d_first, d_first + (last - first)) the value of the generalized noncommutative sum of init, *j... for every j in [first, first + (i - d_first)) over binary_op, 
where generalized noncommutative sum GNSUM(op, a 
1, ..., a 
N) is defined as follows: * if N=1, a

1

* if N &gt; 1, op(GNSUM(op, a

1, ..., a

K), GNSUM(op, a

M, ..., a

N)) for any K where 1 &lt; K+1 = M ≤ N 
In other words, the summation operations may be performed in arbitrary order, and the behavior is nondeterministic if binary_op is not associative. 
Overloads (2,4) are executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. 
binary_op shall not invalidate iterators (including the end iterators) or subranges, nor modify elements in the ranges [first, last) or [d_first, d_first + (last - first)). Otherwise, the behavior is undefined. 

<h2>Parameters</h2>

first, last - the range of elements to sum 
d_first - the beginning of the destination range; may be equal to first 
policy - the execution policy to use. See execution_policy for details. 
init - the initial value 
binary_op - binary FunctionObject that will be applied in to the result of dereferencing the input iterators, the results of other binary_op, and init.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
T must meet the requirements of MoveConstructible. and binary_op(init, *first), binary_op(init, init), and binary_op(*first, *first) must be convertible to T

<h2>Return value</h2>

Iterator to the element past the last element written. 

<h2>Complexity</h2>

O(last - first) applications of the binary operation

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;numeric&gt;

#include &lt;vector&gt;
int main()

{
    std::vector data{3, 1, 4, 1, 5, 9, 2, 6};
    std::cout &lt;&lt; &quot;exclusive sum: &quot;;
    std::exclusive_scan(data.begin(), data.end(),

                        std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),

                        0);
    std::cout &lt;&lt; &quot;\ninclusive sum: &quot;;
    std::inclusive_scan(data.begin(), data.end(),

                        std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; &quot;\n\nexclusive product: &quot;;
    std::exclusive_scan(data.begin(), data.end(),

                        std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),

                        1, std::multiplies&lt;&gt;{});

    std::cout &lt;&lt; &quot;\ninclusive product: &quot;;

    std::inclusive_scan(data.begin(), data.end(),

                        std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),

                        std::multiplies&lt;&gt;{});
}</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;exclusive sum: 0 3 4 8 9 14 23 25 
&nbsp;<wbr>&nbsp;inclusive sum: 3 4 8 9 14 23 25 31 

 
&nbsp;<wbr>&nbsp;exclusive product: 1 3 3 12 12 60 540 1080 
&nbsp;<wbr>&nbsp;inclusive product: 3 3 12 12 60 540 1080 6480

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the differences between adjacent elements in a range 
adjacent_difference <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the partial sum of a range of elements 
partial_sum <i>(function template)</i> 
transform_exclusive_scan applies a functor, then calculates exclusive scan 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
inclusive_scan similar to std::partial_sum, includes the ith input element in the ith sum 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
