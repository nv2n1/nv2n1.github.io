---
title: "stdinner_product(3)"
name: "stdinner_product"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinner_product/"
---

std::inner_product - std::inner_product

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class InputIt1, class InputIt2, class T &gt;

T inner_product( InputIt1 first1, InputIt1 last1,   (1)

InputIt2 first2, T init );

template&lt;class InputIt1, class InputIt2, class T,

class BinaryOperation1, class BinaryOperation2&gt;

T inner_product( InputIt1 first1, InputIt1 last1,   (2)

InputIt2 first2, T init,

BinaryOperation1 op1,

BinaryOperation2 op2 );</code></pre> 
Computes inner product (i.e. sum of products) or performs ordered map/reduce operation on the range [first1, last1) and the range beginning at first2. 
1) Initializes the accumulator acc with the initial value init and then modifies it with the expression acc = acc + *first1 * *first2, then modifies again with the expression acc = acc + *(first1+1) * *(first2+1), etc                       (until C++20)

modifies it with the expression acc = std::move(acc) + *first1 * *first2, then modifies again with the expression acc = std::move(acc) + *(first1+1) * *(first2+1), etc (since C++20) 
until reaching last1. For built-in meaning of + and *, this computes inner product of the two ranges. 
2) Initializes the accumulator acc with the initial value init and then modifies it with the expression acc = op1(acc, op2(*first1, *first2)), then modifies again with the expression acc = op1(acc, op2(*(first1+1), *(first2+1))), etc                       (until C++20)

modifies it with the expression acc = op1(std::move(acc), op2(*first1, *first2)), then modifies again with the expression acc = op1(std::move(acc), op2(*(first1+1), *(first2+1))), etc (since C++20) 
until reaching last1. 
op1 or op2 must not have side effects. <i>(until C++11)</i> 
op1 or op2 must not invalidate any iterators, including the end iterators, or modify any elements of the range involved. <i>(since C++11)</i> 

<h2>Parameters</h2>

first1, last1 - the first range of elements 
first2 - the beginning of the second range of elements 
init - initial value of the sum of the products 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary operation function object that will be applied. This &quot;sum&quot; function takes a value returned by op2 and the current value of the accumulator and produces a new value to be stored in the accumulator. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
op1 - Ret fun(const Type1 &amp;a, const Type2 &amp;b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that objects of types T and Type3 can be implicitly converted to Type1 and Type2 respectively. The type Ret must be such that an object of type T can be assigned a value of type Ret. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary operation function object that will be applied. This &quot;product&quot; function takes one value from each range and produces a new value. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
op2 - Ret fun(const Type1 &amp;a, const Type2 &amp;b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that objects of types InputIt1 and InputIt2 can be dereferenced and then implicitly converted to Type1 and Type2 respectively. The type Ret must be such that an object of type Type3 can be assigned a value of type Ret.

<h2>Type requirements</h2>

- 
InputIt1, InputIt2 must meet the requirements of LegacyInputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
T must meet the requirements of CopyAssignable and CopyConstructible.

<h2>Return value</h2>

The final value of acc as described above. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, class T&gt; 
&nbsp;<wbr>&nbsp;T inner_product(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, T init) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;init = std::move(init) + *first1 * *first2; // std::move since C++20 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return init; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class T, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class BinaryOperation1, class BinaryOperation2&gt; 
&nbsp;<wbr>&nbsp;T inner_product(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, T init, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BinaryOperation1 op1 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BinaryOperation2 op2) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;init = op1(std::move(init), op2(*first1, *first2)); // std::move since C++20 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return init; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

The parallelizable version of this algorithm, std::transform_reduce, requires op1 and op2 to be commutative and associative, but std::inner_product makes no such requirement, and always performs the operations in the order given. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;numeric&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;functional&gt;

int main()

{
    std::vector&lt;int&gt; a{0, 1, 2, 3, 4};
    std::vector&lt;int&gt; b{5, 4, 2, 3, 1};
    int r1 = std::inner_product(a.begin(), a.end(), b.begin(), 0);
    std::cout &lt;&lt; &quot;Inner product of a and b: &quot; &lt;&lt; r1 &lt;&lt; '\n';
    int r2 = std::inner_product(a.begin(), a.end(), b.begin(), 0,
                                std::plus&lt;&gt;(), std::equal_to&lt;&gt;());
    std::cout &lt;&lt; &quot;Number of pairwise matches between a and b: &quot; &lt;&lt; r2 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Inner product of a and b: 21 
&nbsp;<wbr>&nbsp;Number of pairwise matches between a and b: 2

<h2>See also</h2>

transform_reduce applies a functor, then reduces out of order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the partial sum of a range of elements 
partial_sum <i>(function template)</i> 
