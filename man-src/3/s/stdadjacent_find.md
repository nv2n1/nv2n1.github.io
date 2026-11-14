---
title: "stdadjacent_find(3)"
name: "stdadjacent_find"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdadjacent_find/"
---

std::adjacent_find - std::adjacent_find

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt &gt;                                                                      (until C++20)

ForwardIt adjacent_find( ForwardIt first, ForwardIt last );

template&lt; class ForwardIt &gt;                                                                      (since C++20)

constexpr ForwardIt adjacent_find( ForwardIt first, ForwardIt last );

template&lt; class ExecutionPolicy, class ForwardIt &gt;

ForwardIt adjacent_find( ExecutionPolicy&amp;&amp; policy,                                           (2) (since C++17)

ForwardIt first, ForwardIt last );                                                       (1)

template&lt; class ForwardIt, class BinaryPredicate&gt;                                                              (until C++20)

ForwardIt adjacent_find( ForwardIt first, ForwardIt last, BinaryPredicate p );

template&lt; class ForwardIt, class BinaryPredicate&gt;                                                              (since C++20)

constexpr ForwardIt adjacent_find( ForwardIt first, ForwardIt last, BinaryPredicate p );     (3)

template&lt; class ExecutionPolicy, class ForwardIt, class BinaryPredicate&gt;

ForwardIt adjacent_find( ExecutionPolicy&amp;&amp; policy,                                               (4)           (since C++17)

ForwardIt first, ForwardIt last, BinaryPredicate p );</code></pre> 
Searches the range [first, last) for two consecutive identical elements. 
1) Elements are compared using operator==. 
3) Elements are compared using the given binary predicate p. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the elements should be treated as equal. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
p - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type ForwardIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

an iterator to the first of the first pair of identical elements, that is, the first iterator it such that *it == *(it+1) for the first version or p(*it, *(it + 1)) != false for the second version. 
If no such elements are found, last is returned 

<h2>Complexity</h2>

1,3) Exactly min((result-first)+1, (last-first)-1) applications of the predicate where result is the return value. 
2,4) O(last-first) applications of the corresponding predicate.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt; 
&nbsp;<wbr>&nbsp;ForwardIt adjacent_find(ForwardIt first, ForwardIt last) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt next = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++next; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; next != last; ++next, ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*first == *next) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class BinaryPredicate&gt; 
&nbsp;<wbr>&nbsp;ForwardIt adjacent_find(ForwardIt first, ForwardIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BinaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first == last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt next = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++next; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; next != last; ++next, ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (p(*first, *next)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;functional&gt;
int main()

{
    std::vector&lt;int&gt; v1{0, 1, 2, 3, 40, 40, 41, 41, 5};
    auto i1 = std::adjacent_find(v1.begin(), v1.end());
    if (i1 == v1.end()) {
        std::cout &lt;&lt; &quot;no matching adjacent elements\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;the first adjacent pair of equal elements at: &quot;
                  &lt;&lt; std::distance(v1.begin(), i1) &lt;&lt; '\n';
    }
    auto i2 = std::adjacent_find(v1.begin(), v1.end(), std::greater&lt;int&gt;());
    if (i2 == v1.end()) {
        std::cout &lt;&lt; &quot;The entire vector is sorted in ascending order\n&quot;;
    } else {
        std::cout &lt;&lt; &quot;The last element in the non-decreasing subsequence is at: &quot;
                  &lt;&lt; std::distance(v1.begin(), i2) &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The first adjacent pair of equal elements at: 4 
&nbsp;<wbr>&nbsp;The last element in the non-decreasing subsequence is at: 7

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes consecutive duplicate elements in a range 
unique <i>(function template)</i> 
