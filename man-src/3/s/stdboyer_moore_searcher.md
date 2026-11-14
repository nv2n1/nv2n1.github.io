---
title: "stdboyer_moore_searcher(3)"
name: "stdboyer_moore_searcher"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdboyer_moore_searcher/"
---

std::boyer_moore_searcher - std::boyer_moore_searcher

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class RandomIt1,

class Hash = std::hash&lt;typename std::iterator_traits&lt;RandomIt1&gt;::value_type&gt;,  (since C++17)

class BinaryPredicate = std::equal_to&lt;&gt; &gt;

class boyer_moore_searcher;</code></pre> 
A searcher suitable for use with the Searcher overload of std::search that implements the Boyer-Moore_string_searching_algorithm. 
boyer_moore_searcher is CopyConstructible and CopyAssignable. 
RandomIt1 must meet the requirements of LegacyRandomAccessIterator. 

<h2>Member functions</h2>

&nbsp;std::boyer_moore_searcher::boyer_moore_searcher 

 

 
boyer_moore_searcher( RandomIt1 pat_first, 
RandomIt1 pat_last, 
Hash hf = Hash(), 
BinaryPredicate pred = BinaryPredicate()); 

 
Constructs a boyer_moore_searcher by storing copies of pat_first, pat_last, hf, and pred, setting up any necessary internal data structures. 
The value type of RandomIt1 must be DefaultConstructible, CopyConstructible and CopyAssignable. 
For any two values A and B of the type std::iterator_traits&lt;RandomIt1&gt;::value_type, if pred(A, B) == true, then hf(A) == hf(B) shall be true.

<h2>Parameters</h2>

pat_first, pat_last - a pair of iterators designating the string to be searched for 
hf - a callable object used to hash the elements of the string 
pred - a callable object used to determine equality

<h2>Exceptions</h2>

Any exceptions thrown by 

 
* the copy constructor of RandomIt1; 
* the default constructor, copy constructor, and copy assignment operator of the value type of RandomIt1; or 
* the copy constructor and function call operator of BinaryPredicate or Hash. 

 
May also throw std::bad_alloc if additional memory required for internal data structures cannot be allocated. 

 
&nbsp;std::boyer_moore_searcher::operator() 

 

 
template&lt; class RandomIt2 &gt; <i>(since C++17)</i> 
std::pair&lt;RandomIt2,RandomIt2&gt; operator()( RandomIt2 first, RandomIt2 last ) const; 

 
The member function called by the Searcher overload of std::search to perform a search with this searcher. RandomIt2 must meet the requirements of LegacyRandomAccessIterator. 
RandomIt1 and RandomIt2 must have the same value type.

<h2>Parameters</h2>

first, last - a pair of iterators designating the string to be examined

<h2>Return value</h2>

If the pattern ([pat_first, pat_last)) is empty, returns make_pair(first, first). 
Otherwise, returns a pair of iterators to the first and one past last positions in [first, last) where a subsequence that compares equal to [pat_first, pat_last) as defined by pred is located, or make_pair(last, last) otherwise. 

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
                          std::boyer_moore_searcher(
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
