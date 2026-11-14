---
title: "stdreverse_copy(3)"
name: "stdreverse_copy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreverse_copy/"
---

std::reverse_copy - std::reverse_copy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class BidirIt, class OutputIt&gt;
    (until C++ 20)

        OutputIt reverse_copy(BidirIt first, BidirIt last, OutputIt d_first);

template &lt;class BidirIt, class OutputIt&gt;
(1)(since C++ 20)

    constexpr OutputIt reverse_copy(BidirIt first, BidirIt last, OutputIt d_first);

template &lt;class ExecutionPolicy, class BidirIt, class ForwardIt&gt;
(2)(since C++ 17)

    ForwardIt reverse_copy(ExecutionPolicy &amp;&amp;policy, BidirIt first, BidirIt last, ForwardIt d_first);
1) Copies the elements from the range [first, last) to another range beginning at d_first in such a way that the elements in the new range are in reverse order.

Behaves as if by executing the assignment *(d_first + (last - first) - 1 - i) = *(first + i) once for each non-negative i &lt; (last - first)

If the source and destination ranges (that is, [first, last) and [d_first, d_first+(last-first)) respectively) overlap, the behavior is undefined.

2) Same as (1), but executed according to policy. This overload does not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true
</code></pre>

<h2>Parameters</h2>

first, last - the range of elements to copy 
d_first - the beginning of the destination range

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of LegacyBidirectionalIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

Output iterator to the element past the last element copied. 

<h2>Exceptions</h2>

The overload with a template parameter named ExecutionPolicy reports errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

See also the implementations in libstdc++ and libc++. 

 

 
&nbsp;<wbr>&nbsp;template&lt;class BidirIt, class OutputIt&gt; 
&nbsp;<wbr>&nbsp;OutputIt reverse_copy(BidirIt first, BidirIt last, OutputIt d_first) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*(d_first++) = *(--last); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;
int main()

{
    std::vector&lt;int&gt; v({1, 2, 3});
    for (const auto &amp;value : v) {
        std::cout &lt;&lt; value &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
    std::vector&lt;int&gt; destination(3);
    std::reverse_copy(std::begin(v), std::end(v), std::begin(destination));
    for (const auto &amp;value : destination) {
        std::cout &lt;&lt; value &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3 
&nbsp;<wbr>&nbsp;3 2 1

<h2>Complexity</h2>

Linear in the distance between first and last

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reverses the order of elements in a range 
reverse <i>(function template)</i> 
