---
title: "stdis_sorted_until(3)"
name: "stdis_sorted_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_sorted_until/"
---

std::is_sorted_until - std::is_sorted_until

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt &gt;                                                                     (since C++11)

ForwardIt is_sorted_until( ForwardIt first, ForwardIt last );                                   (until C++20)

template&lt; class ForwardIt &gt;                                                                     (since C++20)

constexpr ForwardIt is_sorted_until( ForwardIt first, ForwardIt last );

template&lt; class ExecutionPolicy, class ForwardIt &gt;                                          (2) (since C++17)

ForwardIt is_sorted_until( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last );

template&lt; class ForwardIt, class Compare &gt;                                                                     (since C++11)

ForwardIt is_sorted_until( ForwardIt first, ForwardIt last,                             (1)                    (until C++20)

Compare comp );

template&lt; class ForwardIt, class Compare &gt;

constexpr ForwardIt is_sorted_until( ForwardIt first, ForwardIt last,                       (3)                (since C++20)

Compare comp );

template&lt; class ExecutionPolicy, class ForwardIt, class Compare &gt;

ForwardIt is_sorted_until( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last,           (4)            (since C++17)

Compare comp );</code></pre> 
Examines the range [first, last) and finds the largest range beginning at first in which the elements are sorted in ascending order. 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given binary comparison function comp. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type ForwardIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

The upper bound of the largest range beginning at first in which the elements are sorted in ascending order. That is, the last iterator it for which range [first, it) is sorted. 

<h2>Complexity</h2>

linear in the distance between first and last

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt; 
&nbsp;<wbr>&nbsp;ForwardIt is_sorted_until(ForwardIt first, ForwardIt last) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return is_sorted_until(first, last, std::less&lt;&gt;()); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template &lt;class ForwardIt, class Compare&gt; 
&nbsp;<wbr>&nbsp;ForwardIt is_sorted_until(ForwardIt first, ForwardIt last, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt next = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (++next != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (comp(*next, *first)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return next; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = next; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

std::is_sorted and std::is_sorted_until both return true for empty ranges and ranges of length one. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;

#include &lt;random&gt;
int main()

{
    std::random_device rd;
    std::mt19937 g(rd());
    const int N = 6;
    int nums[N] = {3, 1, 4, 1, 5, 9};
    const int min_sorted_size = 4;
    int sorted_size = 0;
    do {
        std::shuffle(nums, nums + N, g);
        int *sorted_end = std::is_sorted_until(nums, nums + N);
        sorted_size = std::distance(nums, sorted_end);
        for (auto i : nums)
            std::cout &lt;&lt; i &lt;&lt; ' ';
        std::cout &lt;&lt; &quot; : &quot; &lt;&lt; sorted_size &lt;&lt; &quot; initial sorted elements\n&quot;;
    } while (sorted_size &lt; min_sorted_size);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;4 1 9 5 1 3 : 1 initial sorted elements 
&nbsp;<wbr>&nbsp;4 5 9 3 1 1 : 3 initial sorted elements 
&nbsp;<wbr>&nbsp;9 3 1 4 5 1 : 1 initial sorted elements 
&nbsp;<wbr>&nbsp;1 3 5 4 1 9 : 3 initial sorted elements 
&nbsp;<wbr>&nbsp;5 9 1 1 3 4 : 2 initial sorted elements 
&nbsp;<wbr>&nbsp;4 9 1 5 1 3 : 2 initial sorted elements 
&nbsp;<wbr>&nbsp;1 1 4 9 5 3 : 4 initial sorted elements

<h2>See also</h2>

is_sorted checks whether a range is sorted into ascending order 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
