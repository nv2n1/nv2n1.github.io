---
title: "stdaccumulate(3)"
name: "stdaccumulate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdaccumulate/"
---

std::accumulate - std::accumulate

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class InputIt, class T &gt;                        (1)

T accumulate( InputIt first, InputIt last, T init );

template&lt; class InputIt, class T, class BinaryOperation &gt;

T accumulate( InputIt first, InputIt last, T init,        (2)

BinaryOperation op );</code></pre> 
Computes the sum of the given value init and the elements in the range [first, last). The first version uses operator+ to sum up the elements, the second version uses the given binary function op 
, both applying std::move to their operands on the left hand side 
<i>(since C++20)</i>. 
op must not have side effects. <i>(until C++11)</i> 
op must not invalidate any iterators, including the end iterators, nor modify any elements of the range involved, and also *last. <i>(since C++11)</i> 

<h2>Parameters</h2>

first, last - the range of elements to sum 
init - initial value of the sum 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary operation function object that will be applied. The binary operator takes the current accumulation value a (initialized to init) and the value of the current element b. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the function should be equivalent to the following: 
op - Ret fun(const Type1 &amp;a, const Type2 &amp;b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature does not need to have const &amp;. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type1 must be such that an object of type T can be implicitly converted to Type1. The type Type2 must be such that an object of type InputIt can be dereferenced and then implicitly converted to Type2. The type Ret must be such that an object of type T can be assigned a value of type Ret.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
T must meet the requirements of CopyAssignable and CopyConstructible.

<h2>Return value</h2>

1) The sum of the given value and elements in the given range. 
2) The result of left_fold of the given range over op 

<h2>Notes</h2>

std::accumulate performs a left fold. In order to perform a right fold, one must reverse the order of the arguments to the binary operator, and use reverse iterators. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class T&gt; 
&nbsp;<wbr>&nbsp;T accumulate(InputIt first, InputIt last, T init) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;init = std::move(init) + *first; // std::move since C++20 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return init; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class T, class BinaryOperation&gt; 
&nbsp;<wbr>&nbsp;T accumulate(InputIt first, InputIt last, T init, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BinaryOperation op) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;init = op(std::move(init), *first); // std::move since C++20 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return init; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;numeric&gt;

#include &lt;string&gt;

#include &lt;functional&gt;
int main()

{
    std::vector&lt;int&gt; v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int sum = std::accumulate(v.begin(), v.end(), 0);
    int product = std::accumulate(v.begin(), v.end(), 1, std::multiplies&lt;int&gt;());
    auto dash_fold = [](std::string a, int b) {
        return std::move(a) + '-' + std::to_string(b);
    };
    std::string s = std::accumulate(std::next(v.begin()), v.end(),
                                    std::to_string(v[0]), // start with first element
                                    dash_fold);
    // Right fold using reverse iterators
    std::string rs = std::accumulate(std::next(v.rbegin()), v.rend(),
                                     std::to_string(v.back()), // start with last element
                                     dash_fold);
    std::cout &lt;&lt; &quot;sum: &quot; &lt;&lt; sum &lt;&lt; '\n'
              &lt;&lt; &quot;product: &quot; &lt;&lt; product &lt;&lt; '\n'
              &lt;&lt; &quot;dash-separated string: &quot; &lt;&lt; s &lt;&lt; '\n'
              &lt;&lt; &quot;dash-separated string (right-folded): &quot; &lt;&lt; rs &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;sum: 55 
&nbsp;<wbr>&nbsp;product: 3628800 
&nbsp;<wbr>&nbsp;dash-separated string: 1-2-3-4-5-6-7-8-9-10 
&nbsp;<wbr>&nbsp;dash-separated string (right-folded): 10-9-8-7-6-5-4-3-2-1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the differences between adjacent elements in a range 
adjacent_difference <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the inner product of two ranges of elements 
inner_product <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the partial sum of a range of elements 
partial_sum <i>(function template)</i> 
reduce similar to std::accumulate, except out of order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
