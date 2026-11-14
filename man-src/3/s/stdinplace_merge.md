---
title: "stdinplace_merge(3)"
name: "stdinplace_merge"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinplace_merge/"
---

std::inplace_merge - std::inplace_merge

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class BidirIt&gt;
    (1)

        void inplace_merge(BidirIt first, BidirIt middle, BidirIt last);

template &lt;class ExecutionPolicy, class BidirIt&gt;
(2)(since C++ 17)

    void inplace_merge(ExecutionPolicy &amp;&amp;policy, BidirIt first, BidirIt middle, BidirIt last);

template &lt;class BidirIt, class Compare&gt;
(3)

    void inplace_merge(BidirIt first, BidirIt middle, BidirIt last, Compare comp);

template &lt;class ExecutionPolicy, class BidirIt, class Compare&gt;
(4)(since C++ 17)

    void inplace_merge(ExecutionPolicy &amp;&amp;policy, BidirIt first, BidirIt middle, BidirIt last, Compare comp);</code></pre> 
Merges two consecutive sorted ranges [first, middle) and [middle, last) into one sorted range [first, last). For equivalent elements in the original two ranges, the elements from the first range (preserving their original order) precede the elements from the second range (preserving their original order). 
1) Elements are compared using operator&lt; and the ranges must be sorted with respect to the same. 
3) Elements are compared using the given binary comparison function comp and the ranges must be sorted with respect to the same. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first - the beginning of the first sorted range 
middle - the end of the first sorted range and the beginning of the second 
last - the end of the second sorted range 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type BidirIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of ValueSwappable and LegacyBidirectionalIterator. 
- 
The type of dereferenced BidirIt must meet the requirements of MoveAssignable and MoveConstructible.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Given N = std::distance(first, last)}, 
1,3) Exactly N-1 comparisons if enough additional memory is available. If the memory is insufficient, O(N log N) comparisons. 
2,4) O(N log N) comparisons.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

This function attempts to allocate a temporary buffer. If the allocation fails, the less efficient algorithm is chosen. 

<h2>Example</h2>

The following code is an implementation of merge sort. 
 // Run this code <pre><code>#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;
template &lt;class Iter&gt;

void merge_sort(Iter first, Iter last)

{
    if (last - first &gt; 1) {
        Iter middle = first + (last - first) / 2;
        merge_sort(first, middle);
        merge_sort(middle, last);
        std::inplace_merge(first, middle, last);
    }
}
int main()

{
    std::vector&lt;int&gt; v{8, 2, -2, 0, 11, 11, 1, 7, 3};
    merge_sort(v.begin(), v.end());
    for (auto n : v) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;-2 0 1 2 3 7 8 11 11

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;merges two sorted ranges 
merge <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order 
sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range of elements while preserving order between equal elements 
stable_sort <i>(function template)</i> 
