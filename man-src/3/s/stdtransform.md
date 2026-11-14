---
title: "stdtransform(3)"
name: "stdtransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtransform/"
---

std::transform - std::transform

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class OutputIt, class UnaryOperation &gt;

OutputIt transform( InputIt first1, InputIt last1, OutputIt d_first,                                                   (until C++20)

UnaryOperation unary_op );

template&lt; class InputIt, class OutputIt, class UnaryOperation &gt;

constexpr OutputIt transform( InputIt first1, InputIt last1, OutputIt d_first,                                         (since C++20)

UnaryOperation unary_op );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class UnaryOperation &gt;

ForwardIt2 transform( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                               (2) (since C++17)

ForwardIt2 d_first, UnaryOperation unary_op );                                                                 (1)

template&lt; class InputIt1, class InputIt2, class OutputIt, class BinaryOperation &gt;

OutputIt transform( InputIt1 first1, InputIt1 last1, InputIt2 first2,                                                                (until C++20)

OutputIt d_first, BinaryOperation binary_op );

template&lt; class InputIt1, class InputIt2, class OutputIt, class BinaryOperation &gt;

constexpr OutputIt transform( InputIt1 first1, InputIt1 last1, InputIt2 first2,                                    (3)               (since C++20)

OutputIt d_first, BinaryOperation binary_op );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class ForwardIt3, class BinaryOperation &gt;

ForwardIt3 transform( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                                   (4)           (since C++17)

ForwardIt2 first2, ForwardIt3 d_first, BinaryOperation binary_op );</code></pre> 
std::transform applies the given function to a range and stores the result in another range, beginning at d_first. 
1) The unary operation unary_op is applied to the range defined by [first1, last1). 
3) The binary operation binary_op is applied to pairs of elements from two ranges: one defined by [first1, last1) and the other beginning at first2. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 
unary_op and binary_op must not have side effects. <i>(until C++11)</i> 
unary_op and binary_op must not invalidate any iterators, including the end iterators, or modify any elements of the ranges involved. <i>(since C++11)</i> 

<h2>Parameters</h2>

first1, last1 - the first range of elements to transform 
first2 - the beginning of the second range of elements to transform 
d_first - the beginning of the destination range, may be equal to first1 or first2 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary operation function object that will be applied. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
unary_op - Ret fun(const Type &amp;a); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type must be such that an object of type InputIt can be dereferenced and then implicitly converted to Type. The type Ret must be such that an object of type OutputIt can be dereferenced and assigned a value of type Ret. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary operation function object that will be applied. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
binary_op - Ret fun(const Type1 &amp;a, const Type2 &amp;b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that objects of types InputIt1 and InputIt2 can be dereferenced and then implicitly converted to Type1 and Type2 respectively. The type Ret must be such that an object of type OutputIt can be dereferenced and assigned a value of type Ret.

<h2>Type requirements</h2>

- 
InputIt, InputIt1, InputIt2 must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2, ForwardIt3 must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

Output iterator to the element past the last element transformed. 

<h2>Complexity</h2>

1-2) Exactly std::distance(first1, last1) applications of unary_op 
3-4) Exactly std::distance(first1, last1) applications of binary_op

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class UnaryOperation&gt; 
&nbsp;<wbr>&nbsp;OutputIt transform(InputIt first1, InputIt last1, OutputIt d_first, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;UnaryOperation unary_op) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = unary_op(*first1++); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class OutputIt, class BinaryOperation&gt; 
&nbsp;<wbr>&nbsp;OutputIt transform(InputIt1 first1, InputIt1 last1, InputIt2 first2, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first, BinaryOperation binary_op) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = binary_op(*first1++, *first2++); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

std::transform does not guarantee in-order application of unary_op or binary_op. To apply a function to a sequence in-order or to apply a function that modifies the elements of a sequence, use std::for_each 

<h2>Example</h2>

The following code uses transform to convert a string in place to uppercase using the toupper function and then transforms each char to its ordinal value: 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;cctype&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;vector&gt;
int main()

{
    std::string s(&quot;hello&quot;);
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) -&gt; unsigned char { return std::toupper(c); });
    std::vector&lt;std::size_t&gt; ordinals;
    std::transform(s.begin(), s.end(), std::back_inserter(ordinals),
                   [](unsigned char c) -&gt; std::size_t { return c; });
    std::cout &lt;&lt; s &lt;&lt; ':';
    for (auto ord : ordinals) {
        std::cout &lt;&lt; ' ' &lt;&lt; ord;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;HELLO: 72 69 76 76 79

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
for_each <i>(function template)</i> 
