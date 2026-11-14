---
title: "stdprev(3)"
name: "stdprev"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdprev/"
---

std::prev - std::prev

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class BidirIt &gt;

BidirIt prev(                                                     (since C++11)

BidirIt it,                                                       (until C++17)

typename std::iterator_traits&lt;BidirIt&gt;::difference_type n = 1 );

template&lt; class BidirIt &gt;

constexpr BidirIt prev(                                           (since C++17)

BidirIt it,

typename std::iterator_traits&lt;BidirIt&gt;::difference_type n = 1 );</code></pre> 
Return the nth predecessor of iterator it. 

<h2>Parameters</h2>

it - an iterator 
n - number of elements it should be descended

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of LegacyBidirectionalIterator.

<h2>Return value</h2>

The nth predecessor of iterator it. 

<h2>Complexity</h2>

Linear. 
However, if BidirIt additionally meets the requirements of LegacyRandomAccessIterator, complexity is constant.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class BidirIt&gt; 
&nbsp;<wbr>&nbsp;BidirIt prev(BidirIt it, typename std::iterator_traits&lt;BidirIt&gt;::difference_type n = 1) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::advance(it, -n); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return it; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

Although the expression --c.end() often compiles, it is not guaranteed to do so: c.end() is an rvalue expression, and there is no iterator requirement that specifies that decrement of an rvalue is guaranteed to work. In particular, when iterators are implemented as pointers, --c.end() does not compile, while std::prev(c.end()) does. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4};
    auto it = v.end();
    auto pv = std::prev(it, 2);
    std::cout &lt;&lt; *pv &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1

<h2>See also</h2>

next increment an iterator 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance 
advance <i>(function template)</i> 
