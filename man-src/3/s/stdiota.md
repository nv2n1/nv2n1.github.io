---
title: "stdiota(3)"
name: "stdiota"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdiota/"
---

std::iota - std::iota

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;numeric&gt;

    template &lt;class ForwardIt, class T&gt;
    (since C++ 11)

        void iota(ForwardIt first, ForwardIt last, T value);</code></pre> 
Fills the range [first, last) with sequentially increasing values, starting with value and repetitively evaluating ++value. 
Equivalent operation: *(d_first)   = value;

*(d_first+1) = ++value;

*(d_first+2) = ++value;

*(d_first+3) = ++value;

...



<h2>Parameters</h2>

first, last - the range of elements to fill with sequentially increasing values starting with value 
value - initial value to store, the expression ++value must be well-formed

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Exactly last - first increments and assignments.

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class T&gt; 
&nbsp;<wbr>&nbsp;void iota(ForwardIt first, ForwardIt last, T value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while(first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*first++ = value; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++value; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

The function is named after the integer function ⍳ from the programming language APL. It was one of the STL_components that were not included in C++98, but eventually made it into the standard library in C++11. 

<h2>Example</h2>

The following example applies std::shuffle to a vector of std::list iterators since std::shuffle cannot be applied to a std::list directly. std::iota is used to populate both containers. 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;list&gt;

#include &lt;numeric&gt;

#include &lt;random&gt;

#include &lt;vector&gt;
int main()

{
    std::list&lt;int&gt; l(10);
    std::iota(l.begin(), l.end(), -4);
    std::vector&lt;std::list&lt;int&gt;::iterator&gt; v(l.size());
    std::iota(v.begin(), v.end(), l.begin());
    std::shuffle(v.begin(), v.end(), std::mt19937{std::random_device{}()});
    std::cout &lt;&lt; &quot;Contents of the list: &quot;;
    for (auto n : l)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;Contents of the list, shuffled: &quot;;
    for (auto i : v)
        std::cout &lt;&lt; *i &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Contents of the list: -4 -3 -2 -1 0 1 2 3 4 5 
&nbsp;<wbr>&nbsp;Contents of the list, shuffled: 0 -1 3 4 -4 1 -2 -3 2 5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy-assigns the given value to every element in a range 
fill <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns the results of successive function calls to every element in a range 
generate <i>(function template)</i> 
