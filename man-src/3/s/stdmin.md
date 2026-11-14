---
title: "stdmin(3)"
name: "stdmin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmin/"
---

std::min - std::min

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class T&gt;
    (until C++ 14)

        const T &amp;min(const T &amp;a, const T &amp;b);

template &lt;class T&gt;
(since C++ 14)

    constexpr const T &amp;min(const T &amp;a, const T &amp;b);

template &lt;class T, class Compare&gt;
(until C++ 14)

    const T &amp;min(const T &amp;a, const T &amp;b, Compare comp);

template &lt;class T, class Compare&gt;
(since C++ 14)

    constexpr const T &amp;min(const T &amp;a, const T &amp;b, Compare comp);
(1)

    template &lt;class T&gt;
    (since C++ 11)

        T min(std::initializer_list&lt;T&gt; ilist);
(2)(until C++ 14)

    template &lt;class T&gt;
    (since C++ 14)

        constexpr T min(std::initializer_list&lt;T&gt; ilist);
(3)

    template &lt;class T, class Compare&gt;
    (since C++ 11)

        T min(std::initializer_list&lt;T&gt; ilist, Compare comp);
(4)(until C++ 14)

    template &lt;class T, class Compare&gt;
    (since C++ 14)

        constexpr T min(std::initializer_list&lt;T&gt; ilist, Compare comp);</code></pre> 
Returns the smaller of the given values. 
1-2) Returns the smaller of a and b. 
3-4) Returns the smallest of the values in initializer list ilist. 
The (1,3) versions use operator&lt; to compare the values, the (2,4) versions use the given comparison function comp. 

<h2>Parameters</h2>

a, b - the values to compare 
ilist - initializer list with the values to compare 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if a is less than b. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
cmp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type T can be implicitly converted to both of them.

<h2>Type requirements</h2>

- 
T must meet the requirements of LessThanComparable in order to use overloads (1,3). 
- 
T must meet the requirements of CopyConstructible in order to use overloads (3,4).

<h2>Return value</h2>

1-2) The smaller of a and b. If the values are equivalent, returns a. 
3-4) The smallest value in ilist. If several values are equivalent to the smallest, returns the leftmost such value. 

<h2>Complexity</h2>

1-2) Exactly one comparison 
3-4) Exactly ilist.size() - 1 comparisons

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;const T&amp; min(const T&amp; a, const T&amp; b) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (b &lt; a) ? b : a; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class T, class Compare&gt; 
&nbsp;<wbr>&nbsp;const T&amp; min(const T&amp; a, const T&amp; b, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (comp(b, a)) ? b : a; 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;T min( std::initializer_list&lt;T&gt; ilist) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return *std::min_element(ilist.begin(), ilist.end()); 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;template&lt;class T, class Compare&gt; 
&nbsp;<wbr>&nbsp;T min(std::initializer_list&lt;T&gt; ilist, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return *std::min_element(ilist.begin(), ilist.end(), comp); 
&nbsp;<wbr>&nbsp;} 

 

 

 
Warning 

 
Capturing the result of std::min by reference if one of the parameters is rvalue produces a dangling reference if that parameter is returned: 

 
&nbsp;<wbr>&nbsp;int n = 1; 
&nbsp;<wbr>&nbsp;const int&amp; r = std::min(n-1, n+1); 
&nbsp;<wbr>&nbsp;// r is dangling

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;
int main()

{
    std::cout &lt;&lt; &quot;smaller of 1 and 9999: &quot; &lt;&lt; std::min(1, 9999) &lt;&lt; '\n'
              &lt;&lt; &quot;smaller of 'a', and 'b': &quot; &lt;&lt; std::min('a', 'b') &lt;&lt; '\n'
              &lt;&lt; &quot;shortest of \&quot;foo\&quot;, \&quot;bar\&quot;, and \&quot;hello\&quot;: &quot; &lt;&lt; std::min({&quot;foo&quot;, &quot;bar&quot;, &quot;hello&quot;}, [](const std::string &amp;s1, const std::string &amp;s2) {
                     return s1.size() &lt; s2.size();
                 })
              &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;smaller of 1 and 9999: 1 
&nbsp;<wbr>&nbsp;smaller of 'a', and 'b': a 
&nbsp;<wbr>&nbsp;shortest of &quot;foo&quot;, &quot;bar&quot;, and &quot;hello&quot;: foo

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the greater of the given values 
max <i>(function template)</i> 
minmax returns the smaller and larger of two elements 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the smallest element in a range 
min_element <i>(function template)</i> 
