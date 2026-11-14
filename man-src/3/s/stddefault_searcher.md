---
title: "stddefault_searcher(3)"
name: "stddefault_searcher"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddefault_searcher/"
---

std::default_searcher - std::default_searcher

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class ForwardIt, class BinaryPredicate = std::equal_to&lt;&gt; &gt;  (since C++17)

class default_searcher;</code></pre> 
A class suitable for use with Searcher overload of std::search that delegates the search operation to the pre-C++17 standard library's std::search. 
default_searcher is CopyConstructible and CopyAssignable. 

<h2>Member functions</h2>

&nbsp;std::default_searcher::default_searcher 

 

 
default_searcher( ForwardIt pat_first, <i>(since C++17)</i> 
ForwardIt pat_last, <i>(until C++20)</i> 
BinaryPredicate pred = BinaryPredicate()); 
constexpr default_searcher( ForwardIt pat_first, 
ForwardIt pat_last, <i>(since C++20)</i> 
BinaryPredicate pred = BinaryPredicate()); 

 
Constructs a default_searcher by storing copies of pat_first, pat_last, and pred

<h2>Parameters</h2>

pat_first, pat_last - a pair of iterators designating the string to be searched for 
pred - a callable object used to determine equality

<h2>Exceptions</h2>

Any exceptions thrown by the copy constructors of BinaryPredicate or ForwardIt. 

 
&nbsp;std::default_searcher::operator() 

 

 
template&lt; class ForwardIt2 &gt; <i>(since C++17)</i> 
std::pair&lt;ForwardIt2, ForwardIt2&gt; <i>(until C++20)</i> 
operator()( ForwardIt2 first, ForwardIt2 last ) const; 
template&lt; class ForwardIt2 &gt; 
constexpr std::pair&lt;ForwardIt2, ForwardIt2&gt; <i>(since C++20)</i> 
operator()( ForwardIt2 first, ForwardIt2 last ) const; 

 
The member function called by the Searcher overload of std::search to perform a search with this searcher. 
Returns a pair of iterators i, j, where i is std::search(first, last, pat_first, pat_last, pred) and j is std::next(i, std::distance(pat_first, pat_last)) unless std::search returned last (no match), in which case j equals last as well.

<h2>Parameters</h2>

first, last - a pair of iterators designating the string to be examined

<h2>Return value</h2>

A pair of iterators to the first and one past last positions in [first, last) where a subsequence that compares equal to [pat_first, pat_last) as defined by pred is located, or a pair of copies of last otherwise. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;algorithm&gt;

#include &lt;functional&gt;
int main()

{
    std::string in = &quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit,&quot;
                     &quot; sed do eiusmod tempor incididunt ut labore et dolore magna aliqua&quot;;
    std::string needle = &quot;pisci&quot;;
    auto it = std::search(in.begin(), in.end(),
                          std::default_searcher(
                              needle.begin(), needle.end()));
    if (it != in.end())
        std::cout &lt;&lt; &quot;The string &quot; &lt;&lt; needle &lt;&lt; &quot; found at offset &quot;
                  &lt;&lt; it - in.begin() &lt;&lt; '\n';
    else
        std::cout &lt;&lt; &quot;The string &quot; &lt;&lt; needle &lt;&lt; &quot; not found\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The string pisci found at offset 43

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
