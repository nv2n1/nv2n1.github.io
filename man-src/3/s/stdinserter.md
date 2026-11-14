---
title: "stdinserter(3)"
name: "stdinserter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinserter/"
---

std::inserter - std::inserter

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class Container &gt;                                                                           (until C++20)

std::insert_iterator&lt;Container&gt; inserter( Container&amp; c, typename Container::iterator i );

template&lt; class Container &gt;                                                                           (since C++20)

constexpr std::insert_iterator&lt;Container&gt; inserter( Container&amp; c, ranges::iterator_t&lt;Container&gt; i );</code></pre> 
inserter is a convenience function template that constructs a std::insert_iterator for the container c and its iterator i with the type deduced from the type of the argument. 

<h2>Parameters</h2>

c - container that supports a insert operation 
i - iterator in c indicating the insertion position

<h2>Return value</h2>

A std::insert_iterator which can be used to insert elements into the container c at the position indicated by i. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class Container &gt; 
&nbsp;<wbr>&nbsp;std::insert_iterator&lt;Container&gt; inserter( Container&amp; c, typename Container::iterator i ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::insert_iterator&lt;Container&gt;(c, i); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;iterator&gt;

#include &lt;vector&gt;

#include &lt;set&gt;
int main()

{
    std::multiset&lt;int&gt; s{1, 2, 3};
    // std::inserter is commonly used with sets
    std::fill_n(std::inserter(s, s.end()), 5, 2);
    for (int n : s)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    std::vector&lt;int&gt; d{100, 200, 300};
    std::vector&lt;int&gt; l{1, 2, 3, 4, 5};
    // when inserting in a sequence container, insertion point advances
    // because each std::insert_iterator::operator= updates the target iterator
    std::copy(d.begin(), d.end(), std::inserter(l, std::next(l.begin())));
    for (int n : l)
        std::cout &lt;&lt; n &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2 2 2 2 2 2 3 
&nbsp;<wbr>&nbsp;1 100 200 300 2 3 4 5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iterator adaptor for insertion into a container 
insert_iterator <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::back_insert_iterator of type inferred from the argument 
back_inserter <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::front_insert_iterator of type inferred from the argument 
front_inserter <i>(function template)</i> 
