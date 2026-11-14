---
title: "stdtransform_reduce(3)"
name: "stdtransform_reduce"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtransform_reduce/"
---

std::transform_reduce - std::transform_reduce

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt;class InputIt1, class InputIt2, class T&gt;                                    (1) (since C++17)

T transform_reduce(InputIt1 first1, InputIt1 last1, InputIt2 first2, T init);

template &lt;class InputIt1, class InputIt2, class T, class BinaryOp1, class BinaryOp2&gt;

T transform_reduce(InputIt1 first1, InputIt1 last1, InputIt2 first2,                 (2) (since C++17)

T init, BinaryOp1 binary_op1, BinaryOp2 binary_op2);

template&lt;class InputIt, class T, class BinaryOp, class UnaryOp&gt;

T transform_reduce(InputIt first, InputIt last,                                      (3) (since C++17)

T init, BinaryOp binop, UnaryOp unary_op);

template&lt;class ExecutionPolicy,

class ForwardIt1, class ForwardIt2, class T&gt;                                         (4) (since C++17)

T transform_reduce(ExecutionPolicy&amp;&amp; policy,

ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2, T init);

template&lt;class ExecutionPolicy,

class ForwardIt1, class ForwardIt2, class T, class BinaryOp1, class BinaryOp2&gt;

T transform_reduce(ExecutionPolicy&amp;&amp; policy,                                         (5) (since C++17)

ForwardIt1 first1, ForwardIt1 last1, ForwardIt2 first2,

T init, BinaryOp1 binary_op1, BinaryOp2 binary_op2);

template&lt;class ExecutionPolicy,

class ForwardIt, class T, class BinaryOp, class UnaryOp&gt;

T transform_reduce(ExecutionPolicy&amp;&amp; policy,                                         (6) (since C++17)

ForwardIt first, ForwardIt last,

T init, BinaryOp binary_op, UnaryOp unary_op);</code></pre> 
1) Equivalent to transform_reduce(first1, last1, first2, init, std::plus&lt;&gt;(), std::multiplies&lt;&gt;());, effectively parallelized version of the default std::inner_product 
2) Applies binary_op2 to each pair of elements from the ranges [first; last) and the range starting at first2 and reduces the results (possibly permuted and aggregated in unspecified manner) along with the initial value init over binary_op1 
3) Applies unary_op to each element in the range [first; last) and reduces the results (possibly permuted and aggregated in unspecified manner) along with the initial value init over binary_op. 
4-6) Same as (1-3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 
The behavior is non-deterministic if binary_op/binary_op2 is not associative or not commutative. 
The behavior is undefined if unary_op, binary_op, binary_op1, or binary_op2 modifies any element or invalidates any iterator in the input ranges, including their end iterators. 

<h2>Parameters</h2>

first, last - the range of elements to apply the algorithm to 
init - the initial value of the generalized sum 
policy - the execution policy to use. See execution_policy for details. 
unary_op - unary FunctionObject that will be applied to each element of the input range. The return type must be acceptable as input to binary_op 
binary_op - binary FunctionObject that will be applied in unspecified order to the results of unary_op, the results of other binary_op and init.

<h2>Type requirements</h2>

- 
T must meet the requirements of MoveConstructible in order to use overloads (3,6). and the result of the expressions binary_op(init, unary_op(*first)), binary_op(unary_op(*first), init), binary_op(init, init), and binary_op(unary_op(*first), unary_op(*first)) must be convertible to T 
- 
T must meet the requirements of MoveConstructible in order to use overloads (2,5). and the result of the expressions binary_op1(init, binary_op2(*first1, *first2)), binary_op1(binary_op2(*first1, *first2), init), binary_op1(init, init), and binary_op1(binary_op2(*first1, *first2), binary_op2(*first1, *first2)) must be convertible to T 
- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

2) Generalized sum of init and binary_op2(*first,*first2), binary_op2(*(first+1),*(first2+1)), ..., over binary_op1 
3) Generalized sum of init and unary_op(*first), unary_op(*(first+1)), ... unary_op(*(last-1)) over binary_op, 
where generalized sum GSUM(op, a 
1, ..., a 
N) is defined as follows: * if N=1, a

1

* if N &gt; 1, op(GSUM(op, b

1, ..., b

K), GSUM(op, b

M, ..., b

N)) where


* b
1, ..., b
N may be any permutation of a1, ..., aN and
* 1 &lt; K+1 = M ≤ N
 
in other words, the results of unary_op or of binary_op1 may be grouped and arranged in arbitrary order. 

<h2>Complexity</h2>

1,2,4,5) O(last1 - first1) applications each of binary_op1 and binary_op2. 
3,6) O(last - first) applications each of unary_op and binary_op.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

In the unary-binary overload (3,6), unary_op is not applied to init 
If first == last or first1 == last1, init is returned, unmodified 

<h2>Example</h2>

transform_reduce can be used to parallelize std::inner_product: 
 // Run this code <pre><code>#include &lt;vector&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;numeric&gt;

#include &lt;execution&gt;
int main()

{
    std::vector&lt;double&gt; xvalues(10007, 1.0), yvalues(10007, 1.0);
    double result = std::transform_reduce(
        std::execution::par,
        xvalues.begin(), xvalues.end(),
        yvalues.begin(), 0.0);
    std::cout &lt;&lt; result &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10007

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
transform <i>(function template)</i> 
reduce similar to std::accumulate, except out of order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
