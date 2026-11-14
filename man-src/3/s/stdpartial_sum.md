---
title: "stdpartial_sum(3)"
name: "stdpartial_sum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartial_sum/"
---

std::partial_sum - std::partial_sum

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class InputIt, class OutputIt &gt;                              (1)

OutputIt partial_sum( InputIt first, InputIt last, OutputIt d_first );

template&lt; class InputIt, class OutputIt, class BinaryOperation &gt;

OutputIt partial_sum( InputIt first, InputIt last, OutputIt d_first,   (2)

BinaryOperation op );</code></pre> 
Computes the partial sums of the elements in the subranges of the range [first, last) and writes them to the range beginning at d_first. The first version uses operator+ to sum up the elements, the second version uses the given binary function op 
, both applying std::move to their operands on the left hand side 
<i>(since C++20)</i>. 
Equivalent operation: *(d_first)   = *first;

*(d_first+1) = *first + *(first+1);

*(d_first+2) = *first + *(first+1) + *(first+2);

*(d_first+3) = *first + *(first+1) + *(first+2) + *(first+3);

...
 
op must not have side effects. <i>(until C++11)</i> 
op must not invalidate any iterators, including the end iterators, or modify any elements of the range involved. <i>(since C++11)</i> 

<h2>Parameters</h2>

first, last - the range of elements to sum 
d_first - the beginning of the destination range; may be equal to first 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary operation function object that will be applied. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
op - Ret fun(const Type1 &amp;a, const Type2 &amp;b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type1 must be such that an object of type iterator_traits&lt;InputIt&gt;::value_type can be implicitly converted to Type1. The type Type2 must be such that an object of type InputIt can be dereferenced and then implicitly converted to Type2. The type Ret must be such that an object of type iterator_traits&lt;InputIt&gt;::value_type can be assigned a value of type Ret.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator.

<h2>Return value</h2>

Iterator to the element past the last element written. 

<h2>Complexity</h2>

Exactly (last - first) - 1 applications of the binary operation

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt&gt; 
&nbsp;<wbr>&nbsp;OutputIt partial_sum(InputIt first, InputIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) return d_first; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;InputIt&gt;::value_type sum = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first = sum; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sum = std::move(sum) + *first; // std::move since C++20 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*++d_first = sum; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ++d_first; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// or, since C++14: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// return std::partial_sum(first, last, d_first, std::plus&lt;&gt;()); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class BinaryOperation&gt; 
&nbsp;<wbr>&nbsp;OutputIt partial_sum(InputIt first, InputIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first, BinaryOperation op) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) return d_first; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;InputIt&gt;::value_type sum = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first = sum; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sum = op(std::move(sum), *first); // std::move since C++20 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*++d_first = sum; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ++d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;numeric&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;functional&gt;
int main()

{
    std::vector&lt;int&gt; v = {2, 2, 2, 2, 2, 2, 2, 2, 2, 2}; // or std::vector&lt;int&gt;v(10, 2);
    std::cout &lt;&lt; &quot;The first 10 even numbers are: &quot;;
    std::partial_sum(v.begin(), v.end(),
                     std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
    std::partial_sum(v.begin(), v.end(), v.begin(), std::multiplies&lt;int&gt;());
    std::cout &lt;&lt; &quot;The first 10 powers of 2 are: &quot;;
    for (auto n : v) {
        std::cout &lt;&lt; n &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The first 10 even numbers are: 2 4 6 8 10 12 14 16 18 20 
&nbsp;<wbr>&nbsp;The first 10 powers of 2 are: 2 4 8 16 32 64 128 256 512 1024

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the differences between adjacent elements in a range 
adjacent_difference <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
inclusive_scan similar to std::partial_sum, includes the ith input element in the ith sum 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
exclusive_scan similar to std::partial_sum, excludes the ith input element from the ith sum 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
