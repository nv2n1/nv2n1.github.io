---
title: "stdis_permutation(3)"
name: "stdis_permutation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_permutation/"
---

std::is_permutation - std::is_permutation

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt1, class ForwardIt2 &gt;                                (since C++11)

bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                     (until C++20)

ForwardIt2 first2 );

template&lt; class ForwardIt1, class ForwardIt2 &gt;

constexpr bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,           (since C++20)

ForwardIt2 first2 );

template&lt; class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;                        (since C++11)

bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                                    (until C++20)

ForwardIt2 first2, BinaryPredicate p );

template&lt; class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

constexpr bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                          (since C++20)

ForwardIt2 first2, BinaryPredicate p );

template&lt; class ForwardIt1, class ForwardIt2 &gt;                        (1)                                   (since C++14)

bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                                                   (until C++20)

ForwardIt2 first2, ForwardIt2 last2 );

template&lt; class ForwardIt1, class ForwardIt2 &gt;                            (2)

constexpr bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                                         (since C++20)

ForwardIt2 first2, ForwardIt2 last2 );

template&lt; class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;         (3)

bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                                                                  (since C++14)

ForwardIt2 first2, ForwardIt2 last2,                                                                                       (until C++20)

BinaryPredicate p );                                                                         (4)

template&lt; class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

constexpr bool is_permutation( ForwardIt1 first1, ForwardIt1 last1,                                                        (since C++20)

ForwardIt2 first2, ForwardIt2 last2,

BinaryPredicate p );</code></pre> 
Returns true if there exists a permutation of the elements in the range [first1, last1) that makes that range equal to the range [first2,last2), where last2 denotes first2 + (last1 - first1) if it was not given. 
1,3) Elements are compared using operator==. The behavior is undefined if it is not an equivalence_relation. 
2,4) Elements are compared using the given binary predicate p. The behavior is undefined if it is not an equivalence relation. 

<h2>Parameters</h2>

first1, last1 - the range of elements to compare 
first2, last2 - the second range to compare 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the elements should be treated as equal. 
p - The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type &amp;a, const Type &amp;b); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Type should be the value type of both ForwardIt1 and ForwardIt2. The signature does not need to have const &amp;, but the function must not modify the objects passed to it.

<h2>Type requirements</h2>

- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
ForwardIt1, ForwardIt2 must have the same value type.

<h2>Return value</h2>

true if the range [first1, last1) is a permutation of the range [first2, last2). 

<h2>Complexity</h2>

At most O(N2) applications of the predicate, or exactly N if the sequences are already equal, where N=std::distance(first1, last1). 
However if ForwardIt1 and ForwardIt2 meet the requirements of LegacyRandomAccessIterator and std::distance(first1, last1) != std::distance(first2, last2) no applications of the predicate are made.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt1, class ForwardIt2&gt; 
&nbsp;<wbr>&nbsp;bool is_permutation(ForwardIt1 first, ForwardIt1 last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt2 d_first) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// skip common prefix 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::tie(first, d_first) = std::mismatch(first, last, d_first); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// iterate over the rest, counting how many times each element 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// from [first, last) appears in [d_first, d_last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt2 d_last = d_first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::advance(d_last, std::distance(first, last)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (ForwardIt1 i = first; i != last; ++i) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (i != std::find(first, i, *i)) continue; // already counted this *i 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto m = std::count(d_first, d_last, *i); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (m==0 || std::count(i, last, *i) != m) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return true; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

int main()

{
    std::vector&lt;int&gt; v1{1, 2, 3, 4, 5};
    std::vector&lt;int&gt; v2{3, 5, 4, 1, 2};
    std::cout &lt;&lt; &quot;3,5,4,1,2 is a permutation of 1,2,3,4,5? &quot;
              &lt;&lt; std::boolalpha
              &lt;&lt; std::is_permutation(v1.begin(), v1.end(), v2.begin()) &lt;&lt; '\n';
    std::vector&lt;int&gt; v3{3, 5, 4, 1, 1};
    std::cout &lt;&lt; &quot;3,5,4,1,1 is a permutation of 1,2,3,4,5? &quot;
              &lt;&lt; std::boolalpha
              &lt;&lt; std::is_permutation(v1.begin(), v1.end(), v3.begin()) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3,5,4,1,2 is a permutation of 1,2,3,4,5? true 
&nbsp;<wbr>&nbsp;3,5,4,1,1 is a permutation of 1,2,3,4,5? false

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next greater lexicographic permutation of a range of elements 
next_permutation <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next smaller lexicographic permutation of a range of elements 
prev_permutation <i>(function template)</i> 
