---
title: "stdbinary_search(3)"
name: "stdbinary_search"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinary_search/"
---

std::binary_search - std::binary_search

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class ForwardIt, class T&gt;
    (until C++ 20)

        bool binary_search(ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class ForwardIt, class T&gt;
(since C++ 20)

    constexpr bool binary_search(ForwardIt first, ForwardIt last, const T &amp;value);
(1)

    template &lt;class ForwardIt, class T, class Compare&gt;
    (until C++ 20)

        bool binary_search(ForwardIt first, ForwardIt last, const T &amp;value, Compare comp);
(2)

    template &lt;class ForwardIt, class T, class Compare&gt;
    (since C++ 20)

        constexpr bool binary_search(ForwardIt first, ForwardIt last, const T &amp;value, Compare comp);</code></pre> 
Checks if an element equivalent to value appears within the range [first, last). 
For std::binary_search to succeed, the range [first, last) must be at least partially ordered with respect to value, i.e. it must satisfy all of the following requirements: 
* partitioned with respect to element &lt; value or comp(element, value) (that is, all elements for which the expression is true precedes all elements for which the expression is false) 
* partitioned with respect to !(value &lt; element) or !comp(value, element) 
* for all elements, if element &lt; value or comp(element, value) is true then !(value &lt; element) or !comp(value, element) is also true 
A fully-sorted range meets these criteria. 
The first version uses operator&lt; to compare the elements, the second version uses the given comparison function comp. 

<h2>Parameters</h2>

first, last - the range of elements to examine 
value - value to compare the elements to 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type T can be implicitly converted to both Type1 and Type2, and an object of type ForwardIt can be dereferenced and then implicitly converted to both Type1 and Type2.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
Compare must meet the requirements of BinaryPredicate. it is not required to satisfy Compare

<h2>Return value</h2>

true if an element equal to value is found, false otherwise. 

<h2>Complexity</h2>

The number of comparisons performed is logarithmic in the distance between first and last (At most log 
2(last - first) + <a HREF="/docs/linux/man/1-o/">O</a>(1) comparisons). However, for non-LegacyRandomAccessIterators, number of iterator increments is linear.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T&gt; 
&nbsp;<wbr>&nbsp;bool binary_search(ForwardIt first, ForwardIt last, const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = std::lower_bound(first, last, value); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (!(first == last) &amp;&amp; !(value &lt; *first)); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T, class Compare&gt; 
&nbsp;<wbr>&nbsp;bool binary_search(ForwardIt first, ForwardIt last, const T&amp; value, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first = std::lower_bound(first, last, value, comp); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (!(first == last) &amp;&amp; !(comp(value, *first))); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; haystack{1, 3, 4, 5, 9};
    std::vector&lt;int&gt; needles{1, 2, 3};
    for (auto needle : needles) {
        std::cout &lt;&lt; &quot;Searching for &quot; &lt;&lt; needle &lt;&lt; '\n';
        if (std::binary_search(haystack.begin(), haystack.end(), needle)) {
            std::cout &lt;&lt; &quot;Found &quot; &lt;&lt; needle &lt;&lt; '\n';
        } else {
            std::cout &lt;&lt; &quot;no dice!\n&quot;;
        }
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Searching for 1 
&nbsp;<wbr>&nbsp;Found 1 
&nbsp;<wbr>&nbsp;Searching for 2 
&nbsp;<wbr>&nbsp;no dice! 
&nbsp;<wbr>&nbsp;Searching for 3 
&nbsp;<wbr>&nbsp;Found 3 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_270 C++98 Compare was required to be a strict weak ordering only a partitioning is needed; heterogeneous comparisons permitted

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns range of elements matching a specific key 
equal_range <i>(function template)</i> 
