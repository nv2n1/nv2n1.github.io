---
title: "stdrangesviewcounted(3)"
name: "stdrangesviewcounted"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrangesviewcounted/"
---

std::ranges::view::counted - std::ranges::view::counted

<h2>Synopsis</h2>

<pre><code>namespace view {

    inline constexpr /*unspecified*/ counted = /*unspecified*/;  (since C++20)

}</code></pre> 
A counted view presents a View of the elements of the counted range [i, n) for some iterator i and non-negative integer n. 
A counted range [i, n) is the n elements starting with the element pointed to by i and up to but not including the element, if any, pointed to by the result of n applications of ++i. 
If n == 0, the counted range is valid and empty. Otherwise, the counted range is only valid if n is positive, i is dereferenceable, and [++i, --n) is a valid counted range. 
Formally, if E and F are expressions, and T is the type std::decay_t&lt;decltype((E))&gt;, then 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if T models Iterator and decltype((F)) models ConvertibleTo&lt;iter_difference_t&lt;T&gt;&gt;, if T
    models RandomAccessIterator, view::counted(E, F) is expression - equivalent to ranges::subrange{E, E + static_cast&lt;std::iter_difference_t&lt;T&gt;&gt;(F)} otherwise view::counted(E, F) is expression - equivalent to ranges::subrange
    {
        std::counted_iterator{E, F}, std::default_sentinel
    } 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;otherwise, view::counted(E, F) is ill-formed. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;ranges&gt;

#include &lt;iostream&gt;
int main()

{
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (int i : std::view::counted(a, 3))
        std::cout &lt;&lt; i &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;combines an iterator-sentinel pair into a View 
subrange <i>(class template)</i> 
counted_iterator iterator adaptor that tracks the distance to the end of the range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(C++20) 
