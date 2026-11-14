---
title: "stdinput_iterator_tagstdoutput_iterator_tagstdforward_iterator_tagstdbidirectional_iterator_tagstdrandom_access_iterator_tagstdcontiguous_iterator_tag(3)"
name: "stdinput_iterator_tagstdoutput_iterator_tagstdforward_iterator_tagstdbidirectional_iterator_tagstdrandom_access_iterator_tagstdcontiguous_iterator_tag"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinput_iterator_tagstdoutput_iterator_tagstdforward_iterator_tagstdbidirectional_iterator_tagstdrandom_access_iterator_tagstdcontiguous_iterator_tag/"
---

std::input_iterator_tag,std::output_iterator_tag,std::forward_iterator_tag,std::bidirectional_iterator_tag,std::random_access_iterator_tag,std::contiguous_iterator_tag - std::input_iterator_tag,std::output_iterator_tag,std::forward_iterator_tag,std::bidirectional_iterator_tag,std::random_access_iterator_tag,std::contiguous_iterator_tag

<h2>Synopsis</h2>

Defined in header &lt;iterator&gt; 
struct input_iterator_tag { }; 
struct output_iterator_tag { }; 
struct forward_iterator_tag : public input_iterator_tag { }; 
struct bidirectional_iterator_tag : public forward_iterator_tag { }; 
struct random_access_iterator_tag : public bidirectional_iterator_tag { }; 
struct contiguous_iterator_tag: public random_access_iterator_tag { }; <i>(since C++20)</i> 
Defines the category of an iterator. Each tag is an empty type and corresponds to one of the 
five 
<i>(until C++20)</i> 
six 
<i>(since C++20)</i> iterator categories: 
* input_iterator_tag corresponds to LegacyInputIterator. 
* output_iterator_tag corresponds to LegacyOutputIterator. 
* forward_iterator_tag corresponds to LegacyForwardIterator. 
* bidirectional_iterator_tag corresponds to LegacyBidirectionalIterator. 
* random_access_iterator_tag corresponds to LegacyRandomAccessIterator. 
* contiguous_iterator_tag corresponds to LegacyContiguousIterator. <i>(since C++20)</i> 
Iterator category tags carry information that can be used to select the most efficient algorithms for the specific requirement set that is implied by the category. 
For every iterator type It, a typedef std::iterator_traits&lt;It&gt;::iterator_category is available, which is an alias to one of these 
five 
<i>(until C++20)</i> 
six 
<i>(since C++20)</i> tag types. 
Additionally, std::iterator_traits&lt;It&gt;::iterator_­concept may be used to indicate conformance to the iterator concepts.<i>(since C++20)</i> 
Notes <i>(since C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i> 
There is no separate tag for LegacyContiguousIterator. 

<h2>Example</h2>

Common technique for algorithm selection based on iterator category tags is to use a dispatcher function (the alternative is std::enable_if) 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;list&gt;

#include &lt;iterator&gt;
template &lt;class BDIter&gt;

void alg(BDIter, BDIter, std::bidirectional_iterator_tag)

{
    std::cout &lt;&lt; &quot;alg() called for bidirectional iterator\n&quot;;
}
template &lt;class RAIter&gt;

void alg(RAIter, RAIter, std::random_access_iterator_tag)

{
    std::cout &lt;&lt; &quot;alg() called for random-access iterator\n&quot;;
}
template &lt;class Iter&gt;

void alg(Iter first, Iter last)

{
    alg(first, last,
        typename std::iterator_traits&lt;Iter&gt;::iterator_category());
}
int main()

{
    std::vector&lt;int&gt; v;
    alg(v.begin(), v.end());
    std::list&lt;int&gt; l;
    alg(l.begin(), l.end());
    //    std::istreambuf_iterator&lt;char&gt; i1(std::cin), i2;

    //    alg(i1, i2); // compile error: no matching function for call
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;alg() called for random-access iterator 
&nbsp;<wbr>&nbsp;alg() called for bidirectional iterator

<h2>See also</h2>

iterator base class to ease the definition of required types for simple iterators 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
(deprecated in C++17) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides uniform interface to the properties of an iterator 
iterator_traits <i>(class template)</i> 
