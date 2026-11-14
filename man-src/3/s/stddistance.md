---
title: "stddistance(3)"
name: "stddistance"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddistance/"
---

std::distance - std::distance

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class InputIt &gt;

typename std::iterator_traits&lt;InputIt&gt;::difference_type             (until C++17)

distance( InputIt first, InputIt last );

template&lt; class InputIt &gt;

constexpr typename std::iterator_traits&lt;InputIt&gt;::difference_type   (since C++17)

distance( InputIt first, InputIt last );</code></pre> 
Returns the number of hops from first to last. 
The behavior is undefined if last is not reachable from first by (possibly repeatedly) incrementing first. <i>(until C++11)</i> 
If InputIt is not LegacyRandomAccessIterator, the behavior is undefined if last is not reachable from first by (possibly repeatedly) incrementing first. If InputIt is LegacyRandomAccessIterator, the behavior is undefined if last is not reachable from first and first is not reachable from last. <i>(since C++11)</i> 
first - iterator pointing to the first element 
last - iterator pointing to the end of the range

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. The operation is more efficient if InputIt additionally meets the requirements of LegacyRandomAccessIterator

<h2>Return value</h2>

The number of increments needed to go from first to last. 
The value may be negative if random-access iterators are used and first is reachable from last 
<i>(since C++11)</i> 

<h2>Complexity</h2>

Linear. 
However, if InputIt additionally meets the requirements of LegacyRandomAccessIterator, complexity is constant.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4};
    std::cout &lt;&lt; &quot;distance(first, last) = &quot;
              &lt;&lt; std::distance(v.begin(), v.end()) &lt;&lt; '\n'
              &lt;&lt; &quot;distance(last, first) = &quot;
              &lt;&lt; std::distance(v.end(), v.begin()) &lt;&lt; '\n';
    // the behavior is undefined (until C++11)
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;distance(first, last) = 3 
&nbsp;<wbr>&nbsp;distance(last, first) = -3

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances an iterator by given distance 
advance <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the number of elements satisfying specific criteria 
count <i>(function template)</i> 
count_if 
