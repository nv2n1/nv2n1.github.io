---
title: "stdequal_range(3)"
name: "stdequal_range"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdequal_range/"
---

std::equal_range - std::equal_range

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt, class T&gt;

    std::pair&lt;ForwardIt, ForwardIt&gt;(until C++ 20)

        equal_range(ForwardIt first, ForwardIt last,

                    const T &amp;value);

template &lt;class ForwardIt, class T&gt;

constexpr std::pair&lt;ForwardIt, ForwardIt&gt;(since C++ 20)

    equal_range(ForwardIt first, ForwardIt last,

                const T &amp;value);
(1)

    template &lt;class ForwardIt, class T, class Compare&gt;

    std::pair&lt;ForwardIt, ForwardIt&gt;(until C++ 20)

        equal_range(ForwardIt first, ForwardIt last,

                    const T &amp;value, Compare comp);
(2)

    template &lt;class ForwardIt, class T, class Compare&gt;

    constexpr std::pair&lt;ForwardIt, ForwardIt&gt;(since C++ 20)

        equal_range(ForwardIt first, ForwardIt last,

                    const T &amp;value, Compare comp);</code></pre> 
Returns a range containing all elements equivalent to value in the range [first, last). 
The range [first, last) must be at least partially ordered with respect to value, i.e. it must satisfy all of the following requirements: 
* partitioned with respect to element &lt; value or comp(element, value) (that is, all elements for which the expression is true precedes all elements for which the expression is false) 
* partitioned with respect to !(value &lt; element) or !comp(value, element) 
* for all elements, if element &lt; value or comp(element, value) is true then !(value &lt; element) or !comp(value, element) is also true 
A fully-sorted range meets these criteria. 
The returned range is defined by two iterators, one pointing to the first element that is not less than value and another pointing to the first element greater than value. The first iterator may be alternatively obtained with std::lower_bound(), the second - with std::upper_bound(). 
The first version uses operator&lt; to compare the elements, the second version uses the given comparison function comp. 

<h2>Parameters</h2>

first, last - the range of elements to examine 
value - value to compare the elements to 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type T can be implicitly converted to both Type1 and Type2, and an object of type ForwardIt can be dereferenced and then implicitly converted to both Type1 and Type2.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
Compare must meet the requirements of BinaryPredicate. it is not required to satisfy Compare

<h2>Return value</h2>

std::pair containing a pair of iterators defining the wanted range, the first pointing to the first element that is not less than value and the second pointing to the first element greater than value. 
If there are no elements not less than value, last is returned as the first element. Similarly if there are no elements greater than value, last is returned as the second element 

<h2>Complexity</h2>

The number of comparisons performed is logarithmic in the distance between first and last (At most 2 * log 
2(last - first) + <a HREF="/docs/linux/man/1-o/">O</a>(1) comparisons). However, for non-LegacyRandomAccessIterators, the number of iterator increments is linear.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;ForwardIt,ForwardIt&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;equal_range(ForwardIt first, ForwardIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(std::lower_bound(first, last, value), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::upper_bound(first, last, value)); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T, class Compare&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;ForwardIt,ForwardIt&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;equal_range(ForwardIt first, ForwardIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const T&amp; value, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(std::lower_bound(first, last, value, comp), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::upper_bound(first, last, value, comp)); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
struct S

{
    int number;
    char name;
    // note: name is ignored by this comparison operator
    bool operator&lt;(const S &amp;s) const
    {
        return number &lt; s.number;
    }
};
int main()

{
    // note: not ordered, only partitioned w.r.t. S defined below
    std::vector&lt;S&gt; vec = &#123;&#123;1, 'A'}, {2, 'B'}, {2, 'C'}, {2, 'D'}, {4, 'G'}, {3, 'F'}};
    S value = {2, '?'};
    auto p = std::equal_range(vec.begin(), vec.end(), value);
    for (auto i = p.first; i != p.second; ++i)
        std::cout &lt;&lt; i-&gt;name &lt;&lt; ' ';

    // heterogeneous comparison:
    struct Comp {
        bool operator()(const S &amp;s, int i) const
        {
            return s.number &lt; i;
        }
        bool operator()(int i, const S &amp;s) const
        {
            return i &lt; s.number;
        }
    };
    auto p2 = std::equal_range(vec.begin(), vec.end(), 2, Comp{});
    for (auto i = p2.first; i != p2.second; ++i)
        std::cout &lt;&lt; i-&gt;name &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;B C D B C D 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_270 C++98 Compare was required to be a strict weak ordering only a partitioning is needed; heterogeneous comparisons permitted

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an iterator to the first element not less than the given value 
lower_bound <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an iterator to the first element greater than a certain value 
upper_bound <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines if an element exists in a certain range 
binary_search <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;divides a range of elements into two groups 
partition <i>(function template)</i> 
