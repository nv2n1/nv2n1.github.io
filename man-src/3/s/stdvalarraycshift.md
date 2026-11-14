---
title: "stdvalarraycshift(3)"
name: "stdvalarraycshift"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarraycshift/"
---

std::valarray&lt;T&gt;::cshift - std::valarray&lt;T&gt;::cshift

<h2>Synopsis</h2>

<pre><code>valarray&lt;T&gt; cshift(int count) const;</code></pre> 
Returns a new valarray of the same size with elements whose positions are shifted circularly by count elements. The new position of each element is (i−count) mod s where i is the previous position and s is size(). 

<h2>Parameters</h2>

count - number of positions to shift the elements by

<h2>Return value</h2>

The resulting valarray with circularly shifted elements. 

<h2>Notes</h2>

The function can be implemented with the return type different from std::valarray. In this case, the replacement type has the following properties: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All const member functions of std::valarray are provided. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::valarray, std::slice_array, std::gslice_array, std::mask_array and std::indirect_array can be constructed from the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting an argument of type const std::valarray&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;except begin() and end() 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i> should also accept the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* All functions accepting two arguments of type const std::valarray&amp; should accept every combination of const std::valarray&amp; and the replacement type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The return type does not add more than two levels of template nesting over the most deeply-nested argument type. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;

int main()
{
    std::valarray&lt;int&gt; v{1, 2, 3, 4, 5, 6, 7, 8};
    for (auto const &amp;val : v) {
        std::cout &lt;&lt; val &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; &quot;\n&quot;;
    std::valarray&lt;int&gt; v2 = v.cshift(2);
    for (auto const &amp;val : v2) {
        std::cout &lt;&lt; val &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8 
&nbsp;<wbr>&nbsp;3 4 5 6 7 8 1 2

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;zero-filling shift the elements of the valarray 
shift <i>(public member function)</i> 
