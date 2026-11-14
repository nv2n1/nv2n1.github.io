---
title: "stdpush_heap(3)"
name: "stdpush_heap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpush_heap/"
---

std::push_heap - std::push_heap

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (until C++ 20)

        void push_heap(RandomIt first, RandomIt last);

template &lt;class RandomIt&gt;
(since C++ 20)

    constexpr void push_heap(RandomIt first, RandomIt last);

template &lt;class RandomIt, class Compare&gt;
(1)

    void push_heap(RandomIt first, RandomIt last, (until C++ 20)

                                                      Compare comp);
(2)

    template &lt;class RandomIt, class Compare&gt;

    constexpr void push_heap(RandomIt first, RandomIt last, (since C++ 20)

                                                                Compare comp);</code></pre> 
Inserts the element at the position last-1 into the max heap defined by the range [first, last-1). The first version of the function uses operator&lt; to compare the elements, the second uses the given comparison function comp. 

<h2>Parameters</h2>

first, last - the range of elements defining the heap to modify 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type RandomIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of LegacyRandomAccessIterator. 
- 
The type of dereferenced RandomIt must meet the requirements of MoveAssignable and MoveConstructible.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

At most log(N) comparisons where N=std::distance(first, last).

<h2>Notes</h2>

A max heap is a range of elements [f,l) that has the following properties: 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4, 1, 5, 9};
    std::make_heap(v.begin(), v.end());
    std::cout &lt;&lt; &quot;v: &quot;;
    for (auto i : v)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    v.push_back(6);
    std::cout &lt;&lt; &quot;before push_heap: &quot;;
    for (auto i : v)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    std::push_heap(v.begin(), v.end());
    std::cout &lt;&lt; &quot;after push_heap: &quot;;
    for (auto i : v)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;v: 9 5 4 1 1 3 
&nbsp;<wbr>&nbsp;before push_heap: 9 5 4 1 1 3 6 
&nbsp;<wbr>&nbsp;after push_heap: 9 5 6 1 1 3 4

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes the largest element from a max heap 
pop_heap <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a max heap out of a range of elements 
make_heap <i>(function template)</i> 
