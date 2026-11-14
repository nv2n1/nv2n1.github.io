---
title: "stdvalarraysum(3)"
name: "stdvalarraysum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarraysum/"
---

std::valarray&lt;T&gt;::sum - std::valarray&lt;T&gt;::sum

<h2>Synopsis</h2>

<pre><code>T sum() const;</code></pre> 
Computes the sum of the elements. 
The function can be used only if operator+= is defined for type T. If the std::valarray is empty, the behavior is undefined. The order in which the elements are processed by this function is unspecified. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The sum of the elements. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;
int main()

{
    std::valarray&lt;int&gt; a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::cout &lt;&lt; a.sum() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;55

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies a function to every element of a valarray 
apply <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sums up a range of elements 
accumulate <i>(function template)</i> 
