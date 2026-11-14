---
title: "stdback_inserter(3)"
name: "stdback_inserter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdback_inserter/"
---

std::back_inserter - std::back_inserter

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class Container &gt;                                                    (until C++20)

std::back_insert_iterator&lt;Container&gt; back_inserter( Container&amp; c );

template&lt; class Container &gt;                                                    (since C++20)

constexpr std::back_insert_iterator&lt;Container&gt; back_inserter( Container&amp; c );</code></pre> 
back_inserter is a convenience function template that constructs a std::back_insert_iterator for the container c with the type deduced from the type of the argument. 

<h2>Parameters</h2>

c - container that supports a push_back operation

<h2>Return value</h2>

A std::back_insert_iterator which can be used to add elements to the end of the container c 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class Container &gt; 
&nbsp;<wbr>&nbsp;std::back_insert_iterator&lt;Container&gt; back_inserter( Container&amp; c ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::back_insert_iterator&lt;Container&gt;(c); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;
int main()

{
    std::vector&lt;int&gt; v{1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::fill_n(std::back_inserter(v), 3, -1);
    for (int n : v)
        std::cout &lt;&lt; n &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 3 4 5 6 7 8 9 10 -1 -1 -1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion at the end of a container 
back_insert_iterator <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::front_insert_iterator of type inferred from the argument 
front_inserter <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::insert_iterator of type inferred from the argument 
inserter <i>(function template)</i> 
