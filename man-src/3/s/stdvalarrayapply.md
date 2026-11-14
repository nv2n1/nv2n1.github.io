---
title: "stdvalarrayapply(3)"
name: "stdvalarrayapply"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarrayapply/"
---

std::valarray&lt;T&gt;::apply - std::valarray&lt;T&gt;::apply

<h2>Synopsis</h2>

<pre><code>valarray&lt;T&gt; apply(T func(T)) const;

valarray&lt;T&gt; apply(T func(const T &amp;)) const;</code></pre> 
Returns a new valarray of the same size with values which are acquired by applying function func to the previous values of the elements. 

<h2>Parameters</h2>

func - function to apply to the values

<h2>Return value</h2>

The resulting valarray with values acquired by applying function func. 

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

calculates and prints the first 10 factorials 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;

#include &lt;cmath&gt;
int main()

{
    std::valarray&lt;int&gt; v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    v = v.apply([](int n) -&gt; int {
        return std::round(std::tgamma(n + 1));
    });
    for (auto n : v) {
        std::cout &lt;&lt; n &lt;&lt; ' ';
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 6 24 120 720 5040 40320 362880 3628800

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to a range of elements 
for_each <i>(function template)</i> 
