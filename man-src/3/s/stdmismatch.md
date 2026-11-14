---
title: "stdmismatch(3)"
name: "stdmismatch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmismatch/"
---

std::mismatch - std::mismatch

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt1, class InputIt2 &gt;

std::pair&lt;InputIt1,InputIt2&gt;                                                                         (until C++20)

mismatch( InputIt1 first1, InputIt1 last1,

InputIt2 first2 );

template&lt; class InputIt1, class InputIt2 &gt;

constexpr std::pair&lt;InputIt1,InputIt2&gt;                                                               (since C++20)

mismatch( InputIt1 first1, InputIt1 last1,

InputIt2 first2 );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

std::pair&lt;ForwardIt1,ForwardIt2&gt;                                                                 (2) (since C++17)

mismatch( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,

ForwardIt2 first2 );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

std::pair&lt;InputIt1,InputIt2&gt;

mismatch( InputIt1 first1, InputIt1 last1,                                                                         (until C++20)

InputIt2 first2,

BinaryPredicate p );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

constexpr std::pair&lt;InputIt1,InputIt2&gt;

mismatch( InputIt1 first1, InputIt1 last1,                                                                         (since C++20)

InputIt2 first2,

BinaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

std::pair&lt;ForwardIt1,ForwardIt2&gt;

mismatch( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                             (4)           (since C++17)

ForwardIt2 first2,

BinaryPredicate p );                                                                         (1)

template&lt; class InputIt1, class InputIt2 &gt;

std::pair&lt;InputIt1,InputIt2&gt;                                                                                                     (since C++14)

mismatch( InputIt1 first1, InputIt1 last1,                                                                                       (until C++20)

InputIt2 first2, InputIt2 last2 );

template&lt; class InputIt1, class InputIt2 &gt;

constexpr std::pair&lt;InputIt1,InputIt2&gt;                                                           (3)                             (since C++20)

mismatch( InputIt1 first1, InputIt1 last1,

InputIt2 first2, InputIt2 last2 );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

std::pair&lt;ForwardIt1,ForwardIt2&gt;                                                                                   (6)           (since C++17)

mismatch( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,

ForwardIt2 first2, ForwardIt2 last2 );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

std::pair&lt;InputIt1,InputIt2&gt;                                                                         (5)                                        (since C++14)

mismatch( InputIt1 first1, InputIt1 last1,                                                                                                      (until C++20)

InputIt2 first2, InputIt2 last2,

BinaryPredicate p );

template&lt; class InputIt1, class InputIt2, class BinaryPredicate &gt;

constexpr std::pair&lt;InputIt1,InputIt2&gt;

mismatch( InputIt1 first1, InputIt1 last1,                                                                         (7)                          (since C++20)

InputIt2 first2, InputIt2 last2,

BinaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

std::pair&lt;ForwardIt1,ForwardIt2&gt;

mismatch( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                                                         (8)            (since C++17)

ForwardIt2 first2, ForwardIt2 last2,

BinaryPredicate p );</code></pre> 
Returns the first mismatching pair of elements from two ranges: one defined by [first1, last1) and another defined by [first2,last2). If last2 is not provided (overloads (1-4)), it denotes first2 + (last1 - first1). 
1,5) Elements are compared using operator==. 
3,7) Elements are compared using the given binary predicate p. 
2,4,6,8) Same as (1,3,5,7), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first1, last1 - the first range of the elements 
first2, last2 - the second range of the elements 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the elements should be treated as equal. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
p - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that objects of types InputIt1 and InputIt2 can be dereferenced and then implicitly converted to Type1 and Type2 respectively.

<h2>Type requirements</h2>

- 
InputIt1 must meet the requirements of LegacyInputIterator. 
- 
InputIt2 must meet the requirements of LegacyInputIterator. 
- 
ForwardIt1 must meet the requirements of LegacyForwardIterator. 
- 
ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
BinaryPredicate must meet the requirements of BinaryPredicate.

<h2>Return value</h2>

std::pair with iterators to the first two non-equal elements. 
If no mismatches are found when the comparison reaches last1, the pair holds last1 and the corresponding iterator from the second range. The behavior is undefined if the second range is shorter than the first range. <i>(until C++14)</i> 
If no mismatches are found when the comparison reaches last1 or last2, whichever happens first, the pair holds the end iterator and the corresponding iterator from the other range. <i>(since C++14)</i> 

<h2>Complexity</h2>

1-4) At most last1 - first1 applications of operator== or the predicate p 
5-8) At most min(last1 - first1, last2 - first2) applications of operator== or the predicate p.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;InputIt1, InputIt2&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1 &amp;&amp; *first1 == *first2) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1, ++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(first1, first2); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, class BinaryPredicate&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;InputIt1, InputIt2&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2, BinaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1 &amp;&amp; p(*first1, *first2)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1, ++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(first1, first2); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;InputIt1, InputIt2&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1 &amp;&amp; first2 != last2 &amp;&amp; *first1 == *first2) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1, ++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(first1, first2); 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, class BinaryPredicate&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;InputIt1, InputIt2&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2, BinaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first1 != last1 &amp;&amp; first2 != last2 &amp;&amp; p(*first1, *first2)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first1, ++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(first1, first2); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

This program determines the longest substring that is simultaneously found at the very beginning of the given string and at the very end of it, in reverse order (possibly overlapping) 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;algorithm&gt;
std::string mirror_ends(const std::string &amp;in)

{
    return std::string(in.begin(),
                       std::mismatch(in.begin(), in.end(), in.rbegin()).first);
}
int main()

{
    std::cout &lt;&lt; mirror_ends(&quot;abXYZba&quot;) &lt;&lt; '\n'
              &lt;&lt; mirror_ends(&quot;abca&quot;) &lt;&lt; '\n'
              &lt;&lt; mirror_ends(&quot;aba&quot;) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;ab 
&nbsp;<wbr>&nbsp;a 
&nbsp;<wbr>&nbsp;aba

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines if two sets of elements are the same 
equal <i>(function template)</i> 
find 
find_if 
find_if_not finds the first element satisfying specific criteria 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns true if one range is lexicographically less than another 
lexicographical_compare <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
