---
title: "stdvalarrayresize(3)"
name: "stdvalarrayresize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvalarrayresize/"
---

std::valarray&lt;T&gt;::resize - std::valarray&lt;T&gt;::resize

<h2>Synopsis</h2>

<pre><code>void resize(std::size_t count, T value = T());</code></pre> 
Resizes the valarray to contain count elements and assigns value to each element. 
This functions invalidates all pointers and references to elements in the array. 

<h2>Parameters</h2>

count - new size of the container 
value - the value to initialize the new elements with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;valarray&gt;

#include &lt;iostream&gt;

int main()

{
    std::valarray&lt;int&gt; v{1, 2, 3};
    v.resize(10);
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 0 0 0 0 0 0 0 0 0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the size of valarray 
size <i>(public member function)</i> 
