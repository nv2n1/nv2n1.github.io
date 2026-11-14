---
title: "stdsort_heap(3)"
name: "stdsort_heap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsort_heap/"
---

std::sort_heap - std::sort_heap

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (until C++ 20)

        void sort_heap(RandomIt first, RandomIt last);

template &lt;class RandomIt&gt;
(since C++ 20)

    constexpr void sort_heap(RandomIt first, RandomIt last);
(1)

    template &lt;class RandomIt, class Compare&gt;
    (until C++ 20)

        void sort_heap(RandomIt first, RandomIt last, Compare comp);
(2)

    template &lt;class RandomIt, class Compare&gt;
    (since C++ 20)

        constexpr void sort_heap(RandomIt first, RandomIt last, Compare comp);</code></pre> 
Converts the max heap [first, last) into a sorted range in ascending order. The resulting range no longer has the heap property. 
The first version of the function uses operator&lt; to compare the elements, the second uses the given comparison function comp. 

<h2>Parameters</h2>

first, last - the range of elements to sort 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type RandomIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of ValueSwappable and LegacyRandomAccessIterator. 
- 
The type of dereferenced RandomIt must meet the requirements of MoveAssignable and MoveConstructible.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

At most 2×N×log(N) comparisons where N=std::distance(first, last).

<h2>Notes</h2>

A max heap is a range of elements [f,l) that has the following properties: 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2444 C++98 complexity requirement was wrong by a factor of 2 corrected 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; class RandomIt &gt; 
&nbsp;<wbr>&nbsp;void sort_heap( RandomIt first, RandomIt last ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::pop_heap(first, last--); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt; class RandomIt, class Compare &gt; 
&nbsp;<wbr>&nbsp;void sort_heap( RandomIt first, RandomIt last, Compare comp ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::pop_heap(first, last--, comp); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; v = {3, 1, 4, 1, 5, 9};
    std::make_heap(v.begin(), v.end());
    std::cout &lt;&lt; &quot;heap:\t&quot;;
    for (const auto &amp;i : v) {
        std::cout &lt;&lt; i &lt;&lt; ' ';
    }
    std::sort_heap(v.begin(), v.end());
    std::cout &lt;&lt; &quot;\nsorted:\t&quot;;
    for (const auto &amp;i : v) {
        std::cout &lt;&lt; i &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;heap: 9 4 5 1 1 3 
&nbsp;<wbr>&nbsp;sorted: 1 1 3 4 5 9

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a max heap out of a range of elements 
make_heap <i>(function template)</i> 
