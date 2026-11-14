---
title: "stdfront_inserter(3)"
name: "stdfront_inserter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfront_inserter/"
---

std::front_inserter - std::front_inserter

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class Container &gt;                                                      (until C++20)

std::front_insert_iterator&lt;Container&gt; front_inserter( Container&amp; c );

template&lt; class Container &gt;                                                      (since C++20)

constexpr std::front_insert_iterator&lt;Container&gt; front_inserter( Container&amp; c );</code></pre> 
front_inserter is a convenience function template that constructs a std::front_insert_iterator for the container c with the type deduced from the type of the argument. 

<h2>Parameters</h2>

c - container that supports a push_front operation

<h2>Return value</h2>

A std::front_insert_iterator which can be used to add elements to the beginning of the container c 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class Container &gt; 
&nbsp;<wbr>&nbsp;std::front_insert_iterator&lt;Container&gt; front_inserter( Container&amp; c ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::front_insert_iterator&lt;Container&gt;(c); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;vector&gt;

#include &lt;deque&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;

int main()

{
    std::vector&lt;int&gt; v{1, 2, 3, 4, 5};
    std::deque&lt;int&gt; d;
    std::copy(v.begin(), v.end(), std::front_inserter(d));
    for (int n : d)
        std::cout &lt;&lt; n &lt;&lt; ' ';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;5 4 3 2 1

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion at the front of a container 
front_insert_iterator <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::back_insert_iterator of type inferred from the argument 
back_inserter <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::insert_iterator of type inferred from the argument 
inserter <i>(function template)</i> 
