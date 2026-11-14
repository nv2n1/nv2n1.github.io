---
title: "stdvalarraysize(3)"
name: "stdvalarraysize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarraysize/"
---

std::valarray&lt;T&gt;::size - std::valarray&lt;T&gt;::size

<h2>Synopsis</h2>

<pre><code>std::size_t size() const;</code></pre> 
Returns the number of elements in the valarray. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Number of elements in the valarray. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;valarray&gt;
int main()

{
    std::valarray&lt;double&gt; a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::cout &lt;&lt; &quot;Average: &quot; &lt;&lt; a.sum() / a.size() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Average: 5.5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes the size of valarray 
resize <i>(public member function)</i> 
