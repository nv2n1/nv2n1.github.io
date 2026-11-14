---
title: "stdexperimentalparalleltransform_reduce(3)"
name: "stdexperimentalparalleltransform_reduce"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalparalleltransform_reduce/"
---

std::experimental::parallel::transform_reduce - std::experimental::parallel::transform_reduce

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/numeric&gt;

template&lt;class InputIt, class UnaryOp, class T, class BinaryOp&gt;

T transform_reduce(InputIt first, InputIt last,                 (1) (parallelism TS)

UnaryOp unary_op, T init, BinaryOp binary_op);

template&lt;class ExecutionPolicy,

class InputIt, class UnaryOp, class T, class BinaryOp&gt;

T transform_reduce(ExecutionPolicy&amp;&amp; policy,                    (2) (parallelism TS)

InputIt first, InputIt last,

UnaryOp unary_op, T init, BinaryOp binary_op);</code></pre> 
Applies unary_op to each element in the range [first; last) and reduces the results (possibly permuted and aggregated in unspecified manner) along with the initial value init over binary_op. 
The behavior is non-deterministic if binary_op is not associative or not commutative. 
The behavior is undefined if unary_op or binary_op modifies any element or invalidates any iterator in [first; last). 

<h2>Parameters</h2>

first, last - the range of elements to apply the algorithm to 
init - the initial value of the generalized sum 
policy - the execution_policy 
unary_op - unary FunctionObject that will be applied to each element of the input range. The return type must be acceptable as input to binary_op 
binary_op - binary FunctionObject that will be applied in unspecified order to the results of unary_op, the results of other binary_op and init.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator.

<h2>Return value</h2>

Generalized sum of init and unary_op(*first), unary_op(*(first+1)), ... unary_op(*(last-1)) over binary_op, 
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
 
in other words, the results of unary_op may be grouped and arranged in arbitrary order. 

<h2>Complexity</h2>

O(last - first) applications each of unary_op and binary_op.

<h2>Exceptions</h2>

* If execution of a function invoked as part of the algorithm throws an exception, 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if policy is parallel_vector_execution_policy, std::terminate is called 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if policy is sequential_execution_policy or parallel_execution_policy, the algorithm exits with an exception_list containing all uncaught exceptions. If there was only one uncaught exception, the algorithm may rethrow it without wrapping in exception_list. It is unspecified how much work the algorithm will perform before returning after the first exception was encountered. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if policy is some other type, the behavior is implementation-defined 

 

 

 
* If the algorithm fails to allocate memory (either for itself or to construct an exception_list when handling a user exception), std::bad_alloc is thrown.

<h2>Notes</h2>

unary_op is not applied to init 
If the range is empty, init is returned, unmodified 
* If policy is an instance of sequential_execution_policy, all operations are performed in the calling thread. 
* If policy is an instance of parallel_execution_policy, operations may be performed in unspecified number of threads, indeterminately sequenced with each other 
* If policy is an instance of parallel_vector_execution_policy, execution may be both parallelized and vectorized: function body boundaries are not respected and user code may be overlapped and combined in arbitrary manner (in particular, this implies that a user-provided Callable must not acquire a mutex to access a shared resource) 

<h2>Example</h2>

transform_reduce can be used to parallelize std::inner_product: 
 // Run this code <pre><code>#include &lt;vector&gt;

#include &lt;iterator&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;

#include &lt;experimental/numeric&gt;

#include &lt;experimental/execution_policy&gt;

#include &lt;boost/iterator/zip_iterator.hpp&gt;

#include &lt;boost/tuple.hpp&gt;
int main()

{
    std::vector&lt;double&gt; xvalues(10007, 1.0), yvalues(10007, 1.0);
    double result = std::experimental::parallel::transform_reduce(
        std::experimental::parallel::par,
        boost::iterators::make_zip_iterator(
            boost::make_tuple(std::begin(xvalues), std::begin(yvalues))),
        boost::iterators::make_zip_iterator(
            boost::make_tuple(std::end(xvalues), std::end(yvalues))),
        [](auto r) { return boost::get&lt;0&gt;(r) * boost::get&lt;1&gt;(r); } 0.0,
        std::plus&lt;&gt;());
    std::cout &lt;&lt; result &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10007

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
transform <i>(function template)</i> 
reduce similar to std::accumulate, except out of order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(parallelism TS) 
