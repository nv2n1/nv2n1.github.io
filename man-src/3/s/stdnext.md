---
title: "stdnext(3)"
name: "stdnext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnext/"
---

std::next - std::next

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class ForwardIt &gt;

ForwardIt next(                                                     (since C++11)

ForwardIt it,                                                       (until C++17)

typename std::iterator_traits&lt;ForwardIt&gt;::difference_type n = 1 );

template&lt; class InputIt &gt;

constexpr InputIt next(                                             (since C++17)

InputIt it,

typename std::iterator_traits&lt;InputIt&gt;::difference_type n = 1 );</code></pre> 
Return the nth successor of iterator it. 

<h2>Parameters</h2>

it - an iterator 
n - number of elements to advance

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
InputIt must meet the requirements of LegacyInputIterator.

<h2>Return value</h2>

The nth successor of iterator it. 

<h2>Complexity</h2>

Linear. 
However, if InputIt or ForwardIt additionally meets the requirements of LegacyRandomAccessIterator, complexity is constant.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt; 
&nbsp;<wbr>&nbsp;ForwardIt next(ForwardIt it, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;ForwardIt&gt;::difference_type n = 1) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::advance(it, n); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return it; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

Although the expression ++c.begin() often compiles, it is not guaranteed to do so: c.begin() is an rvalue expression, and there is no LegacyBidirectionalIterator requirement that specifies that increment of an rvalue is guaranteed to work. In particular, when iterators are implemented as pointers, ++c.begin() does not compile, while std::next(c.begin()) does. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4};
    auto it = v.begin();
    auto nx = std::next(it, 2);
    std::cout &lt;&lt; *it &lt;&lt; ' ' &lt;&lt; *nx &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 4

<h2>See also</h2>

prev decrement an iterator 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance 
advance <i>(function template)</i> 
