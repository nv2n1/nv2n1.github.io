---
title: "stdadvance(3)"
name: "stdadvance"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdadvance/"
---

std::advance - std::advance

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iterator&gt;

    template &lt;class InputIt, class Distance&gt;
    (until C++ 17)

        void advance(InputIt &amp;it, Distance n);

template &lt;class InputIt, class Distance&gt;
(since C++ 17)

    constexpr void advance(InputIt &amp;it, Distance n);</code></pre> 
Increments given iterator it by n elements. 
If n is negative, the iterator is decremented. In this case, InputIt must meet the requirements of LegacyBidirectionalIterator, otherwise the behavior is undefined. 

<h2>Parameters</h2>

it - iterator to be advanced 
n - number of elements it should be advanced

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Linear. 
However, if InputIt additionally meets the requirements of LegacyRandomAccessIterator, complexity is constant.

<h2>Notes</h2>

The behavior is undefined if the specified sequence of increments or decrements would require that a non-incrementable iterator (such as the past-the-end iterator) is incremented, or that a non-decrementable iterator (such as the front iterator or the singular iterator) is decremented. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4};
    auto vi = v.begin();
    std::advance(vi, 2);
    std::cout &lt;&lt; *vi &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4

<h2>See also</h2>

next increment an iterator 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between two iterators 
distance <i>(function template)</i> 
