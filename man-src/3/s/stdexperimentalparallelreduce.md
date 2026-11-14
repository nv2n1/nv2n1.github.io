---
title: "stdexperimentalparallelreduce(3)"
name: "stdexperimentalparallelreduce"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalparallelreduce/"
---

std::experimental::parallel::reduce - std::experimental::parallel::reduce

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/numeric&gt;

template&lt;class InputIt&gt;

typename std::iterator_traits&lt;InputIt&gt;::value_type reduce(               (1) (parallelism TS)

InputIt first, InputIt last);

template&lt;class ExecutionPolicy, class InputIterator&gt;

typename std::iterator_traits&lt;InputIt&gt;::value_type reduce(               (2) (parallelism TS)

ExecutionPolicy&amp;&amp; policy, InputIt first, InputIt last);

template&lt;class InputIt, class T&gt;                                         (3) (parallelism TS)

T reduce(InputIt first, InputIt last, T init);

template&lt;class ExecutionPolicy, class InputIt, class T&gt;                  (4) (parallelism TS)

T reduce(ExecutionPolicy&amp;&amp; policy, InputIt first, InputIt last, T init);

template&lt;class InputIt, class T, class BinaryOp&gt;                         (5) (parallelism TS)

T reduce(InputIt first, InputIt last, T init, BinaryOp binary_op);

template&lt;class ExecutionPolicy, class InputIt, class T, class BinaryOp&gt;

T reduce(ExecutionPolicy&amp;&amp; policy,                                       (6) (parallelism TS)

InputIt first, InputIt last, T init, BinaryOp binary_op);</code></pre> 
1) same as reduce(first, last, typename std::iterator_traits&lt;InputIt&gt;::value_type{}) 
3) same as reduce(first, last, init, std::plus&lt;&gt;()) 
5) Reduces the range [first; last), possibly permuted and aggregated in unspecified manner, along with the initial value init over binary_op. 
2,4,6) Same as (1,3,5), but executed according to policy 
The behavior is non-deterministic if binary_op is not associative or not commutative. 
The behavior is undefined if binary_op modifies any element or invalidates any iterator in [first; last). 

<h2>Parameters</h2>

first, last - the range of elements to apply the algorithm to 
init - the initial value of the generalized sum 
policy - the execution_policy 
binary_op - binary FunctionObject that will be applied in unspecified order to the result of dereferencing the input iterators, the results of other binary_op and init.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator.

<h2>Return value</h2>

Generalized sum of init and *first, *(first+1), ... *(last-1) over binary_op, 
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
 
in other words, the elements of the range may be grouped and rearranged in arbitrary order 

<h2>Complexity</h2>

O(last - first) applications of binary_op.

<h2>Exceptions</h2>

* If execution of a function invoked as part of the algorithm throws an exception, 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if policy is parallel_vector_execution_policy, std::terminate is called 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if policy is sequential_execution_policy or parallel_execution_policy, the algorithm exits with an exception_list containing all uncaught exceptions. If there was only one uncaught exception, the algorithm may rethrow it without wrapping in exception_list. It is unspecified how much work the algorithm will perform before returning after the first exception was encountered. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if policy is some other type, the behavior is implementation-defined 

 

 

 
* If the algorithm fails to allocate memory (either for itself or to construct an exception_list when handling a user exception), std::bad_alloc is thrown.

<h2>Notes</h2>

If the range is empty, init is returned, unmodified 
* If policy is an instance of sequential_execution_policy, all operations are performed in the calling thread. 
* If policy is an instance of parallel_execution_policy, operations may be performed in unspecified number of threads, indeterminately sequenced with each other 
* If policy is an instance of parallel_vector_execution_policy, execution may be both parallelized and vectorized: function body boundaries are not respected and user code may be overlapped and combined in arbitrary manner (in particular, this implies that a user-provided Callable must not acquire a mutex to access a shared resource) 

<h2>Example</h2>

reduce is the out-of-order version of std::accumulate: 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;

#include &lt;vector&gt;

#include &lt;numeric&gt;

#include &lt;experimental/execution_policy&gt;

#include &lt;experimental/numeric&gt;
int main()

{
    std::vector&lt;double&gt; v(10'000'007, 0.5);
    {
        auto t1 = std::chrono::high_resolution_clock::now();
        double result = std::accumulate(v.begin(), v.end(), 0.0);
        auto t2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration&lt;double, std::milli&gt; ms = t2 - t1;
        std::cout &lt;&lt; std::fixed &lt;&lt; &quot;std::accumulate result &quot; &lt;&lt; result
                  &lt;&lt; &quot; took &quot; &lt;&lt; ms.count() &lt;&lt; &quot; ms\n&quot;;
    }
    {
        auto t1 = std::chrono::high_resolution_clock::now();
        double result = std::experimental::parallel::reduce(
            std::experimental::parallel::par,
            v.begin(), v.end());
        auto t2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration&lt;double, std::milli&gt; ms = t2 - t1;
        std::cout &lt;&lt; &quot;parallel::reduce result &quot;
                  &lt;&lt; result &lt;&lt; &quot; took &quot; &lt;&lt; ms.count() &lt;&lt; &quot; ms\n&quot;;
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;std::accumulate result 5000003.50000 took 12.7365 ms 
&nbsp;<wbr>&nbsp;parallel::reduce result 5000003.50000 took 5.06423 ms

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
transform <i>(function template)</i> 
transform_reduce applies a functor, then reduces out of order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(parallelism TS) 
