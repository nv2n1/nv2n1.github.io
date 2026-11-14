---
title: "stdmake_reverse_iterator(3)"
name: "stdmake_reverse_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_reverse_iterator/"
---

std::make_reverse_iterator - std::make_reverse_iterator

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template &lt;class Iter&gt;                                                   (since C++14)

std::reverse_iterator&lt;Iter&gt; make_reverse_iterator( Iter i );            (until C++17)

template &lt;class Iter&gt;                                                   (since C++17)

constexpr std::reverse_iterator&lt;Iter&gt; make_reverse_iterator( Iter i );</code></pre> 
make_reverse_iterator is a convenience function template that constructs a std::reverse_iterator for the given iterator i with the type deduced from the type of the argument. 

<h2>Parameters</h2>

i - iterator to be converted to reverse iterator

<h2>Return value</h2>

A std::reverse_iterator constructed from i 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class Iter &gt; 
&nbsp;<wbr>&nbsp;constexpr std::reverse_iterator&lt;Iter&gt; make_reverse_iterator( Iter i ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::reverse_iterator&lt;Iter&gt;(i); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;
int main()
{
    std::vector&lt;int&gt; v{1, 3, 10, 8, 22};
    std::sort(v.begin(), v.end());
    std::copy(v.begin(), v.end(), std::ostream_iterator&lt;int&gt;(std::cout, &quot;, &quot;));
    std::cout &lt;&lt; '\n';
    std::copy(
        std::make_reverse_iterator(v.end()),
        std::make_reverse_iterator(v.begin()),
        std::ostream_iterator&lt;int&gt;(std::cout, &quot;, &quot;));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1, 3, 8, 10, 22, 
&nbsp;<wbr>&nbsp;22, 10, 8, 3, 1,

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for reverse-order traversal 
reverse_iterator <i>(class template)</i> 
rbegin returns a reverse iterator to a container or array 
crbegin <i>(function template)</i> 
<i>(C++14)</i> 
rend returns a reverse end iterator for a container or array 
crend <i>(function template)</i> 
<i>(C++14)</i> 
