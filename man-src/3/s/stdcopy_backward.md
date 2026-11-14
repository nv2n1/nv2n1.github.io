---
title: "stdcopy_backward(3)"
name: "stdcopy_backward"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcopy_backward/"
---

std::copy_backward - std::copy_backward

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class BidirIt1, class BidirIt2 &gt;                                           (until C++20)

BidirIt2 copy_backward( BidirIt1 first, BidirIt1 last, BidirIt2 d_last );

template&lt; class BidirIt1, class BidirIt2 &gt;                                           (since C++20)

constexpr BidirIt2 copy_backward( BidirIt1 first, BidirIt1 last, BidirIt2 d_last );</code></pre> 
Copies the elements from the range, defined by [first, last), to another range ending at d_last. The elements are copied in reverse order (the last element is copied first), but their relative order is preserved. 
The behavior is undefined if d_last is within (first, last]. std::copy must be used instead of std::copy_backward in that case. 

<h2>Parameters</h2>

first, last - the range of the elements to copy 
d_last - end of the destination range..

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of LegacyBidirectionalIterator.

<h2>Return value</h2>

iterator to the last element copied. 

<h2>Complexity</h2>

Exactly last - first assignments.

<h2>Notes</h2>

When copying overlapping ranges, std::copy is appropriate when copying to the left (beginning of the destination range is outside the source range) while std::copy_backward is appropriate when copying to the right (end of the destination range is outside the source range). 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class BidirIt1, class BidirIt2 &gt; 
&nbsp;<wbr>&nbsp;BidirIt2 copy_backward(BidirIt1 first, BidirIt1 last, BidirIt2 d_last) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*(--d_last) = *(--last); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_last; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; from_vector;
    for (int i = 0; i &lt; 10; i++) {
        from_vector.push_back(i);
    }
    std::vector&lt;int&gt; to_vector(15);
    std::copy_backward(from_vector.begin(), from_vector.end(), to_vector.end());
    std::cout &lt;&lt; &quot;to_vector contains: &quot;;
    for (auto i : to_vector) {
        std::cout &lt;&lt; i &lt;&lt; &quot; &quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;to_vector contains: 0 0 0 0 0 0 1 2 3 4 5 6 7 8 9

<h2>See also</h2>

copy 
copy_if copies a range of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
