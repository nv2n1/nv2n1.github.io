---
title: "stdexperimentaldefault_searcherstdexperimentalmake_default_searcher(3)"
name: "stdexperimentaldefault_searcherstdexperimentalmake_default_searcher"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaldefault_searcherstdexperimentalmake_default_searcher/"
---

std::experimental::default_searcher,std::experimental::make_default_searcher - std::experimental::default_searcher,std::experimental::make_default_searcher

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/functional&gt;

template&lt; class ForwardIterator1, class BinaryPredicate = std::equal_to&lt;&gt; &gt;  (library fundamentals TS)

class default_searcher;</code></pre> 
A class suitable for use with std::experimental::search that delegates the search operation to the standard library's std::search. 
default_searcher is CopyConstructible and CopyAssignable. 

<h2>Member functions</h2>

&nbsp;std::experimental::default_searcher::default_searcher 

 

 
default_searcher( ForwardIterator pat_first, 
ForwardIterator pat_last, 
BinaryPredicate pred = BinaryPredicate()); 

 
Constructs a default_searcher by storing copies of pat_first, pat_last, and pred

<h2>Parameters</h2>

pat_first, pat_last - a pair of iterators designating the string to be searched for 
pred - a callable object used to determine equality

<h2>Exceptions</h2>

Any exceptions thrown by the copy constructors of BinaryPredicate or ForwardIterator. 

 
&nbsp;std::experimental::default_searcher::operator() 

 

 
template&lt; class ForwardIterator2 &gt; <i>(until C++17)</i> 
ForwardIterator2 operator()( ForwardIterator2 first, ForwardIterator2 last ) const; 
template&lt; class ForwardIterator2 &gt; 
std::pair&lt;ForwardIterator2, ForwardIterator2&gt; <i>(since C++17)</i> 
operator()( ForwardIterator2 first, ForwardIterator2 last ) const; 

 
The member function called by std::experimental::search to perform a search with this searcher. 

 
Equivalent to std::search(first, last, pat_first, pat_last, pred); <i>(until C++17)</i> 
Returns a pair of iterators i, j, where i is std::search(first, last, pat_first, pat_last, pred) and j is std::next(i, std::distance(pat_first, pat_last)) unless std::search returned last (no match), in which case j equals last as well <i>(until C++17)</i>

<h2>Parameters</h2>

first, last - a pair of iterators designating the string to be examined

<h2>Return value</h2>

Iterator to the first position in [first, last) where a subsequence that compares equal to [pat_first, pat_last) as defined by pred is located, or a copy of last otherwise. <i>(until C++17)</i> 
A pair of iterators to the first and one past last positions in [first, last) where a subsequence that compares equal to [pat_first, pat_last) as defined by pred is located, or a pair of copies of last otherwise. <i>(since C++17)</i> 
Helper Functions template &lt;class ForwardIterator, class BinaryPredicate = std::equal_to&lt;&gt;&gt;

default_searcher&lt;ForwardIterator, BinaryPredicate&gt; make_default_searcher(

    ForwardIterator pat_first, (library fundamentals TS)

                                   ForwardIterator pat_last,

    BinaryPredicate pred = BinaryPredicate());
Helper function that constructs a std::experimental::default_searcher using template argument deduction.Equivalent to return default_searcher&lt;ForwardIterator, BinaryPredicate&gt;(pat_first, pat_last, pred);


<h2>Parameters</h2>

pat_first, pat_last - a pair of iterators designating the string to be searched for 
pred - a callable object used to determine equality

<h2>Return value</h2>

A default_searcher constructed with the arguments pat_first, pat_last, pred. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;experimental/algorithm&gt;

#include &lt;experimental/functional&gt;
int main()

{
    std::string in = &quot;Lorem ipsum dolor sit amet, consectetur adipiscing elit,&quot;
                     &quot; sed do eiusmod tempor incididunt ut labore et dolore magna aliqua&quot;;
    std::string needle = &quot;pisci&quot;;
    auto it = std::experimental::search(in.begin(), in.end(),
                                        std::experimental::make_default_searcher(
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
