---
title: "stdvalarraymax(3)"
name: "stdvalarraymax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarraymax/"
---

std::valarray&lt;T&gt;::max - std::valarray&lt;T&gt;::max

<h2>Synopsis</h2>

<pre><code>T max() const;</code></pre> 
Computes the maximum value of the elements. 
If there are no elements, the behavior is undefined. 
The function can be used only if operator&lt; is defined for type T. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The maximum of the elements. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;valarray&gt;

#include &lt;iostream&gt;
int main()

{
    std::valarray&lt;double&gt; a{1, 2, 3, 4, 5, 6, 7, 8};
    std::cout &lt;&lt; &quot;Maximum value : &quot; &lt;&lt; a.max() &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Maximum value : 8

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the smallest element 
min <i>(public member function)</i> 
