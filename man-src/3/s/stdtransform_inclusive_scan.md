---
title: "stdtransform_inclusive_scan(3)"
name: "stdtransform_inclusive_scan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtransform_inclusive_scan/"
---

std::transform_inclusive_scan - std::transform_inclusive_scan

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class InputIt, class OutputIt,

class BinaryOperation, class UnaryOperation &gt;                                     (1) (since C++17)

OutputIt transform_inclusive_scan( InputIt first, InputIt last, OutputIt d_first,

BinaryOperation binary_op, UnaryOperation unary_op );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2,

class BinaryOperation, class UnaryOperation &gt;

ForwardIt2 transform_inclusive_scan( ExecutionPolicy&amp;&amp; policy,                    (2) (since C++17)

ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first,

BinaryOperation binary_op, UnaryOperation unary_op );

template&lt; class InputIt, class OutputIt,

class BinaryOperation, class UnaryOperation, class T &gt;

OutputIt transform_inclusive_scan( InputIt first, InputIt last, OutputIt d_first, (3) (since C++17)

BinaryOperation binary_op, UnaryOperation unary_op,

T init );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2,

class BinaryOperation, class UnaryOperation, class T &gt;

ForwardIt2 transform_inclusive_scan( ExecutionPolicy&amp;&amp; policy,                    (4) (since C++17)

ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first,

BinaryOperation binary_op, UnaryOperation unary_op,

T init );</code></pre> 
Transforms each element in the range [first, last) with unary_op, then computes an inclusive prefix sum operation using binary_op over the resulting range, optionally with init as the initial value, and writes the results to the range beginning at d_first. &quot;inclusive&quot; means that the i-th input element is included in the i-th sum. 
Formally, assigns through each iterator i in [d_first, d_first + (last - first)) the value of 
* for overloads (1-2), the generalized noncommutative sum of unary_op(*j)... for every j in [first, first + (i - d_first + 1)) over binary_op, 
* for overloads (3-4), the generalized noncommutative sum of init, unary_op(*j)... for every j in [first, first + (i - d_first + 1)) over binary_op, 
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
Overloads (2, 4) are executed according to policy, and do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true. 
unary_op and binary_op shall not invalidate iterators (including the end iterators) or subranges, nor modify elements in the ranges [first, last) or [d_first, d_first + (last - first)). Otherwise, the behavior is undefined. 

<h2>Parameters</h2>

first, last - the range of elements to sum 
d_first - the beginning of the destination range; may be equal to first 
policy - the execution policy to use. See execution_policy for details. 
init - the initial value 
unary_op - unary FunctionObject that will be applied to each element of the input range. The return type must be acceptable as input to binary_op. 
binary_op - binary FunctionObject that will be applied in to the result of unary_op, the results of other binary_op, and init if provided.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1 must meet the requirements of LegacyForwardIterator. and, if init is not provided, ForwardIt1's value_type must be MoveConstructible and binary_op(unary_op(*first), unary_op(*first)) must be convertible to ForwardIt1's value type 
- 
ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
T (if init is provided) must meet the requirements of MoveConstructible. All of binary_op(init, unary_op(*first)), binary_op(init, init), and binary_op(unary_op(*first), unary_op(*first)) must be convertible to T

<h2>Return value</h2>

Iterator to the element past the last element written. 

<h2>Complexity</h2>

O(last - first) applications of each of binary_op and unary_op.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

unary_op is not applied to init. 
The parameter init appears last, differing from std::transform_exclusive_scan, because it is optional for this function. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

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
    std::cout &lt;&lt; &quot;\n10 times inclusive sum: &quot;;
    std::transform_inclusive_scan(data.begin(), data.end(),

                                  std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;),

                                  std::plus&lt;int&gt;{}, times_10);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10 times exclusive sum: 0 30 40 80 90 140 230 250 
&nbsp;<wbr>&nbsp;10 times inclusive sum: 30 40 80 90 140 230 250 310

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the partial sum of a range of elements 
partial_sum <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
transform <i>(function template)</i> 
inclusive_scan similar to std::partial_sum, includes the ith input element in the ith sum 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
transform_exclusive_scan applies a functor, then calculates exclusive scan 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
