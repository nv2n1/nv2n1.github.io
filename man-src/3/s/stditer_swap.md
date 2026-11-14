---
title: "stditer_swap(3)"
name: "stditer_swap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stditer_swap/"
---

std::iter_swap - std::iter_swap

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt1, class ForwardIt2&gt;
    (until C++ 20)

        void iter_swap(ForwardIt1 a, ForwardIt2 b);

template &lt;class ForwardIt1, class ForwardIt2&gt;
(since C++ 20)

    constexpr void iter_swap(ForwardIt1 a, ForwardIt2 b);</code></pre> 
Swaps the values of the elements the given iterators are pointing to. 

<h2>Parameters</h2>

a, b - iterators to the elements to swap

<h2>Type requirements</h2>

- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
*a, *b must meet the requirements of Swappable.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

constant

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt1, class ForwardIt2&gt; 
&nbsp;<wbr>&nbsp;constexpr void iter_swap(ForwardIt1 a, ForwardIt2 b) // constexpr since C++20 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using std::swap; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap(*a, *b); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following is an implementation of selection sort in C++ 
 // Run this code <pre><code>#include &lt;random&gt;

#include &lt;vector&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;functional&gt;
template &lt;class ForwardIt&gt;

void selection_sort(ForwardIt begin, ForwardIt end)

{
    for (ForwardIt i = begin; i != end; ++i)
        std::iter_swap(i, std::min_element(i, end));
}
int main()

{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution&lt;&gt; dist(-10, 10);
    std::vector&lt;int&gt; v;
    generate_n(back_inserter(v), 20, bind(dist, gen));
    std::cout &lt;&lt; &quot;Before sort: &quot;;
    for (auto e : v)
        std::cout &lt;&lt; e &lt;&lt; &quot; &quot;;
    selection_sort(v.begin(), v.end());
    std::cout &lt;&lt; &quot;\nAfter sort: &quot;;
    for (auto e : v)
        std::cout &lt;&lt; e &lt;&lt; &quot; &quot;;
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Before sort: -7 6 2 4 -1 6 -9 -1 2 -5 10 -9 -5 -3 -5 -3 6 6 1 8 
&nbsp;<wbr>&nbsp;After sort: -9 -9 -7 -5 -5 -5 -3 -3 -1 -1 1 2 2 4 6 6 6 6 8 10

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two ranges of elements 
swap_ranges <i>(function template)</i> 
