---
title: "stdminmax(3)"
name: "stdminmax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdminmax/"
---

std::minmax - std::minmax

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class T&gt;
    (since C++ 11)

        std::pair&lt;const T &amp;, const T &amp;&gt; minmax(const T &amp;a, const T &amp;b);
(until C++ 14)

    template &lt;class T&gt;
    (since C++ 14)

        constexpr std::pair&lt;const T &amp;, const T &amp;&gt; minmax(const T &amp;a, const T &amp;b);

template &lt;class T, class Compare&gt;
(since C++ 11)

    std::pair&lt;const T &amp;, const T &amp;&gt; minmax(const T &amp;a, const T &amp;b, (until C++ 14)

                                                                       Compare comp);

template &lt;class T, class Compare&gt;

constexpr std::pair&lt;const T &amp;, const T &amp;&gt; minmax(const T &amp;a, const T &amp;b, (1)(since C++ 14)

                                                                             Compare comp);

template &lt;class T&gt;
(2)(since C++ 11)

    std::pair&lt;T, T&gt; minmax(std::initializer_list&lt;T&gt; ilist);
(until C++ 14)

    template &lt;class T&gt;
    (since C++ 14)

        constexpr std::pair&lt;T, T&gt; minmax(std::initializer_list&lt;T&gt; ilist);
(3)

    template &lt;class T, class Compare&gt;
    (since C++ 11)

        std::pair&lt;T, T&gt; minmax(std::initializer_list&lt;T&gt; ilist, Compare comp);
(4)(until C++ 14)

    template &lt;class T, class Compare&gt;
    (since C++ 14)

        constexpr std::pair&lt;T, T&gt; minmax(std::initializer_list&lt;T&gt; ilist, Compare comp);</code></pre> 
Returns the lowest and the greatest of the given values. 
1-2) Returns references to the smaller and the greater of a and b. 
3-4) Returns the smallest and the greatest of the values in initializer list ilist. 
The (1,3) versions use operator&lt; to compare the values, whereas the (2,4) versions use the given comparison function comp. 

<h2>Parameters</h2>

a, b - the values to compare 
ilist - initializer list with the values to compare 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type T can be implicitly converted to both of them.

<h2>Type requirements</h2>

- 
T must meet the requirements of LessThanComparable in order to use overloads (1,3). 
- 
T must meet the requirements of CopyConstructible in order to use overloads (3,4).

<h2>Return value</h2>

1-2) Returns the result of std::pair&lt;const T&amp;, const T&amp;&gt;(a, b) if a&lt;b or if a is equivalent to b. Returns the result of std::pair&lt;const T&amp;, const T&amp;&gt;(b, a) if b&lt;a. 
3-4) A pair with the smallest value in ilist as the first element and the greatest as the second. If several elements are equivalent to the smallest, the leftmost such element is returned. If several elements are equivalent to the largest, the rightmost such element is returned. 

<h2>Complexity</h2>

1-2) Exactly one comparison 
3-4) At most ilist.size() * 3 / 2 comparisons

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;const T&amp;, const T&amp;&gt; minmax( const T&amp; a, const T&amp; b ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (b &lt; a) ? std::pair&lt;const T&amp;, const T&amp;&gt;(b, a) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::pair&lt;const T&amp;, const T&amp;&gt;(a, b); 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class T, class Compare&gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;const T&amp;, const T&amp;&gt; minmax( const T&amp; a, const T&amp; b, Compare comp ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return comp(b, a) ? std::pair&lt;const T&amp;, const T&amp;&gt;(b, a) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::pair&lt;const T&amp;, const T&amp;&gt;(a, b); 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;T, T&gt; minmax( std::initializer_list&lt;T&gt; ilist ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = std::minmax_element(ilist.begin(), ilist.end()); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(*p.first, *p.second); 
&nbsp;<wbr>&nbsp;} 

 
Fourth version 

 
&nbsp;<wbr>&nbsp;template&lt; class T, class Compare &gt; 
&nbsp;<wbr>&nbsp;std::pair&lt;T, T&gt; minmax( std::initializer_list&lt;T&gt; ilist, Compare comp ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auto p = std::minmax_element(ilist.begin(), ilist.end(), comp); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::make_pair(*p.first, *p.second); 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

For overloads (1,2), if one of the parameters is an rvalue, the reference returned becomes a dangling reference at the end of the full expression that contains the call to minmax: int n = 1;

auto p = std::minmax(n, n + 1);

int m = p.first; // ok

int x = p.second; // undefined behavior


<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;cstdlib&gt;

#include &lt;ctime&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4, 1, 5, 9, 2, 6};
    std::srand(std::time(0));
    std::pair&lt;int, int&gt; bounds = std::minmax(std::rand() % v.size(),
                                             std::rand() % v.size());
    std::cout &lt;&lt; &quot;v[&quot; &lt;&lt; bounds.first &lt;&lt; &quot;,&quot; &lt;&lt; bounds.second &lt;&lt; &quot;]: &quot;;
    for (int i = bounds.first; i &lt; bounds.second; ++i) {
        std::cout &lt;&lt; v[i] &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;v[2,7]: 4 1 5 9 2

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the smaller of the given values 
min <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the greater of the given values 
max <i>(function template)</i> 
minmax_element returns the smallest and the largest elements in a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
