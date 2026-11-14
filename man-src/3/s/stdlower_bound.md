---
title: "stdlower_bound(3)"
name: "stdlower_bound"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlower_bound/"
---

std::lower_bound - std::lower_bound

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt, class T&gt;
    (until C++ 20)

        ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class ForwardIt, class T&gt;
(since C++ 20)

    constexpr ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T &amp;value);
(1)

    template &lt;class ForwardIt, class T, class Compare&gt;
    (until C++ 20)

        ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T &amp;value, Compare comp);
(2)

    template &lt;class ForwardIt, class T, class Compare&gt;
    (since C++ 20)

        constexpr ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T &amp;value, Compare comp);</code></pre> 
Returns an iterator pointing to the first element in the range [first, last) that is not less than (i.e. greater or equal to) value, or last if no such element is found. 
The range [first, last) must be partitioned with respect to the expression element &lt; value or comp(element, value), i.e., all elements for which the expression is true must precede all elements for which the expression is false. A fully-sorted range meets this criterion. 
The first version uses operator&lt; to compare the elements, the second version uses the given comparison function comp. 

<h2>Parameters</h2>

first, last - iterators defining the partially-ordered range to examine 
value - value to compare the elements to 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The type Type1 must be such that an object of type ForwardIt can be dereferenced and then implicitly converted to Type1. The type Type2 must be such that an object of type T can be implicitly converted to Type2.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
Compare must meet the requirements of BinaryPredicate. it is not required to satisfy Compare

<h2>Return value</h2>

Iterator pointing to the first element that is not less than value, or last if no such element is found. 

<h2>Complexity</h2>

The number of comparisons performed is logarithmic in the distance between first and last (At most log 
2(last - first) + <a HREF="/docs/linux/man/1-o/">O</a>(1) comparisons). However, for non-LegacyRandomAccessIterators, the number of iterator increments is linear.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T&gt; 
&nbsp;<wbr>&nbsp;ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt it; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;ForwardIt&gt;::difference_type count, step; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count = std::distance(first, last); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (count &gt; 0) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;it = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;step = count / 2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::advance(it, step); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*it &lt; value) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = ++it; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count -= step + 1; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count = step; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T, class Compare&gt; 
&nbsp;<wbr>&nbsp;ForwardIt lower_bound(ForwardIt first, ForwardIt last, const T&amp; value, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ForwardIt it; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;ForwardIt&gt;::difference_type count, step; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count = std::distance(first, last); 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (count &gt; 0) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;it = first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;step = count / 2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::advance(it, step); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (comp(*it, value)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = ++it; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count -= step + 1; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count = step; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;
template &lt;class ForwardIt, class T, class Compare = std::less&lt;&gt;&gt;

ForwardIt binary_find(ForwardIt first, ForwardIt last, const T &amp;value, Compare comp = {})

{
    // Note: BOTH type T and the type after ForwardIt is dereferenced
    // must be implicitly convertible to BOTH Type1 and Type2, used in Compare.
    // This is stricter than lower_bound requirement (see above)
    first = std::lower_bound(first, last, value, comp);
    return first != last &amp;&amp; !comp(value, *first) ? first : last;
}
int main()

{
    std::vector&lt;int&gt; data = {1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6};
    auto lower = std::lower_bound(data.begin(), data.end(), 4);
    auto upper = std::upper_bound(data.begin(), data.end(), 4);
    std::copy(lower, upper, std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
    // classic binary search, returning a value only if it is present
    data = {1, 2, 4, 6, 9, 10};
    auto it = binary_find(data.cbegin(), data.cend(), 4); //&lt; choosing '5' will return end()
    if (it != data.cend())
        std::cout &lt;&lt; *it &lt;&lt; &quot; found at index &quot; &lt;&lt; std::distance(data.cbegin(), it);
    return 0;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4 4 4 
&nbsp;<wbr>&nbsp;4 found at index 2 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_270 C++98 Compare was required to be a strict weak ordering only a partitioning is needed; heterogeneous comparisons permitted

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns range of elements matching a specific key 
equal_range <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides a range of elements into two groups 
partition <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an iterator to the first element greater than a certain value 
upper_bound <i>(function template)</i> 
