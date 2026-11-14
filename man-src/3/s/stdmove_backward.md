---
title: "stdmove_backward(3)"
name: "stdmove_backward"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmove_backward/"
---

std::move_backward - std::move_backward

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class BidirIt1, class BidirIt2 &gt;                                           (since C++11)

BidirIt2 move_backward( BidirIt1 first, BidirIt1 last, BidirIt2 d_last );            (until C++20)

template&lt; class BidirIt1, class BidirIt2 &gt;                                           (since C++20)

constexpr BidirIt2 move_backward( BidirIt1 first, BidirIt1 last, BidirIt2 d_last );</code></pre> 
Moves the elements from the range [first, last), to another range ending at d_last. The elements are moved in reverse order (the last element is moved first), but their relative order is preserved. 
The behavior is undefined if d_last is within (first, last]. std::move must be used instead of std::move_backward in that case. 

<h2>Parameters</h2>

first, last - the range of the elements to move 
d_last - end of the destination range

<h2>Type requirements</h2>

- 
BidirIt1, BidirIt2 must meet the requirements of LegacyBidirectionalIterator.

<h2>Return value</h2>

Iterator in the destination range, pointing at the last element moved. 

<h2>Complexity</h2>

Exactly last - first move assignments.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class BidirIt1, class BidirIt2 &gt; 
&nbsp;<wbr>&nbsp;BidirIt2 move_backward(BidirIt1 first, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BidirIt1 last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;BidirIt2 d_last) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*(--d_last) = std::move(*(--last)); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_last; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

When moving overlapping ranges, std::move is appropriate when moving to the left (beginning of the destination range is outside the source range) while std::move_backward is appropriate when moving to the right (end of the destination range is outside the source range). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;std::string&gt; src{&quot;foo&quot;, &quot;bar&quot;, &quot;baz&quot;};
    std::vector&lt;std::string&gt; dest(src.size());
    std::cout &lt;&lt; &quot;src: &quot;;
    for (const auto &amp;s : src) {
        std::cout &lt;&lt; s &lt;&lt; ' ';
    }
    std::cout &lt;&lt; &quot;\ndest: &quot;;
    for (const auto &amp;s : dest) {
        std::cout &lt;&lt; s &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
    std::move_backward(src.begin(), src.end(), dest.end());
    std::cout &lt;&lt; &quot;src: &quot;;
    for (const auto &amp;s : src) {
        std::cout &lt;&lt; s &lt;&lt; ' ';
    }
    std::cout &lt;&lt; &quot;\ndest: &quot;;
    for (const auto &amp;s : dest) {
        std::cout &lt;&lt; s &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;src: foo bar baz 
&nbsp;<wbr>&nbsp;dest: 
&nbsp;<wbr>&nbsp;src: 
&nbsp;<wbr>&nbsp;dest: foo bar baz

<h2>See also</h2>

move moves a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
